#!/usr/bin/python3

import os
import discord
import openai
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

openai.api_key = os.getenv("OPENAI_API_KEY")

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    prompt = f"User: {message.content}\nAI:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=50,
        n=1,
        stop=None,
        timeout=15,
    )
    await message.channel.send(response.choices[0].text.strip())

client.run(os.getenv("DISCORD_TOKEN"))
