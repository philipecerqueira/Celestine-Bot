import json

from src.config.discord import celestine

from ..actions.show_json import show_json


@celestine.command()
async def show_schedule(ctx):
    data = show_json()
    if isinstance(data, dict):
        await ctx.send(f'Here is your schedule:\n```\n{json.dumps(data, indent=4)}\n```')
    else:
        await ctx.send(data)
