
import asyncio
import json
from datetime import datetime

from ..commands.create_thread import create_thread
from ..variables import time_zone


async def check_schedule(context):
    now = datetime.now(time_zone)

    with open('schedule.json') as file:
        schedule_json = json.load(file)

    current_day = now.strftime('%A').lower()
    current_time = now.strftime('%H:%M')

    if current_day in schedule_json and current_time == schedule_json[current_day]:
        await create_thread(context, now.strftime("%d-%m-%Y"), '@everyone')

    await asyncio.sleep(60)
    await check_schedule(context)
