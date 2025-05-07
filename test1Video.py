import uuid

client_id='8de0e269-07d0-40cb-b87a-facc150226de'
secret='a7e3c092-192c-4024-a9ca-80e5a12e5d7d'
auth_key='OGRlMGUyNjktMDdkMC00MGNiLWI4N2EtZmFjYzE1MDIyNmRlOmE3ZTNjMDkyLTE5MmMtNDAyNC1hOWNhLTgwZTVhMTJlNWQ3ZA=='

import base64
credentials=f"{client_id}:{secret}"
encoded_creds=base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

print(auth_key==encoded_creds)

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