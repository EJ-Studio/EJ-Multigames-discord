
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



@client.command(pass_context=True, aliases=["Change, CHANGE"])
async def change(ctx, *, new_weapon = None):
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
			description=f"{User}, You will need an account to play EJ Multigames Discord.\n Please run the following command `?login`")
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

	await info1.delete()

	author = ctx.message.author
	pfp = author.avatar_url

	path = os.getcwd() + r'\commands\data\PROFILES'
	Save_New_User = os.path.join(path, f'{User}.py')

	logs_path = os.getcwd() + r"\packages\logs"
	system_log_path = os.path.join(logs_path, 'system_log.txt')
	log_path = os.path.join(logs_path, 'log.txt')
	error_log_path = os.path.join(logs_path, 'error_log.txt')


	if new_weapon == None:
		update_embed = discord.Embed(
			colour=discord.Colour.gold(),
			title="System ALERT",
			description=f"Please specify a sword to switch to.")
		info1 = await ctx.send(embed = update_embed)

		await asyncio.sleep(30)

		await info1.delete()

	else:
		if new_weapon == "wooden sword" or new_weapon == "Wooden sword" or new_weapon == "WOODEN SWORD":
			if module.active_weapon != "WOODEN_SWORD":
				if module.wood_owned == True:

					print(f"SYSTEM: Accessing {User}'s profile. | Changing {module.active_weapon} to WOODEN_SWORD")

					f = open(Save_New_User, "w")
					f.write("join_date = '" + str(module.join_date) + "' \n")
					f.write("time_join = '" + str(module.time_join) + "' \n")
					f.write("name = '" + str(module.name) + "' \n")
					f.write("exp = " + str(module.exp) + "\n")
					f.write("next_level_up = " + str(module.next_level_up) + "\n")
					f.write("level = " + str(module.level) + "\n")
					f.write("health = 100\n")
					f.write("gold = " + str(module.gold) + "\n")
					f.write("healthpotion = " + str(module.healthpotion - 1) + "\n")
					f.write("food = " + str(module.food) + "\n")
					f.write("wood = " + str(module.wood) + "\n")
					f.write("stone = " + str(module.stone) + "\n")
					f.write("iron = " + str(module.iron) + "\n")
					f.write("active_weapon = 'WOODEN_SWORD'\n")
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

					print(f"SYSTEM: updating the log.")

					f = open(log_path, "a")
					now = date.today()
					date_now = now.strftime("%#d\%#m\%y")
					now1 = datetime.now()
					time_now = now1.strftime("%H:%M")
					f.write(str(f"Date: {date_now} | Time: {time_now} | User: {User}\n"))
					f.write(str(f"Changed from {module.active_weapon} to WOODEN_SWORD.\n"))
					f.write(str(f"\n\n"))
					f.close()

					print(f"SYSTEM: Finished log update.\n")


					update_embed = discord.Embed(
						colour=discord.Colour.green(),
						title="Switched!",
						description=f"You switched your sword from {module.active_weapon} to a wooden sword.\n")
					info1 = await ctx.send(embed = update_embed)

					await asyncio.sleep(30)

					await info1.delete()

				else:
					update_embed = discord.Embed(
						colour=discord.Colour.gold(),
						title="System Alert",
						description=f"You do not own a wooden sword.\nType `?buy wooden sword` to purchase one.")
					info1 = await ctx.send(embed = update_embed)

					await asyncio.sleep(30)

					await info1.delete()

			else:
				update_embed = discord.Embed(
					colour=discord.Colour.gold(),
					title="System Alert",
					description=f"Wooden sword is already equiped.")
				info1 = await ctx.send(embed = update_embed)

				await asyncio.sleep(30)

				await info1.delete()

		elif new_weapon == "stone sword" or new_weapon == "Stone sword" or new_weapon == "STONE SWORD":
			if module.active_weapon != "STONE_SWORD":
				if module.stone_owned == True:

					print(f"SYSTEM: Accessing {User}'s profile. | Changing {module.active_weapon} to STONE_SWORD")

					f = open(Save_New_User, "w")
					f.write("join_date = '" + str(module.join_date) + "' \n")
					f.write("time_join = '" + str(module.time_join) + "' \n")
					f.write("name = '" + str(module.name) + "' \n")
					f.write("exp = " + str(module.exp) + "\n")
					f.write("next_level_up = " + str(module.next_level_up) + "\n")
					f.write("level = " + str(module.level) + "\n")
					f.write("health = 100\n")
					f.write("gold = " + str(module.gold) + "\n")
					f.write("healthpotion = " + str(module.healthpotion - 1) + "\n")
					f.write("food = " + str(module.food) + "\n")
					f.write("wood = " + str(module.wood) + "\n")
					f.write("stone = " + str(module.stone) + "\n")
					f.write("iron = " + str(module.iron) + "\n")
					f.write("active_weapon = 'STONE_SWORD'\n")
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

					print(f"SYSTEM: updating the log.")

					f = open(log_path, "a")
					now = date.today()
					date_now = now.strftime("%#d\%#m\%y")
					now1 = datetime.now()
					time_now = now1.strftime("%H:%M")
					f.write(str(f"Date: {date_now} | Time: {time_now} | User: {User}\n"))
					f.write(str(f"Changed from {module.active_weapon} to STONE_SWORD.\n"))
					f.write(str(f"\n\n"))
					f.close()

					print(f"SYSTEM: Finished log update.\n")


					update_embed = discord.Embed(
						colour=discord.Colour.green(),
						title="Switched!",
						description=f"You switched your sword from {module.active_weapon} to a stone sword.\n")
					info1 = await ctx.send(embed = update_embed)

					await asyncio.sleep(30)

					await info1.delete()

				else:
					update_embed = discord.Embed(
						colour=discord.Colour.gold(),
						title="System Alert",
						description=f"You do not own a stone sword.\nType `?buy stone sword` to purchase one.")
					info1 = await ctx.send(embed = update_embed)

					await asyncio.sleep(30)

					await info1.delete()

			else:
				update_embed = discord.Embed(
					colour=discord.Colour.gold(),
					title="System Alert",
					description=f"Stone sword is already equiped.")
				info1 = await ctx.send(embed = update_embed)

				await asyncio.sleep(30)

				await info1.delete()

		elif new_weapon == "iron sword" or new_weapon == "Iron sword" or new_weapon == "IRON SWORD":
			if module.active_weapon != "IRON_SWORD":
				if module.iron_owned == True:

					print(f"SYSTEM: Accessing {User}'s profile. | Changing {module.active_weapon} to IRON_SWORD")

					f = open(Save_New_User, "w")
					f.write("join_date = '" + str(module.join_date) + "' \n")
					f.write("time_join = '" + str(module.time_join) + "' \n")
					f.write("name = '" + str(module.name) + "' \n")
					f.write("exp = " + str(module.exp) + "\n")
					f.write("next_level_up = " + str(module.next_level_up) + "\n")
					f.write("level = " + str(module.level) + "\n")
					f.write("health = 100\n")
					f.write("gold = " + str(module.gold) + "\n")
					f.write("healthpotion = " + str(module.healthpotion - 1) + "\n")
					f.write("food = " + str(module.food) + "\n")
					f.write("wood = " + str(module.wood) + "\n")
					f.write("stone = " + str(module.stone) + "\n")
					f.write("iron = " + str(module.iron) + "\n")
					f.write("active_weapon = 'IRON_SWORD'\n")
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

					print(f"SYSTEM: Finished write and closed connection.\n")

					print(f"SYSTEM: updating the log.")

					f = open(log_path, "a")
					now = date.today()
					date_now = now.strftime("%#d\%#m\%y")
					now1 = datetime.now()
					time_now = now1.strftime("%H:%M")
					f.write(str(f"Date: {date_now} | Time: {time_now} | User: {User}\n"))
					f.write(str(f"Changed from {module.active_weapon} to IRON_SWORD.\n"))
					f.write(str(f"\n\n"))
					f.close()

					print(f"SYSTEM: Finished log update.\n")


					update_embed = discord.Embed(
						colour=discord.Colour.green(),
						title="Switched!",
						description=f"You switched your sword from {module.active_weapon} to a iron sword.\n")
					info1 = await ctx.send(embed = update_embed)

					await asyncio.sleep(30)

					await info1.delete()

				else:
					update_embed = discord.Embed(
						colour=discord.Colour.gold(),
						title="System Alert",
						description=f"You do not own a iron sword.\nType `?buy iron sword` to purchase one.")
					info1 = await ctx.send(embed = update_embed)

					await asyncio.sleep(30)

					await info1.delete()

				

			else:
				update_embed = discord.Embed(
					colour=discord.Colour.gold(),
					title="System Alert",
					description=f"Iron sword is already equiped.")
				info1 = await ctx.send(embed = update_embed)

				await asyncio.sleep(30)

				await info1.delete()









		else:
			update_embed = discord.Embed(
				colour=discord.Colour.gold(),
				title="System Alert",
				description=f"`{new_weapon}` is not a valid weapon.\nTo view weapons, type `?weapon`")
			info1 = await ctx.send(embed = update_embed)

			await asyncio.sleep(30)

			await info1.delete()




