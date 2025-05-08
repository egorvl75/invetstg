import csv

from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

api_id = 21261245
api_hash = 'dc4a2111ac6685402b122b6e4cdcc5e1'
session_str='1ApWapzMBu3sZ0gIlcHdV2URDUvj2Bf1G10SG6HJY6taBNwoSbQYSWKENmcZY7Z0SxnhwLD8-R-lPYEBffP8mIKQpKGG-Cf_AuNeRBQzLxKiLE3pFJu_WOUoyLyh9bO5SLvnvGBcGZMASLqbYX69nIDeqoN7t5vDbsM0j96r9fGjqmD8b8tM2rjwFHNteojF1wauZSeT-z96-M9lyCD4okmxdBRlFL7idLFoA6--isXliaeNqOdqJgfE-BsUtiuGu4IV56m0xeEcIZzOwB_lwyHBsO_L0jglf4uANXnOb4oPcV3mGvlbVku5vON67AnTjZIVPyjYQk3Halb3ikd1i0TShmQB2eLM='
client = TelegramClient(StringSession(session_str), api_id, api_hash)

async def main():
    me = await client.get_me()
    print(f"Успешный вход! Здравствуйте, {me.first_name}.")

    # You can print all the dialogs/conversations that you are part of:
    async for dialog in client.iter_dialogs():
        if dialog.name=='ИНВЕСТ ПОРТФЕЛЬ':
            print(dialog.name, 'has ID', dialog.id)
    channel = await client.get_entity(-1001509548243)
    messages=[]
    async for message in client.iter_messages(channel, limit=100):
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