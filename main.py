import asyncio
import json

import discord
import requests

global ip, channel_id

# Server ip below
ip = ""
# Discord's channel id below (no quotes)
channel_id = 
# Discord's BOT token below
TOKEN = ""

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    while 1 == 1:
        channel = client.get_channel(channel_id)
        status = (requests.get("https://api.mcsrvstat.us/2/"+ip)).json()
        online = (status['players']["online"])
        await discord.VoiceChannel.edit(channel, name = "Online: "+str(online))
        await asyncio.sleep(60)
client.run(TOKEN)

