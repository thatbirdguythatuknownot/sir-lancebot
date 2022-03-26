from random import randint

import discord
from discord.ext import commands

from bot.bot import Bot
from bot.constants import Colours

streaks = {}

class Roulette(commands.Cog):
    "Cog for the Russian Roulette game."

    @commands.command(case_insensitive=True)
    async def roulette(self, ctx: commands.Context) -> None:
        """
        Russian Roulette, a game with 1/6 chance of giving a time-out to a player.
        """
        player_id = ctx.author.id
        player_mention = ctx.author.mention

        if randint(0, 5):
            streaks[player_id] += 1
            embed = discord.Embed(
                title="Click.",
                description=f"{player_mention} is lucky with a current streak of {streaks[player_id]}.",
                colour=Colours.green,
            )
            await ctx.send(embed)
        else:
            streaks[player_id] = 0
            embed = discord.Embed(
                title="BANG!",
                description=f"{player_mention} was not too lucky and lost their streak.",
                colour=Colours.red,
            )
            await ctx.send(embed)


def setup(bot: Bot) -> None:
    """Load the Roulette cog."""
    bot.add_cog(Roulette(bot))
