
import os

from src.config.discord import celestine

from ..actions import create_json, update_json, verify_time
from ..events.check_schedule import check_schedule
from ..variables import day_names


@celestine.command()
async def setup_schedule(ctx, *args):
    """
    Creates/Updates one of the days and times provided for thread creation.

    Ex.: !setup_schedule monday 12:00 tuesday 13:00
    """

    if len(args) % 2 != 0:
        await ctx.send('Insert an even number of arguments. Each pair must consist of a day name and a time. E.g.: Monday 12:34')
        return

    data = {}
    for i in range(0, len(args), 2):
        day = args[i].lower()
        time = args[i+1]

        if (day not in day_names):
            await ctx.send('Invalid day name. Please choose one of the following days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.')
            return

        if not (verify_time.verify_time(time)):
            await ctx.send('Invalid time format. Be sure to provide the time in H:M (hour:minute) format.')
            return

        data[day] = time

    message = ""
    if os.path.exists('schedule.json'):
        message = update_json.update_json(data)
    else:
        message = create_json.create_json(data)

    await ctx.send(message)
