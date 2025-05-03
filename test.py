from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

api_id = 21261245
api_hash = 'dc4a2111ac6685402b122b6e4cdcc5e1'
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    if not await client.is_user_authorized():
        phone = input("Введите номер (+7XXX...): ")
        await client.send_code_request(phone)
        code = input("SMS-код: ").strip()

        try:
            logging.info("Пробуем авторизоваться с кодом...")
            await asyncio.wait_for(client.sign_in(phone=phone, code=code), timeout=15)
        except SessionPasswordNeededError:
            logging.info("Запрошен пароль двухфакторной аутентификации.")
            password = input("Введите пароль 2FA: ")
            await client.sign_in(password=password)
        except asyncio.TimeoutError:
            logging.error("Превышено время ожидания при авторизации.")
            return
        except Exception as e:
            logging.error(f"Неизвестная ошибка при авторизации: {e}")
            return

    me = await client.get_me()
    print(f"Успешный вход! Здравствуйте, {me.first_name}.")

with client:
    client.loop.run_until_complete(main())