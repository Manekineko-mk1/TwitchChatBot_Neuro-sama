# Bot.py
from twitchio.ext import commands
import Utilities
import logging
import os
from dotenv import load_dotenv

class Bot(commands.Bot):
    def __init__(self, client_Id, secret, channels, nick):    
        token = Utilities.get_valid_oauth_token(client_Id, secret)
        logging.info(f"Initializing the Bot: token={token}, client_id={client_Id}, secret={secret}, channels={channels}, nick={nick}")
        super().__init__(token=token, client_id=client_Id, prefix='?', initial_channels=channels, nick=nick)

    async def event_ready(self):
        logging.info(f'Logged in as: {self.nick} | User ID: {self.user_id}')
        print(f'Logged in as: {self.nick} | User ID: {self.user_id}')

    @commands.command()
    async def help(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}! Commands available: !help')
        logging.info(f"Responded to user({ctx.author.name})'s !help command")

def main():
    load_dotenv()  # Load environment variables from .env file
    
    # Get environment variables
    client_id = os.getenv('CLIENT_ID')
    secret = os.getenv('CLIENT_SECRET')
    channels = [os.getenv('CHANNEL')]
    nick = os.getenv('BOT_NICK')
    
    Utilities.setup_logging()  # Initialize logging
    Utilities.get_valid_oauth_token(client_id, secret)  # Validate and setup environment variables

    bot = Bot(client_id, secret, channels, nick)
    bot.run()

if __name__ == "__main__":
    main()