from src.config.discord import celestine


@celestine.command()
async def create_thread(context, thread_name="", message=""):
    channel = context.channel

    if thread_name == "":
        await channel.send("Por favor informe o nome da thread que deseja criar")
        return

    new_thread = await channel.create_thread(name=thread_name)

    if message != "":
        await new_thread.send(message)
