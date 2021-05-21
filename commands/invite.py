import discord, os, importlib, sys, subprocess, asyncio, re, random, time, packages

from discord.ext import commands
from discord.utils import get

from importlib import reload
from os import system
from shutil import copyfile
from sys import platform

import urllib.request
import packages.CRITICAL

from commands.data import FOOTER, BOT_CHANNELS

from packages.CRITICAL.STATUS import EJ_M_STATUS
from packages.CRITICAL.TOKEN import TOKEN
from packages.CRITICAL.CLIENT import client
from packages.CRITICAL.VERSION import EJ_M_VERSION


@client.command(pass_context=True, aliases=["Invite, INVITE"])
async def invite(ctx):
	await client.wait_until_ready()

	User = ctx.message.author

	info = await ctx.send("Invite Bot: https://discord.com/api/oauth2/authorize?client_id=833215082007756850&permissions=8&scope=bot\nJoin Server: https://discord.io/EJ-Studios\nVisit Website: https://ejmultigames.github.io/")
	
	await asyncio.sleep(30)

	await info.delete()