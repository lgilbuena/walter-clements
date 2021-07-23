import discord
import os
import random

client = discord.Client()
responses = ['walter', 'i like fire trucks', 'i like moster trucks', 'i like fire trucks and moster trucks']
trucks = ['https://gph.is/g/EGyJx5o','http://gph.is/1UTFMB3']
walterBall = ['It is certain','It is decidedly so','Without a doubt','Yes, definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy try again','Ask again later',
'Better not tell you now','Cannot predict now','Concentrate and ask again','Don''t count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful','walter','i like fire trucks','i like moster trucks','i like fire trucks and moster trucks']

@client.event
async def on_ready():
  print('walter clements reporting for duty')

@client.event
async def on_message(message):
  resline = responses[random.randint(0,3)]
  if message.author == client.user:
    return 
  if random.randint(0, 100) == 69:
    await message.channel.send(resline)
  elif message.content.startswith('#'):
    tempstring = message.content.split('#')[1]
    if tempstring.lower() == 'roll':
      number = int(message.content.split('#roll',1)[1])
      await message.channel.send(random.randint(0,number))
    elif tempstring.lower() == 'walterball':
      await message.channel.send(walterBall[random.randint(0,len(walterBall))])
  elif message.content.lower().startswith(responses[3]):
    await message.channel.send(resline)
  elif message.content.lower().startswith(responses[1]):
    await message.channel.send(trucks[1])
  elif message.content.lower().startswith(responses[2]):
    await message.channel.send(trucks[0])
  elif "walter" in message.content.lower():
    await message.channel.send('walter')


client.run('ODY3OTA4MDkxNzMwMDY3NDg2.YPn8Zg.gIXF9-pJYieVZjKF5CzRR9Ug_ys')