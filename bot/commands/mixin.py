import disnake
from disnake.ext import commands
from main import DEBUG

from bot.core import *


class RollCogMixin:
    def format_output(self, roll: Rolls):
        # out = str(roll)
        outs = str(roll).split("\n")
        formatted_outs = []

        for out in outs:
            out = out.replace("[", "`[")
            out = out[::-1].replace("( ", "( `", 1)[::-1]
            out = out.replace(" ⟵ ", "** ⟵ ")
            out = "**" + out.replace("\n", "\n**")
            formatted_outs.append(out)

        total_line = f"**{sum(r.total for r in roll.rolls)}** ⟵ "
        results = []
        for r in roll.rolls:
            results.extend(r.dices_rolls)
        total_line += (
            f"`[{' + '.join(map(str, results))}]` ({roll._command_line}) TOTAL"
        )

        formatted_outs.append(total_line)

        return "\n".join(formatted_outs)

    @property
    def error_message(self):
        return f"Os dados cairam no chão =/"

    def _roll_dices(self, solicitacao, roll_type) -> str:
        try:
            roll = Rolls(solicitacao, roll_type)
            out = self.format_output(roll)
            return out
        except Exception as e:
            if DEBUG:
                print("Erro ao rolar dados:", solicitacao, roll_type)
                print(e)
            return self.error_message
