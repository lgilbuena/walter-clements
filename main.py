import discord
from discord import player
from discord.ext import commands
import os
import random
import csvwrite as cs
import time
from discord.ext.commands.core import check
import sorting as sort
types = ['Normal','Fire','Water','Grass','Electric','Ice','Fighting','Poison','Ground','Flying','Psychic','Bug','Rock','Ghost','Dark','Dragon','Steel','Fairy']
listOfPlayers = ['<@302264395038195712>','<@187701360915906560>','<@211640631603232769>']

client = commands.Bot(command_prefix = '#')
responses = ['walter', 'i like fire trucks', 'i like moster trucks', 'i like fire trucks and moster trucks']
trucks = ['https://gph.is/g/EGyJx5o','http://gph.is/1UTFMB3']
walterBall = ['It is certain','It is decidedly so','Without a doubt','Yes, definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy try again','Ask again later',
'Better not tell you now','Cannot predict now','Concentrate and ask again','Don''t count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful','walter','i like fire trucks','i like moster trucks','i like fire trucks and moster trucks']
cardNum = ['A','2','3','4','5','6','7','8','9','J','Q','K']
cardType = ['Hearts','Diamonds','Spades','Clubs']
playingBlackjack = False
hits = False

@client.command(name='shop')
async def shop(context):
  message = "this message is sent via DM"
  await context.author.send(message)
@client.command(name='leaderboard')
async def leaderboard(context):
  userList = cs.leaderboards()
  sortedList = sort.sorting(userList)
  fortmat = sort.formats(sortedList)
  await context.message.channel.send('``` {} ```'.format(fortmat))
@client.command(name='give')
async def give(context,user,amount):
  cs.giveCoin(cs.getID(user),  int(amount) )
  cs.giveCoin(context.author.id,-1 * int(amount) )
  await context.message.channel.send('{} has given {} {} uwucoins.'.format(cs.username(context.author.id),user,amount))
@client.command(name='record')
async def record(context):
  await context.message.channel.send('Username: {}'.format(cs.username(context.author.id)))
  await context.message.channel.send('{} wins and {} losses in blackjack. ({} win ratio) '.format(cs.wins(context.author.id),cs.losses(context.author.id),round(cs.wins(context.author.id)/cs.games(context.author.id),2)))
@client.command(name='register')
async def register(context,username):
    if cs.checker(str(context.author.id)):
        await context.message.channel.send("You sussy baka. You already registered a username with your discord account.")
    else:
        cs.write([context.author.id,username]+[0,0,1000])
        await context.message.channel.send("https://cdn.discordapp.com/attachments/800454220679479309/920581571260583936/Screen_Shot_2016_11_17_at_10.png")
        await context.message.channel.send("Welcome to the dark side.")
@client.command(name='walterball')
async def walterball(context,question):
  await context.message.channel.send(walterBall[random.randint(0,len(walterBall))])
@client.command(name='roll')
async def roll(context, number):
  await context.message.channel.send(random.randint(1,int(number)))
@client.command(name='hit')
async def hit(context):
  if playingBlackjack == True:
    hits = True
@client.command(name='balance')
async def uwucoin(context):
    if cs.checker(str(context.author.id)):
        await context.message.channel.send("{}, you have {} uwucoins.".format(cs.username(context.author.id),cs.balance(context.author.id)))
