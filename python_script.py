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
