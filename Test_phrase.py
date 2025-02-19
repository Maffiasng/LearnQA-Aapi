class TestPhrase:
    def test_phrase(self):
        phrase = input("Введите  фразу короче 15 символов: ")
        x = len(phrase)
        assert x <= 15,"В фразе больше 15ти символов!"
