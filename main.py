import discord
from discord import player
from discord.ext import commands
import os
import random

from discord.ext.commands.core import check

client = commands.Bot(command_prefix = '#')
responses = ['walter', 'i like fire trucks', 'i like moster trucks', 'i like fire trucks and moster trucks']
trucks = ['https://gph.is/g/EGyJx5o','http://gph.is/1UTFMB3']
walterBall = ['It is certain','It is decidedly so','Without a doubt','Yes, definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy try again','Ask again later',
'Better not tell you now','Cannot predict now','Concentrate and ask again','Don''t count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful','walter','i like fire trucks','i like moster trucks','i like fire trucks and moster trucks']
cardNum = ['A','2','3','4','5','6','7','8','9','J','Q','K']
cardType = ['Hearts','Diamonds','Spades','Clubs']
playingBlackjack = False
hits = False

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

@client.command(name='blackjack')
async def blackjack(context):
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
              break
          elif sumList(dealerCards) > sumList(playerCards):
              await context.send('Walter wins')
              break
          else:
              await context.send('You win!')
              break
      elif sumList(dealerCards) > 21:
          await context.send('Walter has busted!')
          break
  if sumList(playerCards) == 21:
    await context.send('You win! You have blackjack!')
  elif sumList(playerCards) > 21:
    await context.send('You have busted!')      

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
    elif "silento" in message.content.lower():
      await message.channel.send("<:_1_:793687054453833739>")
  await client.process_commands(message)


client.run('ODY3OTA4MDkxNzMwMDY3NDg2.YPn8Zg.gIXF9-pJYieVZjKF5CzRR9Ug_ys')