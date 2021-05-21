







#> EJ Studios_<
#> EJ Multigames Discord made by EJ Studios#3379 for EJ Studios and future servers.
#
#> This software is free to use and distribute.



























print("System Importing | Discord dependency's")
#Discord dependency's-----------------------------------------------------\
import discord
import asyncio

from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound

print("System Importing | EJ_Multigames_Discord dependency's")
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

from commands import inventory, profile, use, change_status, invite, weapon, change, server, info, buy


print("System Importing | Module importing & Refreshing")
#Module importing & Refreshing--------------------------------------------\
import importlib
from importlib import reload

print("System Importing | System threads & Management")
#System threads & Management----------------------------------------------\
import threading
import multiprocessing
import subprocess
import sys
import os
from threading import Thread
from multiprocessing import Process
from sys import platform

print("System Importing | Specific file editing imports")
#Specific file editing imports--------------------------------------------\
import shutil
from shutil import copyfile

print("System Importing | Time & Date dependency's")
#Time & Date dependency's-------------------------------------------------\
import time
from datetime import date
from datetime import datetime

print("System Importing | Other important modules")
#Other important modules--------------------------------------------------\
import random


os.system('cls' if os.name == 'nt' else "printf '\033c'") #Clears the terminal.

global done
done = False

global has_connected
has_connected = False


async def Loading_bot():
    global done
    chars = '|/-\\'
    while True:
        for c in chars:
            if done == True:
                return
            print(c, end="\r")
            await asyncio.sleep(0.1)


@client.event
async def on_ready():

    client.loop.create_task(Loading_bot())

    global done
    global has_connected
    if has_connected:
        await on_reconnect()
    else:
        has_connected = True
        print('We have logged in as {0.user}'.format(client))
        print("Name: {}".format(client.user.name))
        print("ID: {}".format(client.user.id))
        client.loop.create_task(change_status())
        done = True

'''
The bots CMD line should look like this before passing this stage:

We have logged in as EJ Multigames Discord!#6028
Name: EJ Multigames Discord!
ID: 833215082007756850
'''


async def on_reconnect():
    print('SYSTEM | Facing technical difficulty\'s')
    client.loop.create_task(change_status())

async def change_status():
    await client.wait_until_ready()#waits until bot is ready.

    while True:
        reload(packages.CRITICAL.STATUS)
        EJ_M_STATUS = packages.CRITICAL.STATUS.EJ_M_STATUS

        try:

            if EJ_M_STATUS == "ONLINE":
                activity = discord.Game(name=f"EJ DJ V{EJ_M_VERSION} | {FOOTER.footer}")
                await client.change_presence(status=discord.Status.online, activity=activity)
                await asyncio.sleep(10)

                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="?Help"))
                await asyncio.sleep(10)
                continue

            elif EJ_M_STATUS == "IDLE":
                activity = discord.Game(name=f"EJ DJ V{EJ_M_VERSION} | Under maintenance")
                await client.change_presence(status=discord.Status.idle, activity=activity)
                await asyncio.sleep(10)

                activity = discord.Game(name=f"EJ DJ V{EJ_M_VERSION} | Accounts blocked until complete")
                await client.change_presence(status=discord.Status.idle, activity=activity)
                await asyncio.sleep(10)

                activity = discord.Game(name=f"EJ DJ V{EJ_M_VERSION} | ETA: {SERVER_MAINTENENCE_TIME.time}")
                await client.change_presence(status=discord.Status.idle, activity=activity)
                await asyncio.sleep(10)
                continue

            elif EJ_M_STATUS == "OFFLINE":
                activity = discord.Game(name=f"OFFLINE | Waiting for admins")
                await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
                await asyncio.sleep(10)

                activity = discord.Game(name=f"OFFLINE | A EJ Studios dev will be on it shortly")
                await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
                await asyncio.sleep(10)
                continue

            else:
                activity = discord.Game(name=f"EJ DJ V{EJ_M_VERSION} | {FOOTER.footer}")
                await client.change_presence(status=discord.Status.online, activity=activity)
                await asyncio.sleep(10)
                continue

        except Exception as Error:
            print("SYSTEM | ERROR: Could not change bot status.\n Error: %s") % Error



'''
?login creates an account for the user with all the default values.

This is still in development and may result in save data lose for all users!
'''

@client.command(pass_context=True, aliases=["Login, LOGIN"])
async def login(ctx):
    await client.wait_until_ready()

    User = ctx.message.author

