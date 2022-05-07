import discord
from discord.ext.commands import Bot, Cog, command
import aiohttp
import random
from os.path import join, dirname


class Commands(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.whitelist_users = join(dirname(__file__), '../configs/whitelisted.json')

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

    @command(name='announce')
    async def announce(self, ctx):
        pass

    @command(name='add_whitelist')
    async def add_whitelist(self, ctx, user: discord.User):
        # Add discord role for whitelist and rcon connection to addit
        pass

    @command(name='remove_whitelist')
    async def remove_whitelist(self, ctx, user: discord.User):
        # Add discord role for whitelist and rcon connection to addit
        pass


def setup(bot):
    bot.add_cog(Commands(bot))
