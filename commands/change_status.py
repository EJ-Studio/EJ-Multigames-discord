
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

#import ptdraft
#sys.path.append('../packages.CRITICAL.STATUS')

@client.command(pass_context=True, aliases=["Status", "STATUS"])
async def status(ctx, option = None):
	await client.wait_until_ready()

	await ctx.message.delete()
	User = ctx.message.author

	logs_path = os.getcwd() + r"\packages\logs"
	system_log_path = os.path.join(logs_path, 'system_log.txt')
	log_path = os.path.join(logs_path, 'log.txt')
	error_log_path = os.path.join(logs_path, 'error_log.txt')

	if option == None:
		update_embed = discord.Embed(
			colour=discord.Colour.gold(),
			title="System ALERT",
			description=f"Please specify a state for the bot.\nFor example ?state `online`")
		info1 = await ctx.send(embed = update_embed)
		await asyncio.sleep(30)
		await info1.delete()
		return

	if ctx.channel.name in BOT_CHANNELS.channels:
		from packages.CRITICAL.STATUS import EJ_M_STATUS
		EJ_M_STATUS = EJ_M_STATUS

		if EJ_M_STATUS == option.upper():
			update_embed = discord.Embed(
				colour=discord.Colour.gold(),
				title="System Alert",
				description=f"{option} is already in effect.")
			sent = await ctx.send(embed = update_embed)
			await asyncio.sleep(5)
			await sent.delete()
			return

		if option == "online" or option == "idle" or option == "offline":
			if option.upper() == "OFFLINE":
				print("SYSTEM: Switched to offline mode.")

			elif option.upper() == "ONLINE":
				print("SYSTEM: Switched to online mode.")

			path = r'./packages/CRITICAL/'
			savesave = os.path.join(path, 'STATUS.py')
			f = open(savesave, "w")
			f.write("EJ_M_STATUS = '" + str(option.upper()) + "'")                         #player name save.
			f.close()

			update_embed = discord.Embed(
				colour=discord.Colour.green(),
				title="",
				description=f"Done!")
			sent = await ctx.send(embed = update_embed)
			await asyncio.sleep(30)
			await sent.delete()
			return

		else:
			update_embed = discord.Embed(
				colour=discord.Colour.gold(),
				title="SYSTEM Alert",
				description=f"Please specify an actual state and make sure spelling is correct.")
			sent = await ctx.send(embed = update_embed)
			await asyncio.sleep(30)
			await sent.delete()
			return
# EJ_DJ_STATUS = "ONLINE"