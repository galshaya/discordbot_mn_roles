import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, DMChannel, utils


from responses import get_response

# LOAD TOKEN FROM DOTENV
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID'))  # Add this to your .env file


# BOT SETUP
intents = Intents.default()
intents.message_content = True
intents.dm_messages = True
intents.guild_messages = True
intents.members = True
client = Client(intents=intents)

# MESSAGES
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    try:
        response: str = get_response(user_message)
        
        if response == 'COMMAND_GIVE_ROLE':
            guild = client.get_guild(GUILD_ID)
            if guild:
                member = guild.get_member(message.author.id)
                if member:
                    role = utils.get(guild.roles, name="mcdh2s2")
                    if role:
                        await member.add_roles(role)
                        await message.author.send("Role has been assigned to you in the server, enjoy the workshop!")
                    else:
                        await message.author.send("The 'mcdh2s2' role doesn't exist in the server. Please contact an administrator.")
                else:
                    await message.author.send("You don't seem to be a member of the server. Make sure you've joined the server before using this command.")
            else:
                await message.author.send("I couldn't find the associated server. Please contact an administrator.")
        else:
            await message.author.send(response)
    except Exception as e:
        print(f"Error sending message: {e}")
        await message.author.send("An error occurred while processing your request. Please try again later or contact an administrator.")

# HANDLING STARTUP
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# INCOMING MESSAGE
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    if not isinstance(message.channel, DMChannel):
        return  # Ignore messages that are not in DMs

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

# ENTRY POINT
def main() -> None:
    client.run(TOKEN)

if __name__ == '__main__':
    main()