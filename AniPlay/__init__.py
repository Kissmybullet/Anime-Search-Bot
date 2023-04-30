from os import environ
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(environ.get("APP_ID", "21814574")),
    api_hash= environ.get("API_HASH", "76950ccd860212311210cbcc2a4bbdd3"),
    bot_token= environ.get("TOKEN", "6096092780:AAFvl2Fej6p_LpB7ttuF35Nrdps0g9IcPq0")
)
