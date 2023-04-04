from src.config.discord import bot


@bot.event
async def on_ready():
    print(f'Logado: {bot.user}')
