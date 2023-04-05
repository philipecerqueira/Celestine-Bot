from src.config.discord import celestine


@celestine.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    await celestine.process_commands(message)
