
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


@client.command(pass_context=True, aliases=["Server", "SERVER"])
async def server(ctx):
	await ctx.message.delete()
	if ctx.channel.name in BOT_CHANNELS.channels:

		update_embed = discord.Embed(
			colour=discord.Colour.green(),
			title="",
			description=f"Loading please wait <a:loading:768429190193086475>")
		sent = await ctx.send(embed = update_embed)

		if platform == "linux" or platform == "linux2":
			system2 = "Linux"
		elif platform == "darwin":
			system2 = "Linux"
		elif platform == "win32":
			system2 = "Windows"

		path = os.getcwd() + r'\commands\data\PROFILES'
		list = os.listdir(path) # dir is your directory path
		players = len(list)


		pfp = client.user.avatar_url

		update_embed = discord.Embed(
			colour=discord.Colour.green(),
			title="SERVER",
			description=f"EJ Multigames Discord V{EJ_M_VERSION}")
		update_embed.set_author(name="EJ DJ", icon_url=(pfp))
		update_embed.set_thumbnail(url=(pfp))

		update_embed.add_field(name="SERVER:", value=f"""
			-System: {system2}\n
			-Players: {players}\n
			-Servers: {len(client.guilds)}\n
			-Watching: {len(client.users)} members
			""", inline=True)

		reload(packages.CRITICAL.STATUS)
		EJ_M_STATUS = packages.CRITICAL.STATUS.EJ_M_STATUS

		if EJ_M_STATUS == "ONLINE":
			ono = client.get_emoji(782527423669469184)
			msg1 = "Online"
		elif EJ_M_STATUS == "IDLE":
			ono = client.get_emoji(782540894988795904)
			msg1 = "Under maintenance"
		else:
			ono = client.get_emoji(782527932907651113)
			msg1 = "Critical error"

		pong = (round(client.latency * 1000))

		if pong >= 500:
			ping = pong
			msg2 = "Sorry we are experiencing delays"
		elif pong >= 300:
			ping = pong
			msg2 = "Speeds are slow"
		else:
			ping = pong
			msg2 = "Speeds are fast"
		pass

		update_embed.add_field(name="BOT:", value=f"""
			-Status: {ono} | {msg1}\n
			-Ping: {ping} | {msg2}\n
			""", inline=True)
		update_embed.set_footer(text=f"{FOOTER.footer}")

		await sent.delete()
		sent = await ctx.send(embed = update_embed)
		await asyncio.sleep(30)
		await sent.delete()