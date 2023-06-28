from src.config.discord import celestine


@celestine.command()
async def create_thread(context, thread_name="", message=""):
    """
    Creates a new thread with the specified name and message if want

    Ex.: !create_thread thread_name message
    """

    channel = context.channel

    if thread_name == "":
        await channel.send("Please enter the name of the thread you want to create")
        return

    new_thread = await channel.create_thread(name=thread_name)

    if message != "":
        await new_thread.send(message)
