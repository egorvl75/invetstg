from telethon import TelegramClient

api_id = '21261245'
api_hash = 'dc4a2111ac6685402b122b6e4cdcc5e1'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()
    print("Клиент успешно подключен.")

with client:
    client.loop.run_until_complete(main())