import discord
from discord import app_commands
from discord.ext import commands
from discord.utils import get
from threading import Thread
from runners.server import run_server
import asyncio
import os

bot = commands.Bot(command_prefix="y!", intents=discord.Intents.all()) 

# Utility function to send messages with the commands.Bot object
async def send_message(channel_id, message):
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(message)

async def send_message_user(user_id, message):
    user = bot.get_user(user_id)
    if user:
        await user.send(message)

async def sendConfirmation(discord, osu, username):
    await send_message(1290379391385206895, f"Successfully linked user {bot.get_user(discord).mention} to osu! account [{username}](https://osu.ppy.sh/u/{osu})") 
    # 1290379391385206895 : channel ID for #registration-log

async def giveRoles(discord, user):
    roles=[]
    guild = bot.get_guild(1259762777849987112)
    memRole = guild.get_role(1262748633825284096)
    mem = guild.get_member(discord)
    await mem.add_roles(memRole)
    if user.country.code  != "IN":
        intlRole = guild.get_role(1290339364794269718)
        await mem.add_role(intlRole)

@bot.tree.command(name="register", description="Registers and links your osu! profile to allow you access to the rest of the server!")
async def register(interaction: discord.Interaction):
    authURL = auth.get_auth_url().split()[0]+f"&state={interaction.user.id}"
    await interaction.response.send_message(f"Log into your osu! profile to authenticate with yuzubot [here.]({authURL})", ephemeral=True)

@bot.tree.command(name="sendmessage_c", description="(admin only) Sends messages as yunabot")
async def sendmessage_c(interaction: discord.Interaction, message: str, channel: str):
    print(interaction.user.roles)
    if 1259845414119800922 in [x.id for x in interaction.user.roles]:
        channel=int(channel)
        await send_message(channel_id=channel, message=message)
        await interaction.response.send_message("Done.")
    else:
        await interaction.response.send_message("Insufficient permissions.", ephemeral=True)


@bot.tree.command(name="sendmessage_u", description="(admin only) Sends messages as yunabot")
async def sendmessage_u(interaction: discord.Interaction, message: str, user: str):
    if 1259845414119800922 in [x.id for x in interaction.user.roles]:
        user=int(user)
        await send_message_user(user_id=user, message=message)
        await interaction.response.send_message("Done.")
    else:
        await interaction.response.send_message("Insufficient permissions.", ephemeral=True)

@bot.event
async def on_ready():
    await bot.tree.sync()   
    print(f"Logged in as {bot.user}")
    loop=asyncio.get_running_loop()
    Thread(target=run_server, args=(loop, auth, bot, userAuthenticate, c, db)).start()

def run_discord(auth1, userauth, cur, dab):
    global auth, userAuthenticate, c, db
    c = cur
    db = dab
    auth=auth1
    userAuthenticate = userauth
    bot.run(os.getenv('discord_token'))