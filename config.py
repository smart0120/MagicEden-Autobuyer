import json

from dotenv import load_dotenv
import os

from helpers.utils import cInput

load_dotenv()

CONFIG = json.load(open('config.json'))
ELEMENTS = json.load(open('helpers/elements.json'))

SEED_PHRASE = os.getenv("SEED_PHRASE")
PASSWORD = os.getenv("PASSWORD")

COOLDOWN = 60 * int(CONFIG["cooldown"])
CLOSE_BROWSER = CONFIG["closeBrowser"]

COLLECTION_URL = str(cInput("Enter Collection URL"))
WILLING_PRICE = float(cInput("Enter Willing Price [in SOL]"))
