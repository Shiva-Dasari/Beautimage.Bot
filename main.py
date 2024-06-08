from typing import Final
import os
from dotenv import load_dotenv
from discord import Client, Intents , Message, File
from text_image_convertor4 import text_to_image

#step: 0
#load your somewhere safe
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)

#step 1 : seting up the bot
intents : Intents = Intents.default()
intents.message_content = True
client : Client = Client(intents=intents)


async def send_TextImage( message : Message , user_message : str ) -> None :
    if not user_message:
        return

    is_private = user_message.startswith('?')
    if is_private:
        user_message = user_message[1:]

    try:
        # Generate the image and save to file
        output_path = 'output_image.png'
        text_to_image('DancingScript-Bold.ttf', output_path, user_message)

        # Send the image file
        with open(output_path, 'rb') as f:
            picture = File(f)
            if is_private:
                await message.author.send(file=picture)
            else:
                await message.channel.send(file=picture)
    except Exception as e:
        print(e)


# print(text_to_image('DancingScript-Bold.ttf' , 'output_path.png' ,'shiva'))

@client.event
async def on_ready() -> None:
    print(f'{client.user} is running now..')

    # Send an introductory message to a specific channel
    channel_id = 732240458712875018  # Replace with your channel ID
    channel = client.get_channel(channel_id)
    if channel:
        try:
            await channel.send(
                "If you want your image sent directly to your personal Discord, use `?` before typing the message."
            )
        except Exception as e:
            print(f"An error occurred while sending the message: {e}")

@client.event
async def on_message( message : Message ) -> None :
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username} : {user_message}')
    await send_TextImage(message, user_message)


def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
