from discord.ext import commands
import discord
from bs4 import BeautifulSoup
import requests
import tokens


COMMAND_PREFIX = '~'


bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=discord.Intents.all())


def get_poem(url: 'string') -> 'poem':
    url = url
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    new_soup = soup.find('pre')
    poem = new_soup.text.strip()
    if len(poem) < 2000:
        return poem
    else:
        return str('to long for discord')


def get_writer(url: 'string') -> 'writer':
    url = url
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    new_soup = soup.find('div', class_ = 'byline')
    writer = new_soup.text.strip()
    return writer[11:]


@bot.event
async def on_ready():
    print("i am ready to share poems!")


@bot.command()
async def poem(ctx):
    await ctx.send(get_writer('https://www.poetrysoup.com/famous/poems/random_famous_poem.aspx'))
    await ctx.send('--------------------')
    await ctx.send(get_poem('https://www.poetrysoup.com/famous/poems/random_famous_poem.aspx'))



bot.run(tokens.BOT_TOKEN)
