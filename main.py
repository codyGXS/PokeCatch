import os
import config
import difflib
import sqlite3

count = 0
f = open('pokes.txt', 'r')
file = f.read()
file = file.split('\n')
for i in file:
    if len(i) < 2:
        del file[file.index(i)]
mon_list = []
for i in file:
    if len(i) >= 3:
        mon_list.append(i)
import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
from keep_alive import keep_alive
import requests
from discord_webhook import DiscordWebhook
TOKEN = "" 1042192012100784129
: 
"MTA0MjE5MjAxMjEwMDc4NDEyOQ.GIKxM4._kHrF8aUPxNpIzMIsyJ2olmXNucwfr1_d1Eweg"

editing = {

}
req = requests.get("https://discord.com/api/path/to/the/endpoint")

print(req)
import time

import random

client = commands.Bot(command_prefix='.')

client._skip_check = lambda x, y: False

@tasks.loop(seconds=0.2)
async def spammer():
  text_channel = client.get_channel(config.spam_channel_id)
 # print(text_channel)
  if text_channel != None:
    num = random.randint(1,10000000000000000000000000)
    await text_channel.send(num)
    intervals = [5]
    await asyncio.sleep(random.choice(intervals))

@tasks.loop(seconds=14400)
async def sleeper():
  time.sleep(seconds = 3600)
  spammer.start()
spammer.start()
hint = ""

hint = ""
@client.event
async def on_message(message):
      
      
      def check(m):
          return m.channel == message.channel and m.author != client.user and "The pokémon is" in m.content

      global hint

   
    #if "The pokémon is" in message.content:
      #await message.delete()
      embeds = message.embeds
      if not message.embeds:
        await client.process_commands(message)
        return
      title = (embeds[0].to_dict()['title'])
  
      if message.channel.id == config.catching_poke_channels:
        if "pokémon has appeared" in title:
          hint = ""
          
          m = await message.channel.send(config.poketwo_prefix +"hint")
          
          while True:
            response = await client.wait_for('message', check = check, timeout=300) 
            if "The pokémon is" in response.content:
              break
        
      s = response.content.split(" is ")[1].replace(".","")
      print(s)
      x = get_mon(s)
      print(x)
      first_options = x
      for i in first_options:
        if message.channel.id == config.catching_poke_channels:
          if config.list_poke_for_you == False:
            await message.channel.send(config.poketwo_prefix+"catch "+i)
          else:
              if config.list_poke_for_you == True:
                await message.channel.send("Name: " + i)
      
def get_mon(val):
  val = val.lower()
  while "\_" in val:
      val = val.replace("\_", "-")
        #print(val)
  length = len(val)
  l = list(val)
  new_chars = []
  
  if config.choose_pokemons == False:
    with open('pokes.txt') as f:
         lines = [line.rstrip() for line in f]
  else:
    if config.choose_pokemons == True:
      with open('certain_pokes.txt') as f:
         lines = [line.rstrip() for line in f]
        
  new_names = []
  for i in lines:
    if len(i) == length:
      new_names.append(i)
  #print(new_names)
  final_list = []
  for i in new_names:
    name_list = list(i)
    index = 0
    #print(i)

    flag = False
    for k in l:
      if name_list[index] != k and k != "-":
       # print(name_list[index]+"!="+k)
        flag = True
      index = index+1
    if not flag:
      final_list.append(i)
  #print(final_list)
  return final_list
        


@client.command()
async def catchrate(ctx):
  global count
  count = 0
  print(count)
  await asyncio.sleep(60)
  catch_rate = count/60
  await ctx.send(f'the catch rate is {count} mons per minute')


@client.command()
async def stop(ctx):
    spammer.stop()

@client.command()
async def spam(ctx):
  return
  spammer.start()
  
@client.command()
async def say(ctx, *, args):
  
  await ctx.send(args)

@client.command(aliases=['p', 'pm'])
async def pokemon(ctx, list):

  await ctx.send(config.poketwo_prefix + "p " + str(list))

keep_alive()
client.run(TOKEN,bot=False)
