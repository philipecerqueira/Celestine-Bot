import src.commands.hello
import src.events.on_message
import src.events.on_ready
from src.config.discord import celestine
from src.config.env import env_config

celestine.run(env_config['TOKEN'])
