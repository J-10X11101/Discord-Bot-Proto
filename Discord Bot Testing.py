# bot.py
import os

import discord
from dotenv import load_dotenv
import time

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Game(name="with your data"))
    channel = discord.utils.get(client.get_all_channels(), name="general") #  Gets the channel named general
    await channel.send(f"ProtoAI Systems Initialised.") #  Sends message to channel

    

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    
    greetings = ["hi protoai", "hello protoai", "hey protoai", "sup protoai", "yo protoai", "greetings protoai"]
    goodbyes = ["bye protoai", "goodbye protoai", "see ya protoai", "later protoai", "cya protoai", "goodnight protoai", "gn protoai", "good night protoai", "going to bed"]
    
    if message.author == client.user:
        return

    else:
        messages = message.content.split(" ")

        for i in range(len(messages)):
            for i in range(len(greetings)):
                if greetings[i] in str(messages[i]).lower():
                    await message.channel.send(f"Hello {message.author}")
                    break
        for i in range(len(greetings)):
            if greetings[i] in str(message.content).lower():
                await message.channel.send(f"Hello {message.author}")
                break

        for i in range(len(goodbyes)):
            if goodbyes[i] in str(message.content).lower():
                await message.channel.send(f"Goodbye {message.author}")
                break

        if (message.content).lower() == "what is the time":
            await message.channel.send(f"The time is {time.asctime()} in AEST")

client.run(TOKEN)