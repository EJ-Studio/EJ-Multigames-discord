
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


@client.command(pass_context=True, aliases=["Buy, BUY"])
async def buy(ctx, *, option = None):
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

	if option == None:
		update_embed = discord.Embed(
			colour=discord.Colour.gold(),
			title="System ALERT.",
			description=f"Please make sure to specify what you want to buy.\nFor a list of what you can buy, run this command `?buy list`.")
		await ctx.send(embed = update_embed)
		return

	if option == "list" or option == "List" or option == "LIST":
		update_embed = discord.Embed(
			colour=discord.Colour.green(),
			title="Buy list.",
			description=f"You can buy the following!")

		update_embed.add_field(name="Consumables", value="""
            Health potion | $20 Gold
            Food          | $10 Gold
            """, inline=False)

		update_embed.add_field(name="Repairs", value="""
            Wood  | $25  Gold
            Stone | $65  Gold
            Iron  | $100 Gold
            """, inline=False)

		update_embed.add_field(name="Tools", value="""
            Wooden sword | $50   Gold
            Stone sword  | $500  Gold
            Iron sword   | $1200 Gold
            """, inline=False)

		update_embed.set_footer(text=f"{FOOTER.footer}")
		sent = await ctx.send(embed = update_embed)
		await asyncio.sleep(30)
		await sent.delete()
		return


	update_embed = discord.Embed(
		colour=discord.Colour.green(),
		title="System.",
		description=f"We are fetching your save file <a:loading:768429190193086475>")
	info1 = await ctx.send(embed = update_embed)

	path = os.getcwd() + r'\commands\data\PROFILES'
	Save_New_User = os.path.join(path, f'{User}.py')

	logs_path = os.getcwd() + r"\packages\logs"
	system_log_path = os.path.join(logs_path, 'system_log.txt')
	log_path = os.path.join(logs_path, 'log.txt')
	error_log_path = os.path.join(logs_path, 'error_log.txt')

	file_path = rf"./commands/data/PROFILES/{User}.py"
	module_name = f'{User}'

	spec = importlib.util.spec_from_file_location(module_name, file_path)
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)

	await info1.delete()

	if option == "health potion" or option == "Health potion" or option == "HEALTH POTION":
		if module.gold >= 50:

			print(f"SYSTEM: Accessing {User}'s profile. | Adding a health potion.")

			f = open(Save_New_User, "w")
			f.write("join_date = '" + str(module.join_date) + "' \n")
			f.write("time_join = '" + str(module.time_join) + "' \n")
			f.write("name = '" + str(module.name) + "' \n")
			f.write("exp = " + str(module.exp) + "\n")
			f.write("next_level_up = " + str(module.next_level_up) + "\n")
			f.write("level = " + str(module.level) + "\n")
			f.write("health = " + str(module.health) + "\n")
			f.write("gold = " + str(module.gold - 50) + "\n")
			f.write("healthpotion = " + str(module.healthpotion + 1) + "\n")
			f.write("food = " + str(module.food) + "\n")
			f.write("wood = " + str(module.wood) + "\n")
			f.write("stone = " + str(module.stone) + "\n")
			f.write("iron = " + str(module.iron) + "\n")
			f.write("active_weapon = '" + str(module.active_weapon) + "'\n")
			f.write("wood_owned = " + str(module.wood_owned) + "\n")
			f.write("wood_durability = " + str(module.wood_durability) + "\n")
			f.write("wood_attack = " + str(module.wood_attack) + "\n")
			f.write("stone_owned = " + str(module.stone_owned) + "\n")
			f.write("stone_durability = " + str(module.stone_durability) + "\n")
			f.write("stone_attack = " + str(module.stone_attack) + "\n")
			f.write("iron_owned = " + str(module.iron_owned) + "\n")
			f.write("iron_durability = " + str(module.iron_durability) + "\n")
			f.write("iron_attack = " + str(module.iron_attack) + "\n")
			f.write("BAN = " + str(module.BAN) + "\n")
			f.close()

			print(f"SYSTEM: Finished write and closed connection.")

			pre_healthpotion = module.healthpotion
			pre_gold = module.gold

			spec = importlib.util.spec_from_file_location(module_name, file_path)
			module = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(module)

			print(f"SYSTEM: updating the log.")

			f = open(log_path, "a")
			now = date.today()
			date_now = now.strftime("%#d\%#m\%y")
			now1 = datetime.now()
			time_now = now1.strftime("%H:%M")
			f.write(str(f"Date: {date_now} | Time: {time_now} | User: {User}\n"))
			f.write(str(f"Bought a health potion.\n"))
			f.write(str(f"Previous health potion:  {pre_healthpotion}\n"))
			f.write(str(f"New health potion:       {module.healthpotion}\n"))
			f.write(str(f"Previous gold:           {pre_gold}\n"))
			f.write(str(f"New gold:                {module.gold}\n"))
			f.write(str(f"\n\n"))
			f.close()

			print(f"SYSTEM: Finished log update.\n")

			update_embed = discord.Embed(
				colour=discord.Colour.green(),
				title="Health potion purchased!",
				description=f"You have bought a health potion and own {module.healthpotion} health potions now.")
			info1 = await ctx.send(embed = update_embed)
			await asyncio.sleep(30)
			await info1.delete()
			return

		else:
			update_embed = discord.Embed(
				colour=discord.Colour.gold(),
				title="Sorry.",
				description=f"You do not have enough gold for a health potion\nYour gold: {module.gold} gold | Required: 50 gold.")
			sent = await ctx.send(embed = update_embed)
			await asyncio.sleep(10)
			await sent.delete()
			return


