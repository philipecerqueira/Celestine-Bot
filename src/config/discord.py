import discord
from discord.ext import commands

intents = discord.Intents.all()
celestine = commands.Bot(intents=intents, command_prefix="!")
