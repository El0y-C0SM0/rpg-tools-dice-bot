from disnake.ext import commands
from packages.rolldice import RollDice 

### Realiza o comando de rolagem de dados que envia na dm ###
class RollMaster(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name='roll-master', description='Rola dados e envia na DM. Exemplo de solicitação: 2d20+2 d6.')
    async def roll(self, inter, solicitacao: str = 'd20'):
        dado = RollDice(solicitacao)
        resultado = dado.faz_rolagens()
        resultado = resultado.replace('[', '` [')
        resultado = resultado.replace(']', '] `')
        resultado = resultado.replace('<-', '⟵')
        await inter.author.send(f'Solicitação: ` {dado.solicitacao} `\nResultado:\n{resultado}')
        await inter.response.send_message('Rolado! Boa Sorte!')
        
def setup(bot: commands.Bot):
    bot.add_cog(RollMaster(bot))
