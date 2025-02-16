import json
import requests

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
pars = json.loads(json_text)
second_message = pars['messages'][1]['message']
print(second_message)


#get-Длинный редирект
response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

for i, redirect in enumerate(response.history):
    count_red= i
    print(f"Redirect #{i+1}:{redirect.url}") #выводим редиректы с изначальной  точки назначения

print(f"Количество редиректов:{count_red} до Конечного URL:{response.url}")

#______________________
#Ex7: Запросы и методы
#______________________

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
methods = ("POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS","GET")
values = ["POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS","GET"]

#1 Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
response = requests.request(method='post', url=url)
print(f"Запрос без параметра method!\n{response.text} - {response.status_code}\n")

#2 Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
response = requests.request(method='options', url=url)
print(f"Запрос не из списка!\n{response.text} - {response.status_code}\n")

#3  Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
response = requests.request(method='POST', url=url, data={"method":"POST"})
print(f"Запрос с правильным значением method!\n{response.text} - {response.status_code}\n")

#4 Цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
for method in methods:
    for value in values:
        try:
            response = requests.request(method=method, url=url, data ={"method": value})
            if response.status_code == 200:
                print(f"Метод: {method} \n"
                      f"Полученный ответ: {response.json()}, Код ответа: {response.status_code} \n"
                      f"Значание которое передаем: {value}\n")
            if method == value:# если метод равен параметру method.
                print(f"Метод:{method}\n"
                      f"Полученный ответ:{response.text}, Код ответа:{response.status_code}\n"
                      f"Значание которое передаем: {value}\n")
        except requests.RequestException as e:
            pass
        try:
            response = requests.request(method=method, url=url, params={"method": value})
            if response.status_code == 200:
                print(f"Метод: {method} \n"
                      f"Полученный ответ: {response.text}, Код ответа: {response.status_code} \n"
                      f"Значание которое передаем: {value}\n")
            if method == value and method != "GET" and response.status_code != 400:
                print(f"Метод:{method}\n"
                      f"Полученный ответ:{response.text}, Код ответа:{response.status_code}\n"
                      f"Значание которое передаем: { value}\n")
        except requests.RequestException as e:
            pass