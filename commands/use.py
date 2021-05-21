
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



@client.command(pass_context=True, aliases=["Use, USE"])
async def use(ctx, *, option = None):
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

	logs_path = os.getcwd() + r"\packages\logs"
	system_log_path = os.path.join(logs_path, 'system_log.txt')
	log_path = os.path.join(logs_path, 'log.txt')
	error_log_path = os.path.join(logs_path, 'error_log.txt')

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

	if option == "Health potion" or option == "health potion" or option == "HEALTH POTION":
		if module.healthpotion >= 1:
			if module.health <= 99:

				print(f"SYSTEM: Accessing {User}'s profile. | Using a health potion.")

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

				pre_health = module.health
				pre_healthpotion = module.healthpotion

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
				f.write(str(f"Used a health potion.\n"))
				f.write(str(f"Previous health:         {pre_health}%\n"))
				f.write(str(f"New health:              {module.health}%\n"))
				f.write(str(f"Previous health potions: {pre_healthpotion}\n"))
				f.write(str(f"New health potions       {module.healthpotion}\n"))
				f.write(str(f"\n\n"))
				f.close()

				print(f"SYSTEM: Finished log update.\n")


				update_embed = discord.Embed(
					colour=discord.Colour.green(),
					title="Used a health potion!",
					description=f"You have used a health potion and are at {module.health} health now.")
				info1 = await ctx.send(embed = update_embed)

				await asyncio.sleep(30)

				await info1.delete()

			elif module.health >= 100:
				update_embed = discord.Embed(
					colour=discord.Colour.gold(),
					title="Hmm",
					description=f"You are already above 99% health and can not heal yourself further.")
				info1 = await ctx.send(embed = update_embed)

				await asyncio.sleep(30)

				await info1.delete()

			else:
				update_embed = discord.Embed(
					colour=discord.Colour.red(),
					title="System ERROR",
					description=f"Sorry their is something wrong on our end.\n Please try again, if the problem persist please raise this issue.")
				info1 = await ctx.send(embed = update_embed)

				await asyncio.sleep(30)

				await info1.delete()

		elif module.healthpotion <= 0:
			update_embed = discord.Embed(
				colour=discord.Colour.gold(),
				title="Hmm",
				description=f"You don't seem to have any health potions right now...\n Why not buy some! using `?buy Health potion`")
			info1 = await ctx.send(embed = update_embed)

			await asyncio.sleep(30)

			await info1.delete()

		else:
			update_embed = discord.Embed(
				colour=discord.Colour.red(),
				title="System ERROR",
				description=f"Sorry their is something wrong on our end.\n Please try again, if the problem persist please raise this issue.")
			info1 = await ctx.send(embed = update_embed)

			await asyncio.sleep(30)

			await info1.delete()

	elif option == "food" or option == "Food" or option == "FOOD":
		if module.food >= 1:
			if module.health <= 90:

				print(f"SYSTEM: Accessing {User}'s profile. | Using Food.")

				f = open(Save_New_User, "w")
				f.write("join_date = '" + str(module.join_date) + "' \n")
				f.write("time_join = '" + str(module.time_join) + "' \n")
				f.write("name = '" + str(module.name) + "' \n")
				f.write("exp = " + str(module.exp) + "\n")
				f.write("next_level_up = " + str(module.next_level_up) + "\n")
				f.write("level = " + str(module.level) + "\n")
				f.write("health = " + str(module.health + 10) + "\n")
				f.write("gold = " + str(module.gold) + "\n")
				f.write("healthpotion = " + str(module.healthpotion) + "\n")
				f.write("food = " + str(module.food - 1) + "\n")
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

				pre_health = module.health
				pre_food = module.food

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
				f.write(str(f"Used food.\n"))
				f.write(str(f"Previous health: {pre_health}%\n"))
				f.write(str(f"New health:      {module.health}%\n"))
				f.write(str(f"Previous food:   {pre_food}\n"))
				f.write(str(f"New food:        {module.food}\n"))
				f.write(str(f"\n\n"))
				f.close()

				print(f"SYSTEM: Finished log update.\n")

				update_embed = discord.Embed(
					colour=discord.Colour.green(),
					title="Used food!",
					description=f"You have used a piece of food and are at {module.health} health now.")
				info1 = await ctx.send(embed = update_embed)

				await asyncio.sleep(30)

				await info1.delete()

			elif module.health >= 100:
				update_embed = discord.Embed(
					colour=discord.Colour.gold(),
					title="Hmm",
					description=f"You are already above 90% health and can not heal yourself further.")
				info1 = await ctx.send(embed = update_embed)

				await asyncio.sleep(30)

				await info1.delete()

			else:
				update_embed = discord.Embed(
					colour=discord.Colour.red(),
					title="System ERROR",
					description=f"Sorry their is something wrong on our end.\n Please try again, if the problem persist please raise this issue.")
				info1 = await ctx.send(embed = update_embed)

				await asyncio.sleep(30)

				await info1.delete()

		elif module.healthpotion <= 0:
			update_embed = discord.Embed(
				colour=discord.Colour.gold(),
				title="Hmm",
				description=f"You don't seem to have any food right now...\n Why not buy some! using `?buy Food`")
			info1 = await ctx.send(embed = update_embed)

			await asyncio.sleep(30)

			await info1.delete()

		else:
			update_embed = discord.Embed(
				colour=discord.Colour.red(),
				title="System ERROR",
				description=f"Sorry their is something wrong on our end.\n Please try again, if the problem persist please raise this issue.")
			info1 = await ctx.send(embed = update_embed)

			await asyncio.sleep(30)

			await info1.delete()

	elif option == "wood" or option == "Wood" or option == "WOOD":
		if module.wood_owned == True:
			if module.wood >= 1:
				if module.wood_durability <= 95:

					print(f"SYSTEM: Accessing {User}'s profile. | Using wood.")

					f = open(Save_New_User, "w")
					f.write("join_date = '" + str(module.join_date) + "' \n")
					f.write("time_join = '" + str(module.time_join) + "' \n")
					f.write("name = '" + str(module.name) + "' \n")
					f.write("exp = " + str(module.exp) + "\n")
					f.write("next_level_up = " + str(module.next_level_up) + "\n")
					f.write("level = " + str(module.level) + "\n")
					f.write("health = " + str(module.health) + "\n")
					f.write("gold = " + str(module.gold) + "\n")
					f.write("healthpotion = " + str(module.healthpotion) + "\n")
					f.write("food = " + str(module.food) + "\n")
					f.write("wood = " + str(module.wood - 1) + "\n")
					f.write("stone = " + str(module.stone) + "\n")
					f.write("iron = " + str(module.iron) + "\n")
					f.write("active_weapon = '" + str(module.active_weapon) + "'\n")
					f.write("wood_owned = " + str(module.wood_owned) + "\n")
					f.write("wood_durability = " + str(module.wood_durability + 5) + "\n")
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

					pre_wood_durability = module.wood_durability
					pre_wood = module.wood

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
					f.write(str(f"Used wood.\n"))
					f.write(str(f"Previous wood durability: {pre_wood_durability}%\n"))
					f.write(str(f"New wood durability:      {module.wood_durability}%\n"))
					f.write(str(f"Previous wood:            {pre_wood}\n"))
					f.write(str(f"New wood:                 {module.wood}\n"))
					f.write(str(f"\n\n"))
					f.close()

					print(f"SYSTEM: Finished log update.\n")

					update_embed = discord.Embed(
						colour=discord.Colour.green(),
						title="Used wood!",
						description=f"You have used wood to mend your wooden sword to {module.wood_durability}% durability now.")
					info1 = await ctx.send(embed = update_embed)

					await asyncio.sleep(30)

					await info1.delete()

				elif module.wood_durability >= 96:
					update_embed = discord.Embed(
						colour=discord.Colour.gold(),
						title="Hmm",
						description=f"You're wooden sword is already above 95% durability and can not be repaired further.")
					info1 = await ctx.send(embed = update_embed)

					await asyncio.sleep(30)

					await info1.delete()

				else:
					update_embed = discord.Embed(
						colour=discord.Colour.red(),
						title="System ERROR",
						description=f"Sorry their is something wrong on our end.\n Please try again, if the problem persist please raise this issue.")
					info1 = await ctx.send(embed = update_embed)

					await asyncio.sleep(30)

					await info1.delete()

			elif module.wood <= 0:
				update_embed = discord.Embed(
					colour=discord.Colour.gold(),
					title="Hmm",
					description=f"You don't seem to have any wood right now...\n Why not buy some! using `?buy Wood`")
				info1 = await ctx.send(embed = update_embed)

				await asyncio.sleep(30)

				await info1.delete()

			else:
				update_embed = discord.Embed(
					colour=discord.Colour.red(),
					title="System ERROR",
					description=f"Sorry their is something wrong on our end.\n Please try again, if the problem persist please raise this issue.")
				info1 = await ctx.send(embed = update_embed)

				await asyncio.sleep(30)

				await info1.delete()

		elif module.wood_owned == False:
			update_embed = discord.Embed(
				colour=discord.Colour.gold(),
				title="Hmm",
				description=f"You don't seem to own a wooden sword...\n Why not buy one! using `?buy Wooden sword`")
			info1 = await ctx.send(embed = update_embed)

			await asyncio.sleep(30)

			await info1.delete()

		else:
			update_embed = discord.Embed(
				colour=discord.Colour.red(),
				title="System ERROR",
				description=f"Sorry their is something wrong on our end.\n Please try again, if the problem persist please raise this issue.")
			info1 = await ctx.send(embed = update_embed)

			await asyncio.sleep(30)

			await info1.delete()


	elif option == "stone" or option == "Stone" or option == "STONE":
		if module.stone_owned == True:
			if module.stone >= 1:
				if module.stone_durability <= 95:

					print(f"SYSTEM: Accessing {User}'s profile. | Using stone.")

					f = open(Save_New_User, "w")
					f.write("join_date = '" + str(module.join_date) + "' \n")
					f.write("time_join = '" + str(module.time_join) + "' \n")
					f.write("name = '" + str(module.name) + "' \n")
					f.write("exp = " + str(module.exp) + "\n")
					f.write("next_level_up = " + str(module.next_level_up) + "\n")
					f.write("level = " + str(module.level) + "\n")
					f.write("health = " + str(module.health) + "\n")
					f.write("gold = " + str(module.gold) + "\n")
					f.write("healthpotion = " + str(module.healthpotion) + "\n")
					f.write("food = " + str(module.food) + "\n")
					f.write("wood = " + str(module.wood) + "\n")
					f.write("stone = " + str(module.stone - 1) + "\n")
					f.write("iron = " + str(module.iron) + "\n")
					f.write("active_weapon = '" + str(module.active_weapon) + "'\n")
					f.write("wood_owned = " + str(module.wood_owned) + "\n")
					f.write("wood_durability = " + str(module.wood_durability) + "\n")
					f.write("wood_attack = " + str(module.wood_attack) + "\n")
					f.write("stone_owned = " + str(module.stone_owned) + "\n")
					f.write("stone_durability = " + str(module.stone_durability + 5) + "\n")
					f.write("stone_attack = " + str(module.stone_attack) + "\n")
					f.write("iron_owned = " + str(module.iron_owned) + "\n")
					f.write("iron_durability = " + str(module.iron_durability) + "\n")
					f.write("iron_attack = " + str(module.iron_attack) + "\n")
					f.write("BAN = " + str(module.BAN) + "\n")
					f.close()

					print(f"SYSTEM: Finished write and closed connection.")

					pre_stone_durability = module.stone_durability
					pre_stone = module.stone

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
					f.write(str(f"Used stone.\n"))
					f.write(str(f"Previous stone durability: {pre_stone_durability}%\n"))
					f.write(str(f"New stone durability:      {module.stone_durability}%\n"))
					f.write(str(f"Previous stone:            {pre_stone}\n"))
					f.write(str(f"New stone:                 {module.stone}\n"))
					f.write(str(f"\n\n"))
					f.close()

					print(f"SYSTEM: Finished log update.\n")

					update_embed = discord.Embed(
						colour=discord.Colour.green(),
						title="Used stone!",
						description=f"You have used stone to mend your stone sword to {module.stone_durability + 5}% durability now.")
					info1 = await ctx.send(embed = update_embed)

					await asyncio.sleep(30)

					await info1.delete()

				elif module.stone_durability >= 96:
					update_embed = discord.Embed(
						colour=discord.Colour.gold(),
						title="Hmm",
						description=f"You're stone sword is already above 95% durability and can not be repaired further.")
					info1 = await ctx.send(embed = update_embed)

					await asyncio.sleep(30)

					await info1.delete()

				else:
					update_embed = discord.Embed(
						colour=discord.Colour.red(),
						title="System ERROR",
						description=f"Sorry their is something wrong on our end.\n Please try again, if the problem persist please raise this issue.")
					info1 = await ctx.send(embed = update_embed)

					await asyncio.sleep(30)

					await info1.delete()

			elif module.stone <= 0:
				update_embed = discord.Embed(
					colour=discord.Colour.gold(),
					title="Hmm",
					description=f"You don't seem to have any stone right now...\n Why not buy some! using `?buy Stone`")
				info1 = await ctx.send(embed = update_embed)

				await asyncio.sleep(30)

				await info1.delete()

			else:
				update_embed = discord.Embed(
					colour=discord.Colour.red(),
					title="System ERROR",
					description=f"Sorry their is something wrong on our end.\n Please try again, if the problem persist please raise this issue.")
				info1 = await ctx.send(embed = update_embed)

				await asyncio.sleep(30)

				await info1.delete()

		elif module.stone_owned == False:
			update_embed = discord.Embed(
				colour=discord.Colour.gold(),
				title="Hmm",
				description=f"You don't seem to own a stone sword...\n Why not buy one! using `?buy Stone sword`")
			info1 = await ctx.send(embed = update_embed)

			await asyncio.sleep(30)

			await info1.delete()

		else:
			update_embed = discord.Embed(
				colour=discord.Colour.red(),
				title="System ERROR",
				description=f"Sorry their is something wrong on our end.\n Please try again, if the problem persist please raise this issue.")
			info1 = await ctx.send(embed = update_embed)

			await asyncio.sleep(30)

			await info1.delete()


	elif option == "iron" or option == "Iron" or option == "IRON":
		if module.iron_owned == True:
			if module.iron >= 1:
				if module.iron_durability <= 95:

					print(f"SYSTEM: Accessing {User}'s profile. | Using iron.")

					f = open(Save_New_User, "w")
					f.write("join_date = '" + str(module.join_date) + "' \n")
					f.write("time_join = '" + str(module.time_join) + "' \n")
					f.write("name = '" + str(module.name) + "' \n")
					f.write("exp = " + str(module.exp) + "\n")
					f.write("next_level_up = " + str(module.next_level_up) + "\n")
					f.write("level = " + str(module.level) + "\n")
					f.write("health = " + str(module.health) + "\n")
					f.write("gold = " + str(module.gold) + "\n")
					f.write("healthpotion = " + str(module.healthpotion) + "\n")
					f.write("food = " + str(module.food) + "\n")
					f.write("wood = " + str(module.wood) + "\n")
					f.write("stone = " + str(module.stone) + "\n")
					f.write("iron = " + str(module.iron - 1) + "\n")
					f.write("active_weapon = '" + str(module.active_weapon) + "'\n")
					f.write("wood_owned = " + str(module.wood_owned) + "\n")
					f.write("wood_durability = " + str(module.wood_durability) + "\n")
					f.write("wood_attack = " + str(module.wood_attack) + "\n")
					f.write("stone_owned = " + str(module.stone_owned) + "\n")
					f.write("stone_durability = " + str(module.stone_durability) + "\n")
					f.write("stone_attack = " + str(module.stone_attack) + "\n")
					f.write("iron_owned = " + str(module.iron_owned) + "\n")
					f.write("iron_durability = " + str(module.iron_durability + 5) + "\n")
					f.write("iron_attack = " + str(module.iron_attack) + "\n")
					f.write("BAN = " + str(module.BAN) + "\n")
					f.close()

					print(f"SYSTEM: Finished write and closed connection.")

					pre_iron_durability = module.iron_durability
					pre_iron = module.iron

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
					f.write(str(f"Used iron.\n"))
					f.write(str(f"Previous iron durability: {pre_iron_durability}%\n"))
					f.write(str(f"New iron durability:      {module.iron_durability}%\n"))
					f.write(str(f"Previous iron:            {pre_iron}\n"))
					f.write(str(f"New iron:                 {module.iron}\n"))
					f.write(str(f"\n\n"))
					f.close()

					print(f"SYSTEM: Finished log update.\n")

					update_embed = discord.Embed(
						colour=discord.Colour.green(),
						title="Used iron!",
						description=f"You have used iron to mend your iron sword to {module.iron_durability + 5}% durability now.")
					info1 = await ctx.send(embed = update_embed)

					await asyncio.sleep(30)

					await info1.delete()

				elif module.iron_durability >= 96:
					update_embed = discord.Embed(
						colour=discord.Colour.gold(),
						title="Hmm",
						description=f"You're iron sword is already above 95% durability and can not be repaired further.")
					info1 = await ctx.send(embed = update_embed)

					await asyncio.sleep(30)

					await info1.delete()

				else:
					update_embed = discord.Embed(
						colour=discord.Colour.red(),
						title="System ERROR",
						description=f"Sorry their is something wrong on our end.\n Please try again, if the problem persist please raise this issue.")
					info1 = await ctx.send(embed = update_embed)

					await asyncio.sleep(30)

					await info1.delete()

			elif module.iron <= 0:
				update_embed = discord.Embed(
					colour=discord.Colour.gold(),
					title="Hmm",
					description=f"You don't seem to have any iron right now...\n Why not buy some! using `?buy Iron`")
				info1 = await ctx.send(embed = update_embed)

				await asyncio.sleep(30)

				await info1.delete()

			else:
				update_embed = discord.Embed(
					colour=discord.Colour.red(),
					title="System ERROR",
					description=f"Sorry their is something wrong on our end.\n Please try again, if the problem persist please raise this issue.")
				info1 = await ctx.send(embed = update_embed)

				await asyncio.sleep(30)

				await info1.delete()

		elif module.iron_owned == False:
			update_embed = discord.Embed(
				colour=discord.Colour.gold(),
				title="Hmm",
				description=f"You don't seem to own a iron sword...\n Why not buy one! using `?buy Iron sword`")
			info1 = await ctx.send(embed = update_embed)

			await asyncio.sleep(30)

			await info1.delete()

		else:
			update_embed = discord.Embed(
				colour=discord.Colour.red(),
				title="System ERROR",
				description=f"Sorry their is something wrong on our end.\n Please try again, if the problem persist please raise this issue.")
			info1 = await ctx.send(embed = update_embed)

			await asyncio.sleep(30)

			await info1.delete()

	else:
		update_embed = discord.Embed(
			colour=discord.Colour.gold(),
			title="System ALERT",
			description=f"The option: {option}, does not exist.\nPlease specify an item.")
		info1 = await ctx.send(embed = update_embed)

		await asyncio.sleep(30)

		await info1.delete()