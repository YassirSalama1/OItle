import os
import random
import aiohttp
import discord
from discord.ext import commands

API_URL = 'https://dmoj.ca/api/v2/problems/'

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

async def fetch_random_problem():
    async with aiohttp.ClientSession() as session:
        # get total number of problems
        async with session.get(API_URL, params={'limit': 1}) as resp:
            data = await resp.json()
            total = data.get('meta', {}).get('total_count', 0)
            if total == 0:
                return 'Failed to fetch problems.'
        # choose a random offset
        offset = random.randint(0, total - 1)
        async with session.get(API_URL, params={'limit': 1, 'offset': offset}) as resp:
            data = await resp.json()
            objs = data.get('objects') or data.get('results')
            if not objs:
                return 'Failed to fetch problems.'
            prob = objs[0]
            code = prob.get('code') or prob.get('id')
            name = prob.get('name') or prob.get('title')
            if code and name:
                return f"{name} - https://dmoj.ca/problem/{code}"
            return 'Failed to parse problem.'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    try:
        await bot.tree.sync()
    except Exception as e:
        print(f'Failed to sync commands: {e}')

@bot.tree.command(name='gimme', description='Get a random OI problem from DMOJ')
async def gimme(interaction: discord.Interaction):
    await interaction.response.defer()
    text = await fetch_random_problem()
    await interaction.followup.send(text)

if __name__ == '__main__':
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        raise SystemExit('DISCORD_TOKEN environment variable not set')
    bot.run(token)
