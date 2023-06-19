import discord

from src.config.discord import celestine


@celestine.command()
async def delete_all_threads(context):
    guild = context.guild
    threads = guild.threads

    try:
        for thread in threads:
            await thread.delete()
        await context.send('Todas as threads foram apagadas com sucesso.')
    except:
        await context.send('Ocorreu um erro ao tentar apagar as threads, verifique o log para mais informações')
