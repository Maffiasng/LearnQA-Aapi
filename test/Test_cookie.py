import requests

#Ex11: Тест запроса на метод cookie

class TestCookie:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie_name = 'HomeWork'
        cookie_value = response.cookies.get(cookie_name)
        print(f"Cookie name: {cookie_name}, cookie value: {cookie_value}")

        assert cookie_value == 'hw_value', f"Cookie {cookie_name} значение: {cookie_value}"
