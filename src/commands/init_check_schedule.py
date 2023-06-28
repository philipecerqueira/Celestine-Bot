from src.config.discord import celestine

from ..events.check_schedule import check_schedule


@celestine.command()
async def init_check_schedule(context):
    channel = context.channel

    await channel.send("Automatic checks for thread creation started successfully!")
    await check_schedule(context)
