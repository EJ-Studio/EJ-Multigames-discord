
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




# @client.event
# async def on_raw_reaction_add(payload):
#     print("SOMEONE REACTED")



@client.command(pass_context=True, aliases=["Update"])
async def update(ctx):
    if ctx.channel.name in BOT_CHANNELS.channels:

        pfp = client.user.avatar_url

        update_embed = discord.Embed(
            colour=discord.Colour.green(),
            title="UPDATE",
            description=f"EJ DJ V{EJ_DJ_VERSION}")

        update_embed.set_author(name="Trinity", icon_url=(pfp))
        update_embed.set_thumbnail(url=(pfp))

        update_embed.add_field(name="NEW:", value="""
            -PROFILES!!!\n
            -Changed the radio stop command to " stop radio ".\n
            -Updated the help channel.
            """, inline=True)

        update_embed.add_field(name="FIXED:", value="""
            -Fixed the stop command from sometimes causing file leaks.
            """, inline=True)

        update_embed.add_field(name="KNOWN BUGS:", value="""
            -Their is a known bug when trying to play 2 songs at the same time.
            """, inline=True)

        update_embed.add_field(name="Report:", value="""
            If you find a bug and wish to report it, please contact\n@EJ Studios#3379 or @Happypat900#8268
            """, inline=False)

        update_embed.set_footer(text=f"{FOOTER.footer}")

        await ctx.send(embed = update_embed)