#-------------------------------------------------------------------------------------------------------------Check if the server is under maintenance or offline. 
    if packages.CRITICAL.STATUS.EJ_M_STATUS == "IDLE" or packages.CRITICAL.STATUS.EJ_M_STATUS == "OFFLINE":
        update_embed = discord.Embed(
            colour=discord.Colour.gold(),
            title="System ALERT.",
            description=f"{User}, The server is down right now, please try again when the bot is fully online.\nThank you.")
        await ctx.send(embed = update_embed)
        return

    '''
    Cannot save weapon data separately from the main save as this requires 2 different saves.
    '''

    if os.path.isfile(rf'./commands/data/PROFILES/{User}.py'):
        update_embed = discord.Embed(
            colour=discord.Colour.gold(),
            title="System ALERT.",
            description=f"{User}, You already have a profile in the database.\n Please ask a admin for further help with your account.")
        await ctx.send(embed = update_embed)
        return

    else:
        update_embed = discord.Embed(
            colour=discord.Colour.green(),
            title="System.",
            description=f"Welcome {User} to EJ Multigames Discord.\n We are creating a profile for you and preparing to save default settings!")
        await ctx.send(embed = update_embed)

        path = r'./commands/data/PROFILES/'
        file = f"{User}.py"
        with open(os.path.join(path, file), 'a') as fp:
            fp.write("")
            fp.close()
            pass

    print(f"\nSYSTEM: Setting up user: {User}'s profile.\n")

    print("\nSYSTEM: Setting default values.\n")

    level = 0
    next_level_up = int(100)
    exp = int(0)
    health = 100
    gold = 50
    healthpotion = 0
    food = 0
    wood = 0
    stone = 0
    iron = 0

    active_weapon = 'WOODEN_SWORD'

    wood_owned = True
    wood_durability = 100
    wood_attack = 10

    stone_owned = False
    stone_durability = 100
    stone_attack = 50

    iron_owned = False
    iron_durability = 100
    iron_attack = 100

    BAN = False

    print("\nSYSTEM: Setting system paths.\n")

    path = os.getcwd() + r'\commands\data\PROFILES'
    Save_New_User = os.path.join(path, f'{User}.py')

    now = date.today()
    date_now = now.strftime("%#d.%#m.%y")

    now1 = datetime.now()
    time_now = now1.strftime("%H:%M")

    print("\nSYSTEM: Preparing to write data.\n")
    f = open(Save_New_User, "w")

    print("\nSYSTEM: Writing...\n")

#---Please do not use F strings here.
    f.write("join_date = '" + str(date_now) + "' \n")
    f.write("time_join = '" + str(time_now) + "' \n")

    f.write("name = '" + str(User) + "' \n")
    f.write("exp = " + str(exp) + "\n")
    f.write("next_level_up = " + str(next_level_up) + "\n")
    f.write("level = " + str(level) + "\n")
    f.write("health = " + str(health) + "\n")
    f.write("gold = " + str(gold) + "\n")
    f.write("healthpotion = " + str(healthpotion) + "\n")
    f.write("food = " + str(food) + "\n")
    f.write("wood = " + str(wood) + "\n")
    f.write("stone = " + str(stone) + "\n")
    f.write("iron = " + str(iron) + "\n")

    f.write("active_weapon = '" + str(active_weapon) + "'\n")

    f.write("wood_owned = " + str(wood_owned) + "\n")
    f.write("wood_durability = " + str(wood_durability) + "\n")
    f.write("wood_attack = " + str(wood_attack) + "\n")

    f.write("stone_owned = " + str(stone_owned) + "\n")
    f.write("stone_durability = " + str(stone_durability) + "\n")
    f.write("stone_attack = " + str(stone_attack) + "\n")

    f.write("iron_owned = " + str(iron_owned) + "\n")
    f.write("iron_durability = " + str(iron_durability) + "\n")
    f.write("iron_attack = " + str(iron_attack) + "\n")

    f.write("BAN = " + str(BAN) + "\n")

    print("\nSYSTEM: Successfully saved main user data.\n")

    print("\nSYSTEM: Setup complete.\n")

    return





