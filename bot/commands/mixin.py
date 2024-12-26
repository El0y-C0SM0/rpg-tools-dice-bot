import disnake
from disnake.ext import commands
from bot.core import *

class RollCogMixin: 
    def format_output(self, roll: str):
        out = str(roll)
        out = out.replace('[', '`[')
        out = out[::-1].replace('( ', '( `', 1)[::-1]
        out = out.replace(' ⟵ ', '** ⟵')
        out = '**' + out.replace('\n', '\n**')

        return out
    
    @property
    def error_message(self):
        return f"Os dados cairam no chão =/"
    
    def _roll_dices(self, solicitacao, roll_type) -> str:
        try:
            roll = Rolls(solicitacao, roll_type)
            out = self.format_output(roll)
            return out
        except:
            return self.error_message
        