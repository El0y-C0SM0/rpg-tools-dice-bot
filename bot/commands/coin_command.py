from disnake.ext import commands


class CoinCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="coin", description="Joga uma moeda.")
    async def coin(self, inter):
        await inter.response.defer()

        import random

        result = random.choice(["Head", "Tail"])

        await inter.edit_original_response(f"**{result}**")


def setup(bot: commands.Bot):
    bot.add_cog(CoinCog(bot))
