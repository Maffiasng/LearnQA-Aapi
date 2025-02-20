import requests

#Ex12: Тест запроса на метод header

class TestHeader:
    def test_header(selfs):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        headers =response.headers
        print(f"Headers: {headers}")
        headers_name = 'x-secret-homework-header'
        headers_value = 'Some secret value'

        assert headers_name in headers, f"Header '{headers_name}' отсутствует в ответе"
        actual_header_value = headers[headers_name]
        assert actual_header_value == headers_value, f"Ожидалось значение '{headers_value}', но получено '{actual_header_value}'"

