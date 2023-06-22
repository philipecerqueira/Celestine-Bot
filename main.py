import src.actions.create_json
import src.actions.show_json
import src.actions.update_json
import src.commands.create_thread
import src.commands.delete_all_threads
import src.commands.hello
import src.commands.init_check_schedule
import src.commands.setup_schedule
import src.commands.show_schedule
import src.events.check_schedule
import src.events.on_message
import src.events.on_ready
import src.variables
from src.config.discord import celestine
from src.config.env import env_config

celestine.run(env_config['TOKEN'])
