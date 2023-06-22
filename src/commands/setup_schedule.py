
import os

from src.config.discord import celestine

from ..actions import create_json, update_json, verify_time
from ..events.check_schedule import check_schedule
from ..variables import day_names


@celestine.command()
async def setup_schedule(ctx, *args):
    if len(args) % 2 != 0:
        await ctx.send('Forneça um número par de argumentos. Cada par deve consistir em um nome de dia e uma hora. Ex.: Monday 12:34')
        return

    data = {}
    for i in range(0, len(args), 2):
        day = args[i].lower()
        time = args[i+1]

        if (day not in day_names):
            await ctx.send('Nome do dia inválido. Por favor, escolha um dos seguintes dias: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.')
            return

        if not (verify_time.verify_time(time)):
            await ctx.send('Formato de horário inválido. Certifique-se de fornecer o horário no formato H:M (hora:minuto).')
            return

        data[day] = time

    message = ""
    if os.path.exists('schedule.json'):
        message = update_json.update_json(data)
    else:
        message = create_json.create_json(data)

    await ctx.send(message)
