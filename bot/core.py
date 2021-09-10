from discord.ext import commands

from img_api import ImageApi

bot = commands.Bot(command_prefix='/')
img = ImageApi()
