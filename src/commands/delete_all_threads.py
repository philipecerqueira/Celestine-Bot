import discord

from src.config.discord import celestine


@celestine.command()
async def delete_all_threads(context):
    guild = context.guild
    threads = guild.threads

    try:
        for thread in threads:
            await thread.delete()
        await context.send('All threads have been deleted successfully.')
    except:
        await context.send('An error occurred while trying to delete threads, check the log for more information')
