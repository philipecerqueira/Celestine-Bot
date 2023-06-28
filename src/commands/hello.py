from src.config.discord import celestine


@celestine.command()
async def hello(message):
    await message.channel.send(
        "Hello! I'm Celestine, an intelligent assistant here on the server. I'm here to help and enhance your experience.\n\nIf you don't know my commands use *!help*"
    )
