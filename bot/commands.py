from aiohttp import ClientResponseError
from discord import Embed
from discord.ext import commands

from .core import img_api

ANIMALS = ['dog', 'cat', 'panda', 'red_panda', 'birb', 'fox', 'koala']

@commands.command()
async def img(ctx, arg=None):
    if arg is None:
        await ctx.send("Используй команду так: /img <животное>.\nЗнаю таких животных: dog, cat, panda, red_panda, birb, fox, koala")
        return

    if arg not in ANIMALS:
        await ctx.send("Не знаю такого животного. Знаю этих: dog, cat, panda, red_panda, birb, fox, koala")
        return

    try:
        image = await img_api.get(arg)
        embed = Embed(title=f"Random {arg}")
        embed.set_image(url=image.link)
        await ctx.send(embed=embed)
    except Exception:
        await ctx.send("Произошла неизвестная ошибка :(")


def init(bot: commands.Bot):
    bot.add_command(img)
