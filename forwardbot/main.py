from forwardbot import forward_bot
import os
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    bot = forward_bot.forward_bot()
    # Set discord token in .env file found in repository
    bot.run(os.getenv('DISCORD_TOKEN'))




