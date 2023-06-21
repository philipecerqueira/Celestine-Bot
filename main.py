import src.commands.create_thread
import src.commands.delete_all_threads
import src.commands.hello
import src.commands.init_check_schedule
import src.events.check_schedule
import src.events.on_message
import src.events.on_ready
from src.config.discord import celestine
from src.config.env import env_config

celestine.run(env_config['TOKEN'])
