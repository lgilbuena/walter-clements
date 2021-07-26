import discord
from discord.ext import commands
import os
import random

client = commands.Bot(command_prefix = '#')
responses = ['walter', 'i like fire trucks', 'i like moster trucks', 'i like fire trucks and moster trucks']
trucks = ['https://gph.is/g/EGyJx5o','http://gph.is/1UTFMB3']
walterBall = ['It is certain','It is decidedly so','Without a doubt','Yes, definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy try again','Ask again later',
'Better not tell you now','Cannot predict now','Concentrate and ask again','Don''t count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful','walter','i like fire trucks','i like moster trucks','i like fire trucks and moster trucks']
cardNum = ['A','2','3','4','5','6','7','8','9','J','Q','K']
cardType = ['Hearts','Diamonds','Spades','Clubs']

@client.command(name='walterball')
async def walterball(context,question):
  await context.message.channel.send(walterBall[random.randint(0,len(walterBall))])
@client.command(name='roll')
async def roll(context, number):
  await context.message.channel.send(random.randint(1,int(number)))
@client.command(name='blackjack')
async def blackjack(context):
  dealerCards = []
  playerCards = []
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
          await context.channel.send('Dealer has:',dealerCards[0],'& X')

  while len(playerCards) != 2:
      playerCards.append(random.randint(1,11))
      if len(playerCards) == 2:
          await context.channel.send('You have:',playerCards[0],'&',playerCards[1],'(',sumList(playerCards),')')


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
  await client.process_commands(message)


client.run('ODY3OTA4MDkxNzMwMDY3NDg2.YPn8Zg.gIXF9-pJYieVZjKF5CzRR9Ug_ys')