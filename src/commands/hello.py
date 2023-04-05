from src.config.discord import celestine


@celestine.command(name="hello")
async def hello(message):
    await message.channel.send(
        "Olá, você faz parte da turma? Caso não, venha fazer parte! :D"
    )