@client.command(pass_context=True, aliases=["help"])
async def Help(ctx):
    await client.wait_until_ready()

    await ctx.message.delete()

    User = ctx.message.author
    if ctx.channel.name in BOT_CHANNELS.channels:
        pfp = client.user.avatar_url

        Help_embed = discord.Embed(
            colour=discord.Colour.green(),
            title="EJ Multigames commands..",
            description=f"EJ Multigames V{EJ_M_VERSION}")

        Help_embed.set_author(name="EJ DJ", icon_url=(pfp))
        Help_embed.set_thumbnail(url=(pfp))

        Help_embed.add_field(name="Information", value="""
            Hello and welcome to EJ Studio's **`EJ Multigames discord`** to get started please make sure that you have created an account by running `?login` where you ran this command.

            EJ Multigames discord is a adventure type game that will allow you to attack mythical enemies, earn EXP and battle your friends! You will be able to buy upgrades from the shop and possibly from traders along the way!

            In order to get started please start by reading all the commands located in the `?info` command.

            Good luck, adventurer!
            """, inline=True)

        Help_embed.set_footer(text=f"{FOOTER.footer}")

        sent = await ctx.send(embed = Help_embed)
        await asyncio.sleep(120)
        await sent.delete()





@client.command()
async def SHUTDOWN(ctx):
    if str(ctx.message.author) != "EJ Studios#3379":
        update_embed = discord.Embed(
            colour=discord.Colour.green(),
            title="ACCESS_IS_DENIED",
            description=f"You do not have permission to perform high level moderation.")
        await ctx.send(embed = update_embed)
        return

    await ctx.message.delete()

    User = ctx.message.author

    logs_path = os.getcwd() + r"\packages\logs"
    system_log_path = os.path.join(logs_path, 'system_log.txt')
    log_path = os.path.join(logs_path, 'log.txt')
    error_log_path = os.path.join(logs_path, 'error_log.txt')

    activity = discord.Game(name="Shutting down, good bye!")
    await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)

    update_embed = discord.Embed(
        colour=discord.Colour.green(),
        title="",
        description=f"Shutting down, See ya.")
    await ctx.send(embed = update_embed)

    f = open(system_log_path, "a")
    now = date.today()
    date_now = now.strftime("%#d\%#m\%y")
    now1 = datetime.now()
    time_now = now1.strftime("%H:%M")
    f.write(str(f"Date: {date_now} | Time: {time_now} | User: {User}\n"))
    f.write(str(f"SYSTEM is shutting down.\n"))
    f.write(str(f"\n\n"))
    f.close()

    await client.logout()

@client.command()
async def REFRESH(ctx):
    if str(ctx.message.author) != "EJ Studios#3379":
        update_embed = discord.Embed(
            colour=discord.Colour.green(),
            title="ACCESS_IS_DENIED",
            description=f"You do not have permission to perform high level moderation.")
        await ctx.send(embed = update_embed)
        return

    await ctx.message.delete()

    User = ctx.message.author

    logs_path = os.getcwd() + r"\packages\logs"
    system_log_path = os.path.join(logs_path, 'system_log.txt')
    log_path = os.path.join(logs_path, 'log.txt')
    error_log_path = os.path.join(logs_path, 'error_log.txt')

    try:
        activity = discord.Game(name="Refreshing...")
        await client.change_presence(status=discord.Status.idle, activity=activity)

        update_embed = discord.Embed(
            colour=discord.Colour.green(),
            title="System.",
            description=f"Refreshing.")
        restart_text1 = await ctx.send(embed = update_embed)

        client.remove_command('buy')
        client.remove_command('Buy')
        client.remove_command('BUY')
        reload(commands.buy)

        client.remove_command('info')
        client.remove_command('Info')
        client.remove_command('INFO')
        reload(commands.info)

        client.remove_command('server')
        client.remove_command('Server')
        client.remove_command('SERVER')
        reload(commands.server)

        client.remove_command('status')
        client.remove_command('Status')
        client.remove_command('STATUS')
        reload(commands.change_status)

        client.remove_command('inventory')
        client.remove_command('Inventory')
        client.remove_command('INVENTORY')
        reload(commands.inventory)

        client.remove_command('use')
        client.remove_command('Use')
        client.remove_command('USE')
        reload(commands.use)

        client.remove_command('profile')
        client.remove_command('Profile')
        client.remove_command('PROFILE')
        reload(commands.profile)

        client.remove_command('invite')
        client.remove_command('Invite')
        client.remove_command('INVITE')
        reload(commands.invite)

        client.remove_command('weapon')
        client.remove_command('Weapon')
        client.remove_command('WEAPON')
        reload(commands.weapon)

        client.remove_command('change')
        client.remove_command('Change')
        client.remove_command('CHANGE')
        reload(commands.change)

        activity = discord.Game(name="Done!")

        await client.change_presence(status=discord.Status.online, activity=activity)

        await restart_text1.delete()

        update_embed = discord.Embed(
            colour=discord.Colour.green(),
            title="System.",
            description=f"Finished!")
        restart_text2 = await ctx.send(embed = update_embed)

        f = open(system_log_path, "a")
        now = date.today()
        date_now = now.strftime("%#d\%#m\%y")
        now1 = datetime.now()
        time_now = now1.strftime("%H:%M")
        f.write(str(f"Date: {date_now} | Time: {time_now} | User: {User}\n"))
        f.write(str(f"SYSTEM successfully refreshed.\n"))
        f.write(str(f"\n\n"))
        f.close()

        await asyncio.sleep(5)
        await restart_text2.delete()

    except Exception as Error:

        print(f"SYSTEM | ERROR: An error has occurred while refreshing the bot.\n Report: This error has not effected any users.\n Called by: {User}.\n Error: {Error}")

        update_embed = discord.Embed(
            colour=discord.Colour.red(),
            title="System ERROR.",
            description=f"An error has occurred while refreshing.\nReport: This error has not effected any users.\n Called by: {User}.\n\nThe bot will be switched offline until manually turned back online.")
        await ctx.send(embed = update_embed)

        print("SYSTEM | Turning the bot to offline mode.")

        path = r'./packages/CRITICAL/'
        savesave = os.path.join(path, 'STATUS.py')
        f = open(savesave, "w")
        f.write("EJ_M_STATUS = '" + str("OFFLINE") + "'")                         #player name save.
        f.close()

        f = open(error_log_path, "a")
        now = date.today()
        date_now = now.strftime("%#d\%#m\%y")
        now1 = datetime.now()
        time_now = now1.strftime("%H:%M")
        f.write(str(f"Date: {date_now} | Time: {time_now} | User: {User}\n"))
        f.write(str(f"SYSTEM unsuccessfully refreshed.\n"))
        f.write(str(f"Error: {Error}\n"))
        f.write(str(f"\n\n"))
        f.close()
        return


@client.command(pass_context = True)
async def SERVER_RESTART(ctx):

    await ctx.message.delete()

    if str(ctx.message.author) != "EJ Studios#3379":
        update_embed = discord.Embed(
            colour=discord.Colour.green(),
            title="ACCESS_IS_DENIED",
            description=f"You do not have permission to perform high level moderation.")
        await ctx.send(embed = update_embed)
        return

    User = ctx.message.author

    logs_path = os.getcwd() + r"\packages\logs"
    system_log_path = os.path.join(logs_path, 'system_log.txt')
    log_path = os.path.join(logs_path, 'log.txt')
    error_log_path = os.path.join(logs_path, 'error_log.txt')

    update_embed = discord.Embed(
        colour=discord.Colour.green(),
        title="",
        description=f"Restarting the server now.")
    await ctx.send(embed = update_embed)

    f = open(system_log_path, "a")
    now = date.today()
    date_now = now.strftime("%#d\%#m\%y")
    now1 = datetime.now()
    time_now = now1.strftime("%H:%M")
    f.write(str(f"Date: {date_now} | Time: {time_now} | User: {User}\n"))
    f.write(str(f"SYSTEM is performing a server restart.\n"))
    f.write(str(f"\n\n"))
    f.close()

    os.system("shutdown /r /t 0") 



@client.command()
async def RESTART(ctx):

    await ctx.message.delete()

    if str(ctx.message.author) != "EJ Studios#3379":
        update_embed = discord.Embed(
            colour=discord.Colour.gold(),
            title="ACCESS_IS_DENIED",
            description=f"You do not have permission to perform high level moderation.")
        info = await ctx.send(embed = update_embed)
        await asyncio.sleep(5)
        await info.delete()
        return

    try:
        User = ctx.message.author

        logs_path = os.getcwd() + r"\packages\logs"
        system_log_path = os.path.join(logs_path, 'system_log.txt')
        log_path = os.path.join(logs_path, 'log.txt')
        error_log_path = os.path.join(logs_path, 'error_log.txt')

        activity = discord.Game(name="Restarting...")
        await client.change_presence(status=discord.Status.idle, activity=activity)

        update_embed = discord.Embed(
            colour=discord.Colour.green(),
            title="System.",
            description=f"Restarting...")
        await ctx.send(embed = update_embed)

        print("\nSYSTEM: Restarting")

        f = open(system_log_path, "a")
        now = date.today()
        date_now = now.strftime("%#d\%#m\%y")
        now1 = datetime.now()
        time_now = now1.strftime("%H:%M")
        f.write(str(f"Date: {date_now} | Time: {time_now} | User: {User}\n"))
        f.write(str(f"SYSTEM successfully restarted.\n"))
        f.write(str(f"\n\n"))
        f.close()

        await client.logout()

        if platform == "linux" or platform == "linux2":
            path = (r"python3 EJ_Multigames_Discord.py")
        elif platform == "darwin":
            path = (r"python3 EJ_Multigames_Discord.py")
        elif platform == "win32":
            path = (r"python EJ_Multigames_Discord.py")

        os.system(path)

    except Exception as Error:

        print(f"SYSTEM | ERROR: An error has occurred while restarting the bot.\n Report: This error has not effected any users.\n Called by: {User}.\n Error: {Error}")

        update_embed = discord.Embed(
            colour=discord.Colour.red(),
            title="System ERROR.",
            description=f"An error has occurred while restarting.\nReport: This error has not effected any users.\n Called by: {User}.\n\nThe bot will be switched offline until manually turned back online.")
        await ctx.send(embed = update_embed)

        print("SYSTEM | Turning the bot to offline mode.")

        path = r'./packages/CRITICAL/'
        savesave = os.path.join(path, 'STATUS.py')
        f = open(savesave, "w")
        f.write("EJ_M_STATUS = '" + str("OFFLINE") + "'")                         #player name save.
        f.close()

        f = open(error_log_path, "a")
        now = date.today()
        date_now = now.strftime("%#d\%#m\%y")
        now1 = datetime.now()
        time_now = now1.strftime("%H:%M")
        f.write(str(f"Date: {date_now} | Time: {time_now} | User: {User}\n"))
        f.write(str(f"SYSTEM unsuccessfully restarted.\n"))
        f.write(str(f"Error: {Error}\n"))
        f.write(str(f"\n\n"))
        f.close()
        return

