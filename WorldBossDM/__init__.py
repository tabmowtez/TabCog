from redbot.core.bot import Red

from .wbdm import WorldBossDM


def setup(bot: Red):
    bot.add_cog(WorldBossDM)
