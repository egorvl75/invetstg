import csv

from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

api_id = 21261245
api_hash = 'dc4a2111ac6685402b122b6e4cdcc5e1'
session_str='1ApWapzMBuwdGQJvLbaLQpOu3IKXSmM82ktnPGJGY7tfc8l1psr0bXNCTM4AAVQNMJUPVETt6wGC590dpqeigW4r3QD7Bmm3Sorv6Y9F2W2QRh9MM3CujbgvcQ5_fr0XlbeeJPU-3nPqQvA8SdCpHU4MTYSgYMcAmL5fKoHhXr9JpNbgsxM0PktQgIdJwIp9xCdW61na7nAi2c3woC8s3QCLCzSyYCduhKkPN9ZrFTfJxMMXPoc1ptG_bJqeZZ7Oz0vqnB3Lbuv4ImHkGJUe0KsZteZayKfUfGP8R36G2m3Cmg5v2gciGnCarXKjuo2exKk3SLSvxZIcq46a3CDs7UdMhhPODth8='
client = TelegramClient(StringSession(session_str), api_id, api_hash)

async def main():
    me = await client.get_me()
    print(f"Успешный вход! Здравствуйте, {me.first_name}.")

    # You can print all the dialogs/conversations that you are part of:
    # async for dialog in client.iter_dialogs():
        # if dialog.name=='R':
        #     print(dialog.name, 'has ID', dialog.id)
    channel = await client.get_entity(-503481917)
    messages=[]
    async for message in client.iter_messages(channel, limit=10):
        #print(f"{message.date} - {message.sender_id}: {message.text}")
        messages.append([message.date, message.sender_id, message.text])
        with open('messages.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Дата', 'ID отправителя', 'Сообщение'])
            writer.writerows(messages)



    # You can send messages to yourself...
    await client.send_message('me', 'Hello, myself!')

with client:
    client.loop.run_until_complete(main())