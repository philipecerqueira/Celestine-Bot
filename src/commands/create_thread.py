import json
from datetime import datetime, timedelta

from src.config.discord import celestine


@celestine.command()
async def create_thread(context):
    channel = context.channel
    now = datetime.now()

    with open('dates.json', 'r') as file:
        data = json.load(file)

    weekDays = ['monday', 'tuesday', 'wendnesday',
                'thursday', 'friday', 'saturday', 'sunday']

    for day, time in data.items():
        if day not in weekDays:
            await context.send(f'The week day "{day}" is invalid.')
            break

        validTime = ""
        try:
            validTime = datetime.strptime(time, '%H:%M').time()
        except ValueError:
            await context.send(f'The time "{time}" is invalid. Use the format HH:MM.')
            break

        desired_day = weekDays.index(day)
        delta_days = (desired_day - now.weekday()) % 7
        day_thread = now + timedelta(days=delta_days)
        date_time_thread = datetime.combine(day_thread.date(), validTime)

        if (date_time_thread.strftime("%Y-%m-%d %H:%M") == now.strftime("%Y-%m-%d %H:%M")):
            new_thread = await channel.create_thread(name=f'{date_time_thread.strftime("%d-%m-%Y")}')
            await new_thread.send('@everyone')
