from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 21261245
api_hash = 'dc4a2111ac6685402b122b6e4cdcc5e1'

with TelegramClient(StringSession(), api_id, api_hash).start(password='Egor9482787!') as client:
    print("Введите код подтверждения (и пароль 2FA, если есть)")
    print("🔑 Ваша строка сессии:")
    print(StringSession.save(client.session))
