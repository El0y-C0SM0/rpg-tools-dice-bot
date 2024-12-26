from disnake.ext import commands
from disnake import Option, OptionType, OptionChoice

from bot.core import *
from bot.commands.mixin import RollCogMixin


class HiddenTypes:
    ALL = 'a'
    MINIMUM = 'm'
    VERBOSE = 'v'


hidden_type_option = Option(
    name='hidden_type',
    description='Nivel de sigilo',
    type=OptionType.string,
    required=False,
    choices=[
        OptionChoice(name='All', value=HiddenTypes.ALL),
        OptionChoice(name='Minimum', value=HiddenTypes.MINIMUM),
        OptionChoice(name='Verbose', value=HiddenTypes.VERBOSE)
    ]
)

solicitacao_option = Option(
    name='solicitacao',
    description='Dados a serem rolados',
    type=OptionType.string,
    required=False
)


class HiddenRollCog(RollCogMixin, commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot  

    def _get_verbose_message(self, solicitacao):
        if ' ' in solicitacao:      
            return f"{solicitacao} foram rolados..."
        return f'{solicitacao} foi rolado...'
    
    def _get_minimum_message(self, solicitacao):
        return 'Dados foram rolados...'
    
    def _get_alert_roll(self, inter, hidden_type, solicitacao):
        if hidden_type == HiddenTypes.MINIMUM:
            return inter.send(self._get_minimum_message(solicitacao))
        elif hidden_type == HiddenTypes.VERBOSE:
            return inter.send(self._get_verbose_message(solicitacao))
        
        return inter.send(f'O parametro `{hidden_type}` é invalido.', ephemeral=True)

    @commands.slash_command(
        name='hiddenroll', 
        description='Rola dados secretamente e soma o mod ao total. Ex: 2d20+2 d6.',
        options=[hidden_type_option, solicitacao_option]
    )
    async def hiddenroll(self, inter, hidden_type: str = HiddenTypes.ALL, solicitacao: str = 'd20'):
        if hidden_type != HiddenTypes.ALL:
            await self._get_alert_roll(inter, hidden_type, solicitacao)

        out = self._roll_dices(solicitacao, RollTypes.ROLL)

        await inter.send(out, ephemeral=True)

    @commands.slash_command(
        name='hiddenbest', 
        description='Rola dados secretamente e escolhe o melhor. Ex: 2d20+2 d6.',
        options=[hidden_type_option, solicitacao_option]
    )
    async def hiddenbest(self, inter, hidden_type: str = HiddenTypes.ALL, solicitacao: str = 'd20'):
        if hidden_type != HiddenTypes.ALL:
            await self._get_alert_roll(inter, hidden_type, solicitacao)

        out = self._roll_dices(solicitacao, RollTypes.BEST)

        await inter.send(out, ephemeral=True)

    @commands.slash_command(
        name='hiddenworst', 
        description='Rola dados secretamente e escolhe o pior. Ex: 2d20+2 d6.',
        options=[hidden_type_option, solicitacao_option]
    )
    async def hiddenworst(self, inter, hidden_type: str = HiddenTypes.ALL, solicitacao: str = 'd20'):
        if hidden_type != HiddenTypes.ALL:
            await self._get_alert_roll(inter, hidden_type, solicitacao)

        out = self._roll_dices(solicitacao, RollTypes.WORST)

        await inter.send(out, ephemeral=True)

    @commands.slash_command(
        name='hiddenallmod', 
        description='Rola dados secretamente e aplica o mod a todos os resultados. Ex: 2d20+2 d6.',
        options=[hidden_type_option, solicitacao_option]
    )
    async def hiddenallmod(self, inter, hidden_type: str = HiddenTypes.ALL, solicitacao: str = 'd20'):
        if hidden_type != HiddenTypes.ALL:
            await self._get_alert_roll(inter, hidden_type, solicitacao)

        out = self._roll_dices(solicitacao, RollTypes.ALL)

        await inter.send(out, ephemeral=True)


def setup(bot):
    bot.add_cog(HiddenRollCog(bot))