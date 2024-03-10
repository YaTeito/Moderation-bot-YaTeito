import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands

import sqlite3

connection = sqlite3.connect("server.db") 
cursor = connection.cursor()

class Member_Join(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        print('Events {} is loaded'.format(self.__class__.__name__))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if cursor.execute(f"SELECT id FROM users WHERE id = ?", [member.id]).fetchone() is None:
            cursor.execute(f"INSERT INTO users VALUES(?, ?, ?, ?, ?)", [member.id, 0, 0, 'Не установлен', 0])
        else:
            pass
        connection.commit()


def setup(client):
    client.add_cog(Member_Join(client))