from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

api_id = 21261245
api_hash = 'dc4a2111ac6685402b122b6e4cdcc5e1'

async def main():
 if not await client.is_user_authorized():
  phone = input("Введите номер (+7XXX...): ")

  # Отправка кода
  await client.send_code_request(phone)
  code = input("SMS-код: ").strip()

  try:
   await client.sign_in(phone=phone, code=code)
  except SessionPasswordNeededError:
   # Запрос пароля 2FA
   password = input("Пароль двухэтапной аутентификации: ")
   await client.sign_in(password=password)

  # Сохранение сессии
  await client.session.save()
  print("Сессия сохранена!")

 me = await client.get_me()
 print(f"Успешный вход: {me.first_name}")


if __name__ == '__main__':
 client = TelegramClient('session_name', api_id, api_hash)

 try:
  with client:
   client.loop.run_until_complete(main())
   client.loop.run_until_complete(asyncio.sleep(3))  # Критически важно!
 except Exception as e:
  print(f"Фатальная ошибка: {str(e)}")
 finally:
  client.disconnect()

 input("Нажмите Enter...")