import discord
from discord.ext.commands import Bot, Cog, command
import aiohttp
import random
from app.utils.constants import ANOUNCES_ROLE_EVENT, ANOUNCES_ROLE_SHOP


class Commands(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print("Commands plugin loaded")
        self.bot.log.info("Commands module loaded")

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
    async def announce(self, ctx, title):
        await ctx.message.delete()

        for role in ctx.author.roles:
            if role.id == int(ANOUNCES_ROLE_EVENT):
                embed = discord.Embed(title=title, color=discord.Color.gold())
                await ctx.send(embed=embed)

            elif role.id == int(ANOUNCES_ROLE_SHOP):
                embed = discord.Embed(title=title, color=discord.Color.red())
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Commands(bot))
