
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


@client.command(pass_context=True, aliases=["Profile, PROFILE"])
async def profile(ctx):
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

	path = os.getcwd() + r'\commands\data\PROFILES'

	Save_New_User = os.path.join(path, f'{User}.py')

	if os.path.isfile(rf'./commands/data/PROFILES/{User}.py'):
		pass

	else:
		update_embed = discord.Embed(
			colour=discord.Colour.gold(),
			title="System ALERT.",
			description=f"{User}, You will need an account to play EJ Multigames Discord.\n Please run the following command `?login`")
		await ctx.send(embed = update_embed)
		return

	'''
	Make the view profile command only show the below.
	- The players current level.
	- The amount of exp needed to level up.
	- The current exp the player has.
	- The current amount of health the player has.
	- The current amount of gold the player has.
	- The current weapon in use.
	'''

	file_path = rf"./commands/data/PROFILES/{User}.py"
	module_name = f'{User}'

	spec = importlib.util.spec_from_file_location(module_name, file_path)
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)

	author = ctx.message.author
	pfp = author.avatar_url


	EXP_LEVELUP = module.next_level_up - module.exp

	update_embed = discord.Embed(
		colour=discord.Colour.green(),
		title=f"{User}'s profile.",
		description=f"")

	update_embed.set_author(name="", icon_url=(pfp))
	update_embed.set_thumbnail(url=(pfp))

	update_embed.add_field(name="Player:", 
		value=f"""
		Account created: {module.join_date} at {module.time_join}
		Level: `{module.level}` | Exp: `{module.exp}` | `{EXP_LEVELUP}` exp until next level
		""", inline=False)

	update_embed.add_field(name="Resources:", value=f"""
		Health: `{module.health}`
		Gold: `{module.gold}`
		Active weapon: `{module.active_weapon}`
		""",
		inline=False)

	info1 = await ctx.send(embed = update_embed)

	await asyncio.sleep(30)

	await info1.delete()



	# if ctx.channel.name in BOT_CHANNELS.channels:
 #        pfp = client.user.avatar_url

 #        Help_embed = discord.Embed(
 #            colour=discord.Colour.green(),
 #            title="EJ Multigames commands..",
 #            description=f"EJ Multigames V{EJ_M_VERSION}")

 #        Help_embed.set_author(name="EJ DJ", icon_url=(pfp))
 #        Help_embed.set_thumbnail(url=(pfp))

 #        Help_embed.add_field(name=">help", value="Returns this command.", inline=True)
 #        Help_embed.add_field(name=">login", value="Every person will need to do this in order to play EJ Multigames.", inline=True)

 #        Help_embed.add_field(name="\u200b", value="\u200b")

 #        Help_embed.add_field(name=">pause", value="Pauses current playing music.", inline=True)
 #        Help_embed.add_field(name=">resume", value="Resumes the music.", inline=True)

 #        Help_embed.add_field(name="\u200b", value="\u200b")

 #        Help_embed.add_field(name=">join", value="Makes the bot join your current voice channel.", inline=True)
 #        Help_embed.add_field(name=">leave", value="Makes the bot leave your current voice channel.", inline=True)

 #        Help_embed.add_field(name="\u200b", value="\u200b")

 #        #Help_embed.add_field(name="\u200b", value="\u200b")

 #        Help_embed.add_field(name=">stop", value="Makes the music stop.", inline=True)
 #        Help_embed.add_field(name=">skip", value="Skipes to the next song in your queue.", inline=True)

 #        Help_embed.add_field(name="\u200b", value="\u200b")

 #        Help_embed.add_field(name=">update", value="See the lattest added fetures on EJ DJ!", inline=True)
 #        Help_embed.add_field(name=">info", value="See general information about the bot.", inline=True)

 #        Help_embed.add_field(name="\u200b", value="\u200b")

 #        Help_embed.add_field(name=">radio", value="Puts all of the bots downloaded songs on a random playlist!", inline=True)
 #        Help_embed.add_field(name="stop radio", value="Stops the radio from playing.", inline=True)

 #        Help_embed.add_field(name="\u200b", value="\u200b")

 #        Help_embed.add_field(name=">playlist", value="Plays your liked songs!", inline=True)
 #        Help_embed.add_field(name="stop playlist", value="Stops your playlist from playing.", inline=True)

 #        Help_embed.add_field(name="\u200b", value="\u200b")

 #        Help_embed.add_field(name=">server", value="See everything the bot is up too and stats.", inline=True)

 #        Help_embed.add_field(name="\u200b", value="\u200b")

 #        Help_embed.set_footer(text=f"{FOOTER.footer}")

 #        await ctx.send(embed = Help_embed)
