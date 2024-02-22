import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

async def send_message(message,user_message):
    if not user_message:
        print('Message was empty because intents were not enabled')
        return
    
    is_private = user_message[0] == '?'
    
    if is_private: 
        user_message = user_message[1:]
    
    try:
        response = get_response(user_message)
        await message.author.send(response) if is_private else message.channel.send(response)
    except:
        print("error")


@client.event
async def on_ready():
    print(f'{client.user} is now running')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)
    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message,user_message)

def main():
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
        