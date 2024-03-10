import disnake
from disnake.ext import commands

import time
import sqlite3
import asyncio

tdict = {}

connection = sqlite3.connect("server.db") 
cursor = connection.cursor()

class Voice_Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Events {} is loaded'.format(self.__class__.__name__))

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

        if before.channel is None and after.channel is not None:
            time1 = int(time.time()) 
            tdict[member.id] = time1
            while True:
                await asyncio.sleep(60)
                cursor.execute("UPDATE users SET balance = balance + 1 WHERE id = ?", [member.id])
                connection.commit()

        elif after.channel is None:
            voice_time = int(time.time()) - int(tdict[member.id])

            cursor.execute(
                "UPDATE users SET voice_time = voice_time+? WHERE id = ?", [voice_time, member.id])
            connection.commit()

def setup(client):
    client.add_cog(Voice_Events(client))