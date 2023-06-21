from src.config.discord import celestine

from ..events.check_schedule import check_schedule


@celestine.command()
async def init_check_schedule(context):
    channel = context.channel

    await channel.send("Verificações automaticas para a criação de threads iniciadas com sucesso!")
    await check_schedule(context)
