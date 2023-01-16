import disnake
import os
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv('secret.env')

TOKEN = os.environ["TOKEN_BOT"]

bot = commands.Bot()

### Carrega as cogs da pasta commands ###
def load_cogs(bot):
    for file in os.listdir('commands'):
        if file.endswith('.py'):
            cog = file[:-3]
            bot.load_extension(f'commands.{cog}')

load_cogs(bot)

@bot.event
async def on_ready():
    print('O bot tá on')

    await bot.change_presence(activity = disnake.Game('RPG'))

bot.run(TOKEN)