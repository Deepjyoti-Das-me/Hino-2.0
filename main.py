import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import datetime
import asyncio
import time
import random
import aiohttp
import json
from discord import app_commands

token = 'MTIzNDU2MTk5Mjk4MzgzODgzMA.G3V2eO.sYtJP7Ae-ihU_rdjm1_2T4dPzxQ2fcuh4R_Ooc'  # Replace with your actual bot token

# Enable intents
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.guilds = True  # Make sure to enable the necessary intents
intents.members = True  # Enable member intents if you need them

client = commands.Bot(command_prefix="h!", intents=intents)

# Events
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(
        type=discord.ActivityType.watching, name=f"on {len(client.guilds)} servers | h!help"
    ))
    print("Ready")
    await client.tree.sync()  # Sync the slash commands

# Slash command example
@client.tree.command(name="ping", description="Ping the bot")
async def slash_ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

# Example function to add rules slash command
@client.tree.command(name="rules", description="Show the server rules")
async def slash_rules(interaction: discord.Interaction):
    rules_text = "1. Be respectful\n2. No spamming\n3. Follow Discord's TOS"
    await interaction.response.send_message(rules_text)

# Prefix command example
@client.command(name="ping")
async def ping_command(ctx):
    await ctx.send("Pong!")

# Prefix command for server info
@client.command(name="serverinfo")
async def prefix_serverinfo(ctx):
    guild = ctx.guild
    embed = discord.Embed(title=f"{guild.name}", description="Server Information", color=discord.Color.blue())
    embed.add_field(name="Server ID", value=guild.id, inline=True)
    embed.add_field(name="Member Count", value=guild.member_count, inline=True)
    embed.add_field(name="Owner", value=guild.owner, inline=True)
    await ctx.send(embed=embed)



client.run(token)
