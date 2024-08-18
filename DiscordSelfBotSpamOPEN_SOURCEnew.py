import discord
from discord.ext import tasks
import asyncio
from concurrent.futures import ThreadPoolExecutor

print("""

  _____ _____  _____  _____ ____  _____  _____  
 |  __ \_   _|/ ____|/ ____/ __ \|  __ \|  __ \ 
 | |  | || | | (___ | |   | |  | | |__) | |  | |
 | |  | || |  \___ \| |   | |  | |  _  /| |  | |
 | |__| || |_ ____) | |___| |__| | | \ \| |__| |
 |_____/_____|_____/ \_____\____/|_|  \_\_____/ 
  / ____|  ____| |    |  ____|                  
 | (___ | |__  | |    | |__                     
  \___ \|  __| | |    |  __|                    
  ____) | |____| |____| |                       
 |_____/|______|______|_| __                    
  / ____|  __ \ /\   |  \/  |                   
 | (___ | |__) /  \  | \  / |                   
  \___ \|  ___/ /\ \ | |\/| |                   
  ____) | |  / ____ \| |  | |                   
 |_____/|_|_/_/____\_\_|  |_|                   
 |  _ \ / __ \__   __|                          
 | |_) | |  | | | |                             
 |  _ <| |  | | | |                             
 | |_) | |__| | | |                             
 |____/ \____/  |_|                             
                                                
                                                
=====================
| BY PLXANONYMOUS0  |
=====================

# BASIC INFO: The accounts must be in the server to spam.



———————————————
""")

# List of account tokens
TOKENS = [] # You can add more tokenss hereeee

# Ask for the Channel ID to send messages to
CHANNEL_ID = int(input("Please enter the channel ID: "))
MESSAGE_INP = input('''Enter The message: ''')


class MyClient(discord.Client):
    def __init__(self, token, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = token
        self.task = None

    async def on_ready(self):
        print(f'Logged in as {self.user}')
        channel = self.get_channel(CHANNEL_ID)
        if channel:
            guild = channel.guild
            if self.user in guild.members:
                print(f"\033[92mSUCCESS\033[0m")  # Print in green
                if self.task is None:
                    self.task = self.send_message_task.start()
            else:
                print(f"\033[91mTHE ACCOUNT IS NOT IN THE SERVER\033[0m")  # Print in red
        else:
            print(f"\033[91mTHE CHANNEL DOES NOT EXIST\033[0m")  # Print in red

    @tasks.loop(seconds=1)  # Adjust the interval as needed
    async def send_message_task(self):
        channel = self.get_channel(CHANNEL_ID)
        if channel:
            await channel.send(MESSAGE_INP)


async def run_client(token):
    client = MyClient(token)
    await client.start(token)


async def main():
    with ThreadPoolExecutor() as executor:
        loop = asyncio.get_running_loop()
        tasks = [
            loop.run_in_executor(executor, asyncio.run, run_client(token))
            for token in TOKENS
        ]
        await asyncio.gather(*tasks)

# thats all
asyncio.run(main())
