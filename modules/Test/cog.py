from discord.ext import commands

class Test(commands.Cog, name="실험하는 명령어"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def 실험(self, ctx: commands.Context):
        await ctx.send("완료")    

async def setup(bot: commands.Bot):
    await bot.add_cog(Test(bot))