@client.event
async def on_command_error(ctx, error):
    Error = str(error)
    print("\n\nSystem | ERROR:" + Error + "\n")

    if "PermissionError:" in Error:
        print("\nSystem ERROR: The system has detected a permission error, please review logs.")
        pass

    elif "FileNotFoundError:" in Error:
        print("\nSystem ERROR: The system could not find a file, please review logs.")
        pass

    elif "IndexError:" in Error:
        print("\nSystem ERROR: The system tried accessing an index that does not exist, please review logs.")
        pass

    elif "Already playing audio." in Error:
        print("\nSystem ERROR: The system failed to play audio because their is audio already playing, please review logs.")
        pass

    elif "url1 is a required argument that is missing." in Error:
        update_embed = discord.Embed(
            colour=discord.Colour.gold(),
            title="",
            description=f">download - ERROR:\nPlease make sure to specify the song and author, or give a valid youtube link.")
        await ctx.send(embed = update_embed)

    elif "url is a required argument that is missing." in Error:
        update_embed = discord.Embed(
            colour=discord.Colour.gold(),
            title="",
            description=f">play - ERROR:\nPlease make sure to specify the song and author, or give a valid youtube link.")
        await ctx.send(embed = update_embed)

    elif "Command" and "is not found" in Error:
        update_embed = discord.Embed(
            colour=discord.Colour.gold(),
            title="",
            description=f">? - ERROR:\nPlease make sure that this command exists and you have permission to use it.")
        await ctx.send(embed = update_embed)

    else:
        reload(packages.CRITICAL.STATUS)
        EJ_M_STATUS = packages.CRITICAL.STATUS.EJ_M_STATUS
        
        if EJ_M_STATUS == "OFFLINE":
            update_embed = discord.Embed(
                colour=discord.Colour.gold(),
                title="System ALERT.",
                description=f"Please wait until EJ Multigames is back online.")
            await ctx.send(embed = update_embed)

        elif EJ_M_STATUS == "IDLE":
            update_embed = discord.Embed(
                colour=discord.Colour.gold(),
                title="System ALERT.",
                description=f"Please wait for maintenance to finish and try again.")
            await ctx.send(embed = update_embed)

        else:
            update_embed = discord.Embed(
                colour=discord.Colour.red(),
                title="System ERROR.",
                description=f"Sorry, something critical happened.\n Rest-assured the error has been saved in our logs.\n\n You may also report this error in the official server.\nUse `?invite`")
            await ctx.send(embed = update_embed)
            pass


try:
    client.run(TOKEN)
except Exception as Error:
    print(f"System Error | Could not start the bot due to an unknown reason. Error: {Error}\n\nThe system will reboot in 1 minute")
    Time = 60
    while True:
        Time -= 1
        os.system('cls' if os.name == 'nt' else "printf '\033c'") #Clears the terminal.
        print(f"System Error | Could not start the bot due to an unknown reason.\n\nError: {Error}\n\nThe system will reboot in {Time}")
        if Time != 0:
            time.sleep(1)
            continue
        os.system("shutdown /r /t 0") 

