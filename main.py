import discord
from discord.ext import commands
import discord.emoji


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.event
async def on_member_join(member):
     await message.channel.send(f'{member} suncuya hoş geldin!')

@bot.event
async def message_received(message: discord.Message):
    await message.add_reaction(":https://cdn.discordapp.com/emojis/1133805723051102218.webp?size=96&quality=lossless")

@bot.event 
async def on_message_delete(message):
    print(f'{message.author} : {message.content} : {message.created_at}')

 
