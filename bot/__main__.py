import logging

from . import commands, core, config

logging.basicConfig(level=logging.INFO)

commands.init(core.bot)

core.bot.run(config.DISCORD_TOKEN)
