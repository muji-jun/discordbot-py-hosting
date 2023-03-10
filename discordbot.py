from cmath import log
from distutils.sysconfig import PREFIX
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

def main():
    intents = discord.Intents.all()
    client = commands.Bot(command_prefix='>', intents=intents)
    load_dotenv()

    @client.event
    async def on_ready():
        print("다음으로 로그인합니다 : ")
        print(client.user.name)
        print(client.user.id)
        print("==========")
        game = discord.Game("정상가동")
        await client.change_presence(status=discord.Status.online, activity=game)    
    
    for filename in os.listdir('./Cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'Cogs.{filename[:-3]}')

    #봇 가동
    try:
        client.run(TOKEN)
    except discord.errors.LoginFailure as e:
        print("Improper token has been passed.") 

if __name__ == '__main__':
    main()    
