
#Discord dependency's-----------------------------------------------------\
import discord
import asyncio

from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound


#EJ_Multigames_Discord dependency's---------------------------------------\
import packages
import packages.CRITICAL
import commands #Reloading the modules (>REFRESH) will not work without this imported...

from packages import SERVER_MAINTENENCE_TIME

from packages.CRITICAL.TOKEN import TOKEN
from packages.CRITICAL.CLIENT import client
from packages.CRITICAL.STATUS import EJ_M_STATUS
from commands.data import FOOTER, BOT_CHANNELS

from packages.CRITICAL.STATUS import EJ_M_STATUS
from packages.CRITICAL.TOKEN import TOKEN
from packages.CRITICAL.CLIENT import client
from packages.CRITICAL.VERSION import EJ_M_VERSION



#Module importing & Refreshing--------------------------------------------\
import importlib
from importlib import reload


#System threads & Management----------------------------------------------\
import threading
import multiprocessing
import subprocess
import sys
import os
from threading import Thread
from multiprocessing import Process
from sys import platform


#Specific file editing imports--------------------------------------------\
import shutil
from shutil import copyfile


#Time & Date dependency's-------------------------------------------------\
import time
from datetime import date
from datetime import datetime


#Other important modules--------------------------------------------------\
import random



@client.command(pass_context=True, aliases=["Weapon, WEAPON"])
async def weapon(ctx):
	await client.wait_until_ready()

	await ctx.message.delete()

	User = ctx.message.author

	if packages.CRITICAL.STATUS.EJ_M_STATUS == "IDLE" or packages.CRITICAL.STATUS.EJ_M_STATUS == "OFFLINE":
		update_embed = discord.Embed(
			colour=discord.Colour.gold(),
			title="System ALERT.",
			description=f"{User}, The server is down right now, please try again when the bot is fully online.\nThank you.")
		await ctx.send(embed = update_embed)
		return

	if os.path.isfile(rf'./commands/data/PROFILES/{User}.py'):
		pass

	else:
		update_embed = discord.Embed(
			colour=discord.Colour.gold(),
			title="System ALERT.",
			description=f"{User}, You will need an account to play EJ Multigames Discord.\n Please run the following command ?login")
		await ctx.send(embed = update_embed)
		return


	update_embed = discord.Embed(
		colour=discord.Colour.green(),
		title="System.",
		description=f"We are fetching your save file <a:loading:768429190193086475>")
	info1 = await ctx.send(embed = update_embed)


	file_path = rf"./commands/data/PROFILES/{User}.py"
	module_name = f'{User}'

	spec = importlib.util.spec_from_file_location(module_name, file_path)
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)

	author = ctx.message.author
	pfp = author.avatar_url

	update_embed = discord.Embed(
		colour=discord.Colour.green(),
		title=f"{User}'s weapons.",
		description=f"In use : `{module.active_weapon}`")

	update_embed.add_field(name="Owned swords:", value=f"""
		Wooden sword : `{module.wood_owned}`\n
		Stone sword : `{module.stone_owned}`\n
		Iron sword : `{module.iron_owned}`\n\n
		To switch to another weapon, type `?change` + the sword name.
		""")

	update_embed.set_author(name="", icon_url=(pfp))
	update_embed.set_thumbnail(url=(pfp))
	
	info2 = await ctx.send(embed = update_embed)


	await info1.delete()

	await asyncio.sleep(30)

	await info2.delete()