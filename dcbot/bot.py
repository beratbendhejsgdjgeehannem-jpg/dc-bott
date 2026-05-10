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
token = os.getenv('MTQ4MjY2NTUzMDA5MDU4NjE5Mg.GU2tj5.0P00WydvmD852Na4Pk-AWGVcnV5a18hx6FOkdc')
bot.run(token)
