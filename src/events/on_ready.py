from src.config.discord import celestine


@celestine.event
async def on_ready():
    print(f'Logged: {celestine.user}')