@client.command(name='blackjack')
async def blackjack(context,uwucoin=None):
  dealerCards = []
  playerCards = []
  def check(m):
    return m.author.id == context.author.id
  def sumList(deck):
    sum = 0
    for x in deck:
        sum += x
    return sum
  def stateCards(deck):
      outLine = ""
      for x in range(len(deck)):
          if x == len(deck)-1:
              outLine += str(deck[x])
          else:outLine += str(deck[x]) + ", "
      return outLine
  if uwucoin == None:
        await context.send('You need to bet an amount.')
  elif int(uwucoin) > cs.balance(context.author.id):
        await context.send('You\'re betting more than you can afford!')
  elif int(uwucoin) <= 0:
        await context.send('Don\'t even try that.')
  elif cs.checker(str(context.author.id)):
    while len(dealerCards) != 2:
        dealerCards.append(random.randint(1,11))
        if len(dealerCards) == 2:
            await context.send('Walter has: ' +str(dealerCards[0])+' & X')

    while len(playerCards) != 2:
        playerCards.append(random.randint(1,11))
        if len(playerCards) == 2:
            await context.send('You have: '+str(playerCards[0])+' & '+str(playerCards[1])+' ('+str(sumList(playerCards))+')')

    
    while sumList(playerCards) < 21:
      await context.send('Hit or stand?')
      message = await client.wait_for('message',check=check)
      if message.content.lower() == 'hit':
        playerCards.append(random.randint(1,11))
        await context.send('You now have a total of ' + str(sumList(playerCards)) + ' from these cards: ' + stateCards(playerCards))
      elif message.content.lower() == 'stand':
        while(sumList(dealerCards) < 17):
          dealerCards.append(random.randint(1,11))
          await context.send('Walter has a total of '+str(sumList(dealerCards))+' with '+stateCards(dealerCards))
        await context.send('Walter has a total of ' + str(sumList(dealerCards)))
        await context.send('You have a total of '+ str(sumList(playerCards))+' with ' + stateCards(playerCards))
        if sumList(dealerCards) <= 21 and sumList(playerCards) <= 21:
            if sumList(dealerCards) == sumList(playerCards):
                await context.send('Issa draw!')
                break
            elif sumList(dealerCards) == 21:
                await context.send('Walter has: ' + str(dealerCards[0]) + ' & ' + str(dealerCards[1]))
                await context.send("Walter has 21 and wins!")
                cs.giveCoin(context.author.id, -1 * int(uwucoin))
                await context.send('You lose {} uwucoins!'.format(uwucoin))
                cs.addWin(context.author.id, 0)  
                break
            elif sumList(dealerCards) > sumList(playerCards):
                await context.send('Walter wins')
                cs.giveCoin(context.author.id, -1 * int(uwucoin))
                await context.send('You lose {} uwucoins!'.format(uwucoin))
                cs.addWin(context.author.id, 0)  
                break
            else:
                await context.send('You win!')
                cs.giveCoin(context.author.id, 1 * int(uwucoin))
                await context.send('You win {} uwucoins!'.format(2*int(uwucoin)))
                cs.addWin(context.author.id, 1)  
                break
        elif sumList(dealerCards) > 21:
            await context.send('Walter has busted!')
            cs.giveCoin(context.author.id, 1 * int(uwucoin))
            await context.send('You win {} uwucoins!'.format(2*int(uwucoin)))
            cs.addWin(context.author.id, 1)  
            break
    if sumList(playerCards) == 21:
      await context.send('You win! You have blackjack!')
      cs.giveCoin(context.author.id, int(round(1.5 * int(uwucoin))))
      await context.send('You win {} uwucoins!'.format(2.5*int(uwucoin)))
      cs.addWin(context.author.id, 1)  
    elif sumList(playerCards) > 21:
      await context.send('You have busted!')
      cs.giveCoin(context.author.id, -1 * int(uwucoin))
      await context.send('You lose {} uwucoins!'.format(uwucoin))  
      cs.addWin(context.author.id, 0)    
      
@client.command(name='assign')
async def makematch(context):
    while len(listOfPlayers) != 0:
        randomIndex = random.randint(0,len(types)-1)
        randomPlayer = random.randint(0,len(listOfPlayers)-1)
        await context.send(str(listOfPlayers[randomPlayer]) + ': ' + str(types[randomIndex]))
        types.remove(types[randomIndex])
        listOfPlayers.remove(listOfPlayers[randomPlayer])
    await context.send('done.')

@client.command(name='join')
async def makematch(context):
    if '<@'+str(context.author.id)+'>' in listOfPlayers:
        await context.send('You already registered idiot.')
    else:
        listOfPlayers.append('<@'+str(context.author.id)+'>')
        await context.send('<@'+str(context.author.id)+'>' + ' has registered.')
        
@client.command(name='list')
async def list(context):
  await context.send(listOfPlayers)

@client.event
async def on_ready():
  print('walter clements reporting for duty')

@client.event
async def on_message(message):
  resline = responses[random.randint(0,3)]
  if message.author == client.user:
    return 
  if not message.content.startswith('#'):
    if random.randint(0, 100) == 69:
      await message.channel.send(resline)
    elif message.content.lower().startswith(responses[3]):
      await message.channel.send(resline)
    elif message.content.lower().startswith(responses[1]):
      await message.channel.send(trucks[1])
    elif message.content.lower().startswith(responses[2]):
      await message.channel.send(trucks[0])
    elif "walter" in message.content.lower():
      await message.channel.send('walter')
    if random.randint(0,1000000) == 420:
      await message.channel.send("<:_1_:793687054453833739><:_2_:793687054683734027><:_3_:793687054780596255><:_4_:793687054915600384>")
      await message.channel.send("<:_5_:793687054894628864><:_6_:793687055183380490><:_7_:793687054898692118><:_8_:793687054969470986>")
      await message.channel.send("<:_9_:793687054915076096><:_10_:793687055140913192><:_11_:793687054960951317><:_12_:793687054964883488>")
      await message.channel.send("<:_13_:793687055011151903><:_14_:793687055107358772><:_15_:793687055015870484><:_16_:793687054978252810>")
  await client.process_commands(message)


client.run('ODY3OTA4MDkxNzMwMDY3NDg2.YPn8Zg.gIXF9-pJYieVZjKF5CzRR9Ug_ys')
