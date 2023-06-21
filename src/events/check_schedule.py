
import asyncio
import json
from datetime import datetime

from ..commands.create_thread import create_thread


async def check_schedule(context):
    now = datetime.now()

    with open('dates.json') as file:
        dates_json = json.load(file)

    current_day = now.strftime('%A').lower()
    current_time = now.strftime('%H:%M')

    if current_day in dates_json and current_time == dates_json[current_day]:
        await create_thread(context, now.strftime("%d-%m-%Y"), '@everyone')

    await asyncio.sleep(60)
    await check_schedule(context)
