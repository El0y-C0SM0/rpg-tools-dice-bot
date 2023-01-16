from disnake.ext import commands
from packages.calc import Calc

class CalcCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    ###Realiza o comando de calcular numeros###
    @commands.slash_command(name='calc', description='calcula uma operção entre dois numeros')
    async def calc(self, inter, number1, operator, number2=1):
        calculo = Calc(number1=number1, operacao=operator, number2=number2)
        resultado = f'Operação: ` {number1} {operator} {number2} `\nResultado: ` {calculo.calcula()} `'
        resultado = resultado.replace('.', ',')

        await inter.response.send_message(resultado)

def setup(bot: commands.Bot):
    bot.add_cog(CalcCommand(bot))