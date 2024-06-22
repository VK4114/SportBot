import SportBot_logic
from SportBot_logic import SportBotLogic
import aiohttp
import discord
from bs4 import BeautifulSoup
import requests
import re
import os
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.all()
intents.messages = True
intents.guilds = True



load_dotenv()

token = os.getenv('DISCORD_TOKEN')




bot = commands.Bot(command_prefix= '##', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name ='GetNFLRoster')
async def GetNFLRoster(ctx, abv: str, team_name: str):
    roster = SportBotLogic.GetNFLRoster(abv, team_name)
    await send_long_message(ctx, roster)

@bot.command(name = "GetNBARoster")
async def GetNBARoster(ctx, abv: str, team_name: str):
    roster = SportBotLogic.GetNBARoster(abv, team_name)
    await send_long_message(ctx,roster)

@bot.command(name = "GetMLBRoster")
async def GetMLBRoster(ctx, abv: str, team_name: str):
    roster = SportBotLogic.GetMLBRoster(abv, team_name)
    await send_long_message(ctx,roster)

@bot.command(name = "GetNFLTeamStats")
async def GetNFLTeamStats(ctx, abv: str, year: str, seasonType: str):
    Team_stats = SportBotLogic.GetNFLTeamStats(abv, year, seasonType)
    await send_long_message(ctx, Team_stats)


@bot.command(name = "GetNFLPlayerStats")
async def GetNFLPlayerStats(ctx, abv: str, year: str, player_name: str, seasonType: str):
    player_stats = SportBotLogic.GetNFLPlayerStats(abv, year, player_name, seasonType)
    await ctx.send(player_stats)


@bot.command(name = "GetNBAPlayerStats")
async def GetNBAPlayerStats(ctx, abv: str, year: str, player_name: str, seasonType: str):
    player_stats = SportBotLogic.GetNBAPlayerStats(abv, year, player_name, seasonType)
    await ctx.send(player_stats)


@bot.command(name = "GetMLBPlayerStats")
async def GetMLBPlayerStats(ctx, abv: str, year: str, player_name: str, seasonType: str):
    player_stats = SportBotLogic.GetMLBPlayerStats(abv, year, player_name, seasonType)
    await ctx.send(player_stats)


async def send_long_message(ctx, message):
    max_length = 2000  # Discord's message character limit
    if len(message) > max_length:
        chunks = [message[i:i + max_length] for i in range(0, len(message), max_length)]
        for chunk in chunks:
            await ctx.send(chunk)
    else:
        await ctx.send(message)


if token:
    bot.run(token)
else:
    print("Bot token not found. Exiting...")