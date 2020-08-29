import discord
from math_logic import factoriser
import os
import mendeleev
from discord.ext import commands
from webserver import keep_alive
from chem_logic import emprical_formula, formula_mass, formula_mass_advanced
client = commands.Bot(command_prefix='fish ')
@client.event
async def on_ready():
  print('Bot is ready.')
@client.command()
async def hello(ctx):
  await ctx.send('Hi')
@client.command()
async def say(ctx, arg1):
  await ctx.send(arg1)
@client.command()
async def count(ctx, *args):
  await ctx.send('You typed {} words'.format(len(args)))
@client.command()
async def whatup(ctx):
  await ctx.send('bhalo')
@client.command()
async def eatfish(ctx):
  await ctx.send('NO')
@client.command()
async def slap(ctx, person, *reason):
  await ctx.send('{}, you got slapped by a fish on the command of {} {}.'.format(person, ctx.author, ' '.join(reason)))
@client.command()
async def hi(ctx):
  await ctx.send('Hello')
@client.command()
async def chem(ctx, arg1, arg2, arg3=None):
  if arg1 == 'name':
    await ctx.send(mendeleev.element(arg2).name)
  elif arg1 == 'ram':
    await ctx.send(round(mendeleev.element(arg2).atomic_weight))
  elif arg1 == 'number':
    await ctx.send(mendeleev.element(arg2).atomic_number)
  elif arg1 == 'emprical_formula':
    await ctx.send(emprical_formula(arg2.split(','), arg3.split(',')))
  elif arg1 == 'rfm':
    await ctx.send(formula_mass(arg2))
  elif arg1 == 'rfm_advanced':
    await ctx.send(formula_mass_advanced(arg2, arg3))
@client.command()
async def math(ctx, arg1, arg2):
  if arg1 == 'factorise':
    await ctx.send(factoriser(arg2))
keep_alive()
BOT_TOKEN = os.environ.get('DISCORD_BOT_SECRET')
client.run(BOT_TOKEN)
