from osu import Client, AuthHandler, Scope
from dotenv import load_dotenv
from runners.server import run_server
from runners.discord import run_discord
from util import userAuthenticate
import sqlite3
import asyncio
import nest_asyncio
from threading import Thread
import os
load_dotenv()


def load_db():
    global c, db
    db = sqlite3.connect("data.db", check_same_thread=False)
    c = db.cursor()
    c.execute("create table if not exists users(discordID int(20), osuID int(15))")
    return c, db



client_id = int(os.getenv('osu_client_id'))
client_secret = os.getenv('osu_client_secret')
redirect_url = os.getenv('redirect_uri')
auth = AuthHandler(client_id, client_secret, redirect_url, Scope.identify())
c, db = load_db()

run_discord(auth, userAuthenticate, c, db)