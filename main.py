# Импорт необходимых модулей
import csv  # Для работы с CSV-файлами
from telethon import TelegramClient  # Основной клиент для взаимодействия с Telegram
import asyncio  # Для запуска асинхронных функций

# Ваши API-данные, полученные с https://my.telegram.org
api_id = '21261245'
api_hash = 'dc4a2111ac6685402b122b6e4cdcc5e1'

# Создание клиента Telegram с указанным именем сессии
client = TelegramClient('session_name', api_id, api_hash)

# Асинхронная функция для сбора сообщений
async def main():
    await client.start()  # Запуск клиента и авторизация

    # Получение объекта канала по его username (без @)
    channel = await client.get_entity('test')  # Замените на username интересующего канала

    messages = []  # Список для хранения сообщений

    # Итерация по последним 100 сообщениям канала
    async for message in client.iter_messages(channel, limit=100):
        # Добавление даты, ID отправителя и текста сообщения в список
        messages.append([message.date, message.sender_id, message.text])

    # Запись собранных сообщений в CSV-файл
    with open('messages.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)  # Создание объекта для записи в CSV
        writer.writerow(['Дата', 'ID отправителя', 'Сообщение'])  # Запись заголовков столбцов
        writer.writerows(messages)  # Запись всех сообщений

# Запуск асинхронной функции
with client:
    client.loop.run_until_complete(main())
