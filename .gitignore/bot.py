import discord # sensebot by Joshek
import asyncio # this bot is a proof of concept and shouldn't be used as a proper bot under any circumstances
from discord.ext import commands # if you do, thats dumb
from discord.ext.commands import Bot # anyway, enjoy the crappy code
from discord.utils import find
from sense_hat import SenseHat
from random import randint
from time import sleep

print("SenseBot is loading")
bot = commands.Bot(command_prefix='./', description="A proof of concept bot by Joshek. Merges discord.py with the Raspberry Pi Sense HAT.")
sense = SenseHat()

@bot.event
aysnc def on_ready():
    print("Done")
    await bot.change_presence(game=discord.Game(name="sensehat pixels flash", type=3))

@bot.command(pass_context=True)
async def about(ctx):
    await bot.say("This is a bot that will control the Raspberry Pi's Sense HAT. Written in python for native execution.")

@bot.command(pass_context=True)
async def flash(ctx):
    x = randint(0, 7)
    y = randint(0, 7)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    sense.set_pixel(x, y, r, g, b)
    sleep(0.01)

bot.run("")
