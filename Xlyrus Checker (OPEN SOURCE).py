import discord
from discord.ext import commands
import random
import os
 

os.system('cls')
token = input("Enter Token: ")
client = commands.Bot(command_prefix=commands.when_mentioned_or("$"))
os.system('cls')
os.system(f'title [XLYRUS AFK CHECKER]')
os.system(f'mode 60,20')
 
exoticlikesmen = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
 
@client.event
async def on_ready():
  print(f""" \u001b[31m
 ------------------------------------------------------------------------------------
  say "afk check (tag)" to afkcheck the mentioned user, and it'll count for you.
 ╔══════════════════════════════╗
  ╔═╗╦ ╦╔╦╗╔═╗╔═╗╦ ╦╔═╗╦╔═╔═╗╦═╗
  ╠═╣║ ║ ║ ║ ║║  ╠═╣║╣ ╠╩╗║╣ ╠╦╝
  ╩ ╩╚═╝ ╩ ╚═╝╚═╝╩ ╩╚═╝╩ ╩╚═╝╩╚═
 ╚══════════════════════════════╝
 made by 5tacey#8308 & yy#3000 join discord.gg/chiefjustice
 remade and fixed by exotic#0001 ? ?? ? ? 
-------------------------------------------------------------------------------------
""")
 
@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('afk check'):
        await message.channel.send({exoticlikesmen[0:100]}) 


client.run(token, bot=False)
