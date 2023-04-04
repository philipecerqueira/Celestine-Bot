from src.config.discord import bot


@bot.event
async def on_message(message):
    print(f'Message de {message.author}: {message.content}')
    await bot.process_commands(message)
