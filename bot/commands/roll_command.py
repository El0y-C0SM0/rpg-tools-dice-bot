import disnake
from disnake.ext import commands

from core import *
from commands.mixin import RollCogMixin

class RollCog(RollCogMixin, commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name='roll', description='Rola dados e soma o mod ao total. Ex: 2d20+2 d6.')
    async def roll(self, inter, solicitacao: str = 'd20'):
        await inter.response.defer()

        out = self._roll_dices(solicitacao, RollTypes.ROLL)

        await inter.edit_original_response(out)

    @commands.slash_command(name='best', description='Rola dados e escolhe o melhor. Ex: 2d20+2 d6.')
    async def best(self, inter, solicitacao: str = 'd20'):
        await inter.response.defer()

        out = self._roll_dices(solicitacao, RollTypes.BEST)

        await inter.edit_original_response(out)

    @commands.slash_command(name='worst', description='Rola dados e escolhe o pior. Ex: 2d20+2 d6.')
    async def worst(self, inter, solicitacao: str = 'd20'):
        await inter.response.defer()

        out = self._roll_dices(solicitacao, RollTypes.WORST)

        await inter.edit_original_response(out)

    @commands.slash_command(name='allmod', description='Rola dados e aplica o mod a todos os resultados. Ex: 2d20+2 d6.')
    async def allmod(self, inter, solicitacao: str = 'd20'):
        await inter.response.defer()

        out = self._roll_dices(solicitacao, RollTypes.ALL)

        await inter.edit_original_response(out)

def setup(bot: commands.Bot):
    bot.add_cog(RollCog(bot))
