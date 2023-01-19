import discord
import psycopg2
import responses
from settings import *


async def send_message(message, user_message, db_conn):
    try:
        response = responses.handle_response(user_message, db_conn)
        await message.author.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    # Set up bot client
    TOKEN = settings["TOKEN"]

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # Set up database cursor
    db_conn = psycopg2.connect(
    database = settings["db_name"],
    host = settings["db_host"],
    port = settings["db_port"],
    user = settings["db_user"],
    password = settings["db_password"]
    )

    # Startup finished
    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")

    #React to commands
    @client.event
    async def on_message(message):
        # Ignore messages from itself
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Logging in terminal
        print(f"{username} said '{user_message}' in {channel}")

        await send_message(message, user_message, db_conn)


    client.run(TOKEN)
