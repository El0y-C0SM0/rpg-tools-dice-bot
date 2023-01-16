from disnake.ext import commands
from packages.rolldice import RollDice 

### Faz o comando de rolagem de dados ###
class Roll(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name='roll', description='Rola dados. Exemplo de solicitação: 2d20+2 d6.')
    async def roll(self, inter, solicitacao: str = 'd20'):
        dado = RollDice(solicitacao)
        resultado = dado.faz_rolagens()
        resultado = resultado.replace('[', '` [')
        resultado = resultado.replace(']', '] `')
        resultado = resultado.replace('<-', '⟵')
        await inter.response.send_message(resultado)

def setup(bot: commands.Bot):
    bot.add_cog(Roll(bot))