# # import requests
# # import urllib3
# #
# # # Отключаем вывод предупреждения
# # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# #
# # auth_data = {
# #     'scope': 'GIGACHAT_API_PERS',
# #     'grant_type': 'client_credentials',
# #     'client_id': '8de0e269-07d0-40cb-b87a-facc150226de',
# #     'client_secret': 'a7e3c092-192c-4024-a9ca-80e5a12e5d7d'
# # }
# #
# # response = requests.post(
# #     'https://ngw.devices.sberbank.ru:9443/api/v2/oauth',
# #     data=auth_data,
# #     headers={'Content-Type': 'application/x-www-form-urlencoded'},
# #   verify=False
# # )
# # response = requests.request("POST", url, headers=headers, data=payload)
# # print(response.text)
#
#
# import requests
#
# url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
#
# payload={
#   'scope': 'GIGACHAT_API_PERS'
# }
# headers = {
#   'Content-Type': 'application/x-www-form-urlencoded',
#   'Accept': 'application/json',
#   'RqUID': '607de185-1e41-468d-890f-317478a89453',
#   'Authorization': 'Basic OGRlMGUyNjktMDdkMC00MGNiLWI4N2EtZmFjYzE1MDIyNmRlOmE3ZTNjMDkyLTE5MmMtNDAyNC1hOWNhLTgwZTVhMTJlNWQ3ZA=='
# }
#
# response = requests.request("POST", url, headers=headers, data=payload,verify=False)
#
# print(response.text)

from gigachat import GigaChat
import requests

url = "https://gigachat.devices.sberbank.ru/api/v1/models"

payload={}
headers = {
  'Accept': 'application/json',
  'Authorization': 'eyJjdHkiOiJqd3QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiUlNBLU9BRVAtMjU2In0.Hb88HukHKIqc1DcBULUHg50lavQ0nsx-qxjXMZwY1mSqYf6_qaMECJufvd6HywfSICZON92MwJkre6hKxMD_AItGgJOMCHTKl6FBlzothHNzaC1VvQDTfcKPSkDHdjmgOAST05L67nNKFFLwp79S3JmBZP5ksdbL-HhEbYBgouOYoj0GiqPYod2KXQzcERPpg7AK-rGX1tEdvPr9fYD47NbIfuSTXtxeezzEKPvNCUMYZeTA7LTRKoxB2DVsFKVAM_LZVyaAwdrG87cVelu4KIsIS6lhdDeZfp7XYCKaSo3tR8Vujku9hs763E1SDiMWFJmZKImFbq_FJjG3ML1lgA.rQn3J1nI13EdGOQGVw5vjw.GQHmfJaGyOUwLMb8Pk2eCs5wZpGkbW8bpM5YFcnAZRdCzyFgFGjQK8ueDmTGZ89kiaQsPtKbfNIzUee8sPwgbPORqqRqBUuQHX6u7OV8BXyeYcJzYiGQ0eJyqKPDIeHl8Dwv86LNumrp9hkBHozHveWeafXOhjhnwZn6-YLbc7aAFh54Y_Ziq1mtnGAFdAIa0pPUfy9NtLgoz44epCh0VH8oGEDYQbcJsQVJPK2Mw9DNR0_xxk4s4D4YDkMplCLVHNF2WVQ05DzEamEvrfRgc338nCFLaMOOOQWNkzRrAnvLa52w7CnYKH57k20gWlM5ERNFTtWrEGJWVTGeO5Rd72GFRksfDXUjUzB9Sd-kt_zUg7wFK0Q4MWH_vKUBMKT6fxxTvWbdRz9dlfQ2JG9iWVfZ0p3fSfU7jNVGuRfwEXjdlDCEmgK4YS9Xlr5xAgf5cE85zHbm44qvOp8HN7hXG8giqXfIMiDjhuUGEvxZrGiR_meKNHZGJZBUHiYDP457Uh_Y8H1PQaVFYe4l0CTj_O8wjq3so9SjXPoiHFhNrB_LuRgN8qW6egWNUCcB_ErUwDRaxdHE9fewQDEOXQzbJ1_lbyDVOaIU_PZFet2_nvr4mf9fm5f-oJ6rnqXyZVauJhcp-I4Pn6N48cNC4FuSwBTvjYb2u32U-5bXMGdggQTopsrPWo4TgJZL7UlvOfQrRqtBOBor1hp0rDXubqprqFYKMYo7_MQAaEZZ6T06Fwc.OyYcRYSQ2pc13bPJCnnISeL7sZPUu0ckQAt5pgfWTR8'
}

giga=GigaChat()

response = requests.request("GET", url, headers=headers, data=payload,verify=False)

print(response.text)