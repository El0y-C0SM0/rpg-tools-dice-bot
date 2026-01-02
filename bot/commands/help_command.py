import disnake
from disnake.ext import commands


class HelpCog(commands.Cog):
    commands_description = {
        "help": "Mostra todos os comandos disponíveis.",
        "roll": "Rola dados e soma o mod ao total. Ex: 2d20+2 d6.",
        "best": "Rola dados e escolhe o melhor. Ex: 2d20+2 d6.",
        "worst": "Rola dados e escolhe o pior. Ex: 2d20+2 d6.",
        "allmod": "Rola dados e aplica o mod a todos os resultados. Ex: 2d20+2 d6.",
        "coin": "Joga uma moeda.",
        "hiddenroll": "Rola dados secretamente e soma o mod ao total. Ex: 2d20+2 d6.",
        "hiddenbest": "Rola dados secretamente e escolhe o melhor. Ex: 2d20+2 d6.",
        "hiddenworst": "Rola dados secretamente e escolhe o pior. Ex: 2d20+2 d6.",
        "hiddenallmod": "Rola dados secretamente e aplica o mod a todos os resultados. Ex: 2d20+2 d6.",
    }
    hidden_types = {
        "all": "Sigilo total.",
        "minimum": "Avisa que dados foram rolados",
        "verbose": "Avisa quais dados foram rolados",
    }

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def get_commands_description(self):
        descripiton = ""

        for command, description in self.commands_description.items():
            descripiton += f"- `/{command}`: {description}\n"

        return descripiton

    def get_hidden_types_description(self):
        descripiton = ""

        for hidden_type, description in self.hidden_types.items():
            descripiton += f"- `{hidden_type}`: {description}\n"

        return descripiton

    def get_solicitacoes_description(self):
        description = """\
- `2d20+2`: Rola dois dados de 20 lados e soma 2 ao resultado.
- `d6`: Rola um dado de 6 lados.
- `3d13`: Rola três dados de 13 lados."""

        return description

    def get_operadores_description(self):
        description = """\
- `+`: Soma o valor ao resultado.
- `-`: Subtrai o valor do resultado.
- `*`: Multiplica o resultado pelo valor.
- `/`: Divide o resultado pelo valor.
- `**`: Eleva o resuldado ao valor."""

        return description

    @commands.slash_command(
        name="help", description="Mostra todos os comandos disponíveis."
    )
    async def help(self, inter):
        await inter.response.defer()

        embed = disnake.Embed(
            title="RPGTools",
            description="Estou aqui para rolar seus dados :)",
            color=0x00FF00,
        )
        embed.add_field(
            name="Comandos", value=self.get_commands_description(), inline=False
        )
        embed.add_field(
            name="Tipos de sigilo",
            value=self.get_hidden_types_description(),
            inline=False,
        )
        embed.add_field(
            name="Solicitações", value=self.get_solicitacoes_description(), inline=False
        )
        embed.add_field(
            name="Operadores", value=self.get_operadores_description(), inline=False
        )
        embed.set_footer(
            text="Feito por El0y C0sm0s (https://github.com/El0y-C0SM0).",
            icon_url="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
        )

        await inter.edit_original_response(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(HelpCog(bot))
