from osu import Client, AuthHandler, Scope
from discord.ext import commands
from runners.discord import send_message, send_message_user, sendConfirmation, giveRoles
import sqlite3

def loadObjects(authParent: AuthHandler, botParent: commands.Bot):
    global auth, bot
    auth = authParent
    bot = botParent

async def userAuthenticate(bot, auth, code, discord, c, db):
    auth.get_auth_token(code)
    client = Client(auth)
    user = client.get_own_data()
    c.execute(f"select * from users where osuID = {user.id}")
    res = c.fetchall()
    res=[]
    if res == []:
        await giveRoles(discord, user)
        c.execute(f"insert into users values(?, ?);", (discord, user.id))
        db.commit()
        print("confirm")
        await sendConfirmation(discord, user.id, user.username)
    else:
        print("already exist")
        await send_message_user(discord, "You have already linked with yuzubot on another account. Please note that you are allowed to have only one account in the osu!India CBT server at a time. If you have changed Discord accounts, DM an admin.")