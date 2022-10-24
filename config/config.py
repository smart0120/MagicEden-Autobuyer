import json

from dotenv import load_dotenv
import os

from pkg import c_input

load_dotenv()

__path_to_user_config = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

__config: dict = json.load(open(__path_to_user_config))

user_config = {
    "seed": os.getenv("SEED_PHRASE"),
    "password": os.getenv("PASSWORD"),
    "cooldown": 60 * int(__config.get("cooldown")),
    "close_browser": __config.get("closeBrowser"),
    "collection_url": str(c_input("Enter Collection URL")),
    "willing_price": float(c_input("Enter Willing Price [in SOL]"))
}