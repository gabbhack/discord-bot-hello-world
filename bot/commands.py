from aiohttp import ClientResponseError
from discord import Embed
from discord.ext import commands

from core import img

@commands.command()
async def img(ctx, arg):
    try:
        image = await img.get(arg)
        embed = Embed(title=f"Random {arg}")
        embed.set_image(url=image.link)
        await ctx.send(embed=embed)
    except ClientResponseError as response:
        if response.status == 404:
            await ctx.send("Не знаю такого животного. Знаю этих: dog, cat, panda, red_panda, birb, fox, koala")
        else:
            await ctx.send("Произошла неизвестная ошибка :(")
    except Exception:
        await ctx.send("Произошла неизвестная ошибка :(")


def init(bot: commands.Bot):
    bot.add_command(img)
