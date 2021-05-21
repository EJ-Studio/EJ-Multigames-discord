
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


@client.command(pass_context=True, aliases=["Info", "INFO"])
async def info(ctx):
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

    pfp = client.user.avatar_url

    pages = 6
    cur_page = 1

    info_1 = discord.Embed(
        colour=discord.Colour.green(),
        title="?profile",
        description=f"EJ Multigames V{EJ_M_VERSION}.")
    info_1.set_author(name="EJ Multigames", icon_url=(pfp))
    info_1.set_thumbnail(url=(pfp))
    info_1.add_field(name="?profile | ?Profile | ?PROFILE:", value="""
        This command allows you to view the main stats in your account.

        This includes your EXP, health and current weapon. 
        """, inline=True)
    info_1.set_footer(text=f"Page 1/{pages} \n{FOOTER.footer}")

    #PLAY COMMAND----------------
    info_2 = discord.Embed(
        colour=discord.Colour.green(),
        title="?inventory",
        description=f"EJ Multigames V{EJ_M_VERSION}.")
    info_2.set_author(name="EJ Multigames", icon_url=(pfp))
    info_2.set_thumbnail(url=(pfp))
    info_2.add_field(name="?inventory | ?Inventory | ?INVENTORY",
        value="""
        This command will show you everything in your inventory and how much you have of everything.
        """, inline=True)
    info_2.set_footer(text=f"Page 2/{pages} \n{FOOTER.footer}")

    #PAUSE COMMAND--------------------
    info_3 = discord.Embed(
        colour=discord.Colour.green(),
        title=">pause",
        description=f"The main pause command.")
    info_3.set_author(name="EJ DJ", icon_url=(pfp))
    info_3.set_thumbnail(url=(pfp))
    info_3.add_field(name=">pause | >Pause",
        value="""
        Pauses any current playing music.
        Works for:
        >play
        >radio
        >playlist.
        """, inline=True)
    info_3.set_footer(text=f"Page 3/{pages} \n{FOOTER.footer}")

    #RESUME COMMAND---------------------
    info_4 = discord.Embed(
        colour=discord.Colour.green(),
        title=">resume",
        description=f"The main resume command.")
    info_4.set_author(name="EJ DJ", icon_url=(pfp))
    info_4.set_thumbnail(url=(pfp))
    info_4.add_field(name=">resume | >Resume",
        value="""
        Resumes any paused music.\n
        Works for any paused music.
        """, inline=True)
    info_4.set_footer(text=f"Page 4/{pages} \n{FOOTER.footer}")

    info_5 = discord.Embed(
        colour=discord.Colour.green(),
        title=">join",
        description=f"The main join command.")
    info_5.set_author(name="EJ DJ", icon_url=(pfp))
    info_5.set_thumbnail(url=(pfp))
    info_5.add_field(name=">join | >Join",
        value="""
        Joins the bot to your current voice chat.\n
        If you are not in a voice chat the bot should notify you.
        """, inline=True)
    info_5.set_footer(text=f"Page 5/{pages} \n{FOOTER.footer}")

    info_6 = discord.Embed(
        colour=discord.Colour.green(),
        title=">leave",
        description=f"The main leave command.")
    info_6.set_author(name="EJ DJ", icon_url=(pfp))
    info_6.set_thumbnail(url=(pfp))
    info_6.add_field(name=">leave | >Leave",
        value="""
        Makes the bot leave your voice channel\n
        If you are not in a voice chat the bot should notify you.
        """, inline=True)
    info_6.set_footer(text=f"Page 6/{pages} \n{FOOTER.footer}")




    message = await ctx.send(embed = info_1)
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")
    #adds reactions.

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                if cur_page == 1:
                    await message.edit(embed=info_1)

                elif cur_page == 2:
                    await message.edit(embed=info_2)

                elif cur_page == 3:
                    await message.edit(embed=info_3)

                elif cur_page == 4:
                    await message.edit(embed=info_4)

                elif cur_page == 5:
                    await message.edit(embed=info_5)

                elif cur_page == 6:
                    await message.edit(embed=info_6)

                # await message.edit(embed=info)
                await message.remove_reaction(reaction, user)


            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1

                if cur_page == 1:
                    await message.edit(embed=info_1)

                elif cur_page == 2:
                    await message.edit(embed=info_2)

                elif cur_page == 3:
                    await message.edit(embed=info_3)

                elif cur_page == 4:
                    await message.edit(embed=info_4)

                elif cur_page == 5:
                    await message.edit(embed=info_5)

                elif cur_page == 6:
                    await message.edit(embed=info_6)

                #await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.delete()
            break
            # ending the loop if user doesn't react after x seconds