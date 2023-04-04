import src.commands.hello
import src.events.on_message
import src.events.on_ready
from src.config.discord import bot
from src.config.env import env_config

bot.run(env_config['TOKEN'])
