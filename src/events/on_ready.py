from src.config.discord import celestine


def get_discord_channel():
    for guild in celestine.guilds:
        for channel in guild.text_channels:
            return celestine.get_channel(channel.id)


@celestine.event
async def on_ready():
    print(f'Logged: {celestine.user}')

    channel = get_discord_channel()

    if channel is not None:
        await channel.send("I'm online, need me just call! ;D. If you don't know my commands use *!help*")
