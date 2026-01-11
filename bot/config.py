import os
import sys
from pathlib import Path

# Adiciona o diretório raiz ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from dotenv import load_dotenv

load_dotenv()

DEBUG = os.environ["DEBUG"] != "False"
TOKEN = None
GUILD_ID = None

if DEBUG:
    TOKEN = os.environ["TOKEN_TESTE"]
    GUILD_ID = os.environ["GUILD_ID_TESTE"]
else:
    TOKEN = os.environ["TOKEN_BOT"]

    if os.environ["GUILD_ID"] != "0":
        GUILD_ID = os.environ["GUILD_ID"]
