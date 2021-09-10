import discord
import os


client=discord.Client()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))


#commanding compile
@client.event
async def on_message(message):
  if message.author==client.user:
    return
  if message.content.startswith('!hello'):
    await message.channel.send('Hai')
    

client.run(os.environ['Token'])
