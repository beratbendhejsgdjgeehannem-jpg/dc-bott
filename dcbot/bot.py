import discord
from discord.ext import commands
import os

# Botun ön eki
intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot giriş yaptı: {bot.user.name}')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Selam {ctx.author.mention}! Artık 7/24 aktifim.')

# Render üzerinden çalışması için güvenli yöntem
token = os.getenv('DISCORD_TOKEN')
bot.run(token)
