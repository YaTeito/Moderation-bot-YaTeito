import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands

class Errors(commands.Cog):

    def __init__(self, client):
        self.client = client
        print('Errors {} is loaded'.format(self.__class__.__name__))
    
    

def setup(client):
    client.add_cog(Errors(client))