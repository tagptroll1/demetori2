import discord
from discord.ext import commands


class Member:
    """Cog for member related commands"""

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Member(bot))