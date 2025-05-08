import uuid

client_id='8de0e269-07d0-40cb-b87a-facc150226de'
secret='a7e3c092-192c-4024-a9ca-80e5a12e5d7d'
auth_key='OGRlMGUyNjktMDdkMC00MGNiLWI4N2EtZmFjYzE1MDIyNmRlOmE3ZTNjMDkyLTE5MmMtNDAyNC1hOWNhLTgwZTVhMTJlNWQ3ZA=='

import base64
credentials=f"{client_id}:{secret}"
encoded_creds=base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

#print(auth_key==encoded_creds)

import requests
import uuid

def get_token(auth_token, scope='GIGACHAT_API_PERS'):
    """
      Выполняет POST-запрос к эндпоинту, который выдает токен.

      Параметры:
      - auth_token (str): токен авторизации, необходимый для запроса.
      - область (str): область действия запроса API. По умолчанию — «GIGACHAT_API_PERS».

      Возвращает:
      - ответ API, где токен и срок его "годности".
      """
    # Создадим идентификатор UUID (36 знаков)
    rq_uid = str(uuid.uuid4())

    # API URL
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    # Заголовки
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': rq_uid,
        'Authorization': f'Basic {auth_token}'
    }

    # Тело запроса
    payload = {
        'scope': scope
    }

    try:
        # Делаем POST запрос с отключенной SSL верификацией
        # (можно скачать сертификаты Минцифры, тогда отключать проверку не надо)
        response = requests.post(url, headers=headers, data=payload, verify=False)
        return response
    except requests.RequestException as e:
        print(f"Ошибка: {str(e)}")
        return -1


response = get_token(auth_key)

if response != 1:
    print(response.text)
    giga_token = response.json()['access_token']


import requests
import json

def get_chat_completion(auth_token, user_message, conversation_history=None):
    """
    Отправляет POST-запрос к API чата для получения ответа от модели GigaChat в рамках диалога.

    Параметры:
    - auth_token (str): Токен для авторизации в API.
    - user_message (str): Сообщение от пользователя, для которого нужно получить ответ.
    - conversation_history (list): История диалога в виде списка сообщений (опционально).

    Возвращает:
    - response (requests.Response): Ответ от API.
    - conversation_history (list): Обновленная история диалога.
    """
    # URL API, к которому мы обращаемся
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    # Если история диалога не предоставлена, инициализируем пустым списком
    if conversation_history is None:
        conversation_history = []

    # Добавляем сообщение пользователя в историю диалога
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    # Подготовка данных запроса в формате JSON
    payload = json.dumps({
        "model": "GigaChat:latest",
        "messages": conversation_history,
        "temperature": 1,
        "top_p": 0.1,
        "n": 1,
        "stream": False,
        "max_tokens": 512,
        "repetition_penalty": 1,
        "update_interval": 0
    })

    # Заголовки запроса
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {auth_token}'
    }

    # Выполнение POST-запроса и возвращение ответа
    try:
        response = requests.post(url, headers=headers, data=payload, verify=False)
        response_data = response.json()
        print(response_data)

        # Добавляем ответ модели в историю диалога
        conversation_history.append({
            "role": "assistant",
            "content": response_data['choices'][0]['message']['content']
        })

        return response, conversation_history
    except requests.RequestException as e:
        # Обработка исключения в случае ошибки запроса
        print(f"Произошла ошибка: {str(e)}")
        return None, conversation_history

# Пример использования функции для диалога

#conversation_history = []

# Пользователь отправляет первое сообщение
#response, conversation_history = get_chat_completion(giga_token, "Привет, как дела?", conversation_history)

# Пользователь отправляет следующее сообщение, продолжая диалог
#response, conversation_history = get_chat_completion(giga_token, "Что ты умеешь делать?", conversation_history)

#print(conversation_history)

def get_files(auth_token):
    import requests

    url = "https://gigachat.devices.sberbank.ru/api/v1/files"

    payload = {}
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {auth_token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    print(response.text)

def put_files(creds,file_name ):
    from gigachat import GigaChat

    giga = GigaChat(
        credentials=creds,
        verify_ssl_certs=False,
    )

    file = giga.upload_file(open(file_name, "rb"))

#put_files(encoded_creds,'txt.txt')
#get_files(giga_token)

def analyze_file(creds,id):
    from gigachat import GigaChat

    giga = GigaChat(
        credentials=creds,
        verify_ssl_certs=False,
    )

    result = giga.chat(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Проведи аналитику данного файла по инвестиционным рекомендациям. Предоставь структурированную информацию по нему.",
                    "attachments": [id],
                }
            ],
            "temperature": 1
        }
    )

    print(result.choices[0].message)

analyze_file(encoded_creds,'4575d919-8c2f-4625-8c8d-c2d36b9e8303')
