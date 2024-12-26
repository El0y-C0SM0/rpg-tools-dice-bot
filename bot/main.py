import os
import sys
from pathlib import Path

# Adiciona o diretório raiz ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.environ["DEBUG"] != "False"
TOKEN = None

if DEBUG:
    TOKEN = os.environ["TOKEN_TESTE"]
else:
    TOKEN = os.environ["TOKEN_BOT"]

bot = commands.InteractionBot()

def load_cogs(bot):
    for file in os.listdir('commands'):
        if file.endswith('.py') and 'mixin' not in file and file[0] != '_':
            cog = file[:-3]
            bot.load_extension(f'commands.{cog}')

load_cogs(bot)

@bot.event
async def on_ready():
    await bot.change_presence(activity = disnake.Game('RPG'))

    print('O bot tá on')
    print(f"debug: {DEBUG}")

bot.run(TOKEN)