import requests

import time

from requests import JSONDecodeError

url = "https://playground.learnqa.ru/ajax/api/longtime_job"
#1 создал задачу
response = requests.get(url=url)
token = response.json()
#2 делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
x = token["token"]
time_waiting = token["seconds"]
params = {"token":x}
try:
    response2 = requests.get(url=url, params=params)#для теста "error" {"token":"gNzoxMwozMyAyNx0iMw0SNyAjz"})
    pars = response2.json()
    if 'status' in pars:
        print("Задача еще неготова")
    if 'error' in pars:
        print(f"{pars['error']}")
except requests.RequestException as e:
    print(xz, e)
#3 ждать нужное количество секунд
time.sleep(time_waiting)
#4 Запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result
try:
    response2 = requests.get(url=url, params=params)
    pars = response2.json()
    if pars['status'] == 'Job is ready' and pars['result']:
        print("Задача готова")
except JSONDecodeError:
    print(xz2)

