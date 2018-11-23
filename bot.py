# Created By DK#0001
# For CRH Only


# Imports
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
from discord import Game
from discord.utils import *
import random

bot = commands.Bot(command_prefix='*') #prefix


@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="CRH Discord Server Info", color=0xFF0000)
    embed.set_author(name="CRH")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed) #SERVERINFO

@bot.command(pass_context=True)
async def website(ctx):
    await bot.say("http://coderedhosting.bubbleapps.io/")# WEBSITE

@bot.command(pass_context=True)
async def op(ctx):
    await bot.say("https://docs.google.com/document/d/1sEVYcLmnHdpIIEHzR7yT7Xz5-JvLdstkWmuhAc2U0vc")# OP


@bot.command(pass_context=True)
async def share(ctx):
    await bot.say("Code Red Hosting")
    await bot.say("Join Code Red Hosting Today to satisfy all of your hosting needs. We try to meet all needs when requested and usually break our backs to do so.Our usual time frame for delivering a product takes between 4 to 15 minutes so its quick. Other products that are requested as custom may take longer but are normally delivered in a day depending on the amount of customization.")
    await bot.say("We offer multiple different products. CAD/MDTS,Logos,Bots,Intros,Outros,Overlays,and more all of our products can be found on our website.All product listed above or")
    await bot.say("website can come in different versions or different designs.If you are interested in seeing what Code Red Hosting has to offer just click the discord link below and all info will be given in the welcome message. We make getting your product as quick and simple as it has to be.")
    await bot.say("Website : http://coderedhosting-website.bubbleapps.io/")
    await bot.say("Discord : https://discord.gg/fdmQm9M") # SHARE

@bot.command(pass_context=True)
async def tos(ctx):
    await bot.say("https://docs.google.com/document/d/10Gmyo_FdxxqmYa2Xq3SlT89BANMj88nHgEWL02Vz5Bc/edit?usp=sharing")# TOS

@bot.command(pass_context=True)
async def privacy(ctx):
    await bot.say("https://docs.google.com/document/d/1AJhTA6psFW3S5L67SOJzZLS0eKfqkel0-iG5KgJ0rVw/edit?usp=sharing")#PRIVACY

@bot.command(pass_context=True)
async def bothelp(ctx):
    await bot.say(" List Of Commands You Can Use, Make Sure to Use the Prefix *")
    await bot.say("bothelp , share , tos , privacy , website , serverinfo")
    print("help") # HELP

@bot.command(pass_context=True)
async def pay(ctx):
    await bot.say("Paypal :  https://www.paypal.me/coderedhosting")
    await bot.say("Cash App:  https://cash.me/app/MVLWCTS")
    await bot.say("Venmo : https://venmo.com/code?user_id=2618050775875584688") # PAY

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)# INFO

@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name='*bothelp | Version 1.0.0'))#PRESENCE

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, userName: discord.User):
    await bot.ban(userName)
    print("User has been banned")# KICK

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, userName: discord.User):
    await bot.kick(userName)
    print("User has been kicked")# BAN

@bot.command(pass_context=True)
async def dice(con,min1=1,max1=6):
    await bot.say("**{}**".format(random.randint(min1,max1))) #I PUT IT THIS WAY TO MAKE IT BOLD IN DISCORD

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await bot.delete_messages(messages)





bot.run ("NTE1MzA3MjM5MTQ2NTIwNTc3.DtjNAQ.ilOjOM5zHUOrHDo8Y2b_x6YD398") # CRH Bot Run


