import discord
from discord.ext import commands

from helpers.hiscore import Hiscore
from helpers.urls import clue_icon, bounty_icon, lms_icon


class Scores(commands.Cog):
    """ Score commands used to pull stats from hiscore page.
    This includes LMS, Bounty Hunter, and clue scrolls.
    (Logout or hop to update hiscore page) """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='bounty',
                      description='Pulls bounty hunter scores for a specific username',
                      aliases=['bh'],
                      case_insensitive=True)
    async def bounty_lookup(self, ctx, *username):
        """ Shows bounty hunter scores and rank """
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Bounty Hunter", description=f'{safe_name}')
            embed.set_thumbnail(url=bounty_icon)
            if user.bounty_hunter_hunter_score == '-1':
                embed.add_field(name="Hunter", value="You have never played as Hunter", inline=False)
            else:
                embed.add_field(name="Hunter",
                                value=f'**{int(user.bounty_hunter_hunter_score):,}** score (Rank {int(user.bounty_hunter_hunter_rank):,})',
                                inline=False)
            if user.bounty_hunter_rogue_rank == '-1':
                embed.add_field(name="Rogue", value="You have never played as Rogue", inline=False)
            else:
                embed.add_field(name="Rogue",
                                value=f'**{int(user.bounty_hunter_rogue_score):,}** score (Rank {int(user.bounty_hunter_rogue_rank):,})',
                                inline=False)
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return

    @commands.command(name='lms',
                      description='Pulls LMS scores for a specific username',
                      aliases=[],
                      case_insensitive=True)
    async def lms_lookup(self, ctx, *username):
        """ Shows LMS scores and rank """
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Last Man Standing", description=f'{safe_name}')
            embed.set_thumbnail(url=lms_icon)
            if user.lms_score == '-1':
                embed.add_field(name="Score", value="You have never played LMS")
            else:
                embed.add_field(name="Score", value=f'**{int(user.lms_score):,}** score (Rank {int(user.lms_rank):,})',
                                inline=False)
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return

    @commands.command(name='clues',
                      description='Pulls clue scroll scores for a specific username',
                      aliases=['clue', 'scrolls'],
                      case_insensitive=True)
    async def clue_lookup(self, ctx, *username):
        """ Shows clue scrolls for user """
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Clue Scrolls", description=f'{safe_name}')
            embed.set_thumbnail(url=clue_icon)
            if user.all_clues_rank == '-1':
                embed.add_field(name="Nothing found", value="You haven't solved any clue scrolls", inline=True)
            else:
                embed.add_field(name="Total clues",
                                value=f'**{int(user.all_clues_score):,}** (Rank {int(user.all_clues_rank):,})',
                                inline=True)
            if user.beginner_clues_rank != '-1':
                embed.add_field(name="Beginner clues",
                                value=f'**{int(user.beginner_clues_score):,}** (Rank {int(user.beginner_clues_rank):,})',
                                inline=True)
            if user.easy_clues_rank != '-1':
                embed.add_field(name="Easy clues",
                                value=f'**{int(user.easy_clues_score):,}** (Rank {int(user.easy_clues_rank):,})',
                                inline=True)
            if user.medium_clues_rank != '-1':
                embed.add_field(name="Medium clues",
                                value=f'**{int(user.medium_clues_score):,}** (Rank {int(user.medium_clues_rank):,})',
                                inline=True)
            if user.hard_clues_rank != '-1':
                embed.add_field(name="Hard clues",
                                value=f'**{int(user.hard_clues_score):,}** (Rank {int(user.hard_clues_rank):,})',
                                inline=True)
            if user.elite_clues_rank != '-1':
                embed.add_field(name="Elite clues",
                                value=f'**{int(user.elite_clues_score):,}** (Rank {int(user.elite_clues_rank):,})',
                                inline=True)
            if user.master_clues_rank != '-1':
                embed.add_field(name="Master clues",
                                value=f'**{int(user.master_clues_score):,}** (Rank {int(user.master_clues_rank):,})',
                                inline=True)
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return


# Cog setup
def setup(bot):
    bot.add_cog(Scores(bot))
