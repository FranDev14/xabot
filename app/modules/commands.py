import discord
from discord.ext.commands import Bot, Cog, command
import aiohttp
import random


class Commands(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    # Reddit meme generator
    @command(pass_context=True)
    async def meme(self, ctx):
        embed = discord.Embed(title="test", description="testing")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    @command(name='eraser')
    async def purge(self, ctx, amount=200):
        await ctx.channel.purge(limit=amount)


def setup(bot):
    bot.add_cog(Commands(bot))
