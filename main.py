import discord
import os
import random

client = discord.Client()
responses = ['walter', 'i like fire trucks', 'i like moster trucks', 'i like fire trucks and moster trucks']
trucks = ['https://gph.is/g/EGyJx5o','http://gph.is/1UTFMB3']

@client.event
async def on_ready():
  print('walter clements reporting for duty')

@client.event
async def on_message(message):
  if message.author == client.user:
    return 
  if random.randint(0, 100) == 69:
    await message.channel.send(responses[random.randint(0,3)])
  elif message.content.startswith('i like fire trucks'):
    await message.channel.send(trucks[1])
  elif message.content.startswith('i like moster trucks'):
    await message.channel.send(trucks[0])
  elif "walter" in message.content:
    await message.channel.send(responses[0])
  if message.content.startswith('#roll'):
    number = int(message.content.split("#roll,1")[1])
    await message.channel.send('hello')


client.run('ODY3OTA4MDkxNzMwMDY3NDg2.YPn8Zg.gIXF9-pJYieVZjKF5CzRR9Ug_ys')