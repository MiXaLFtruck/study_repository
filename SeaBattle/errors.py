class BoardUsedError(Exception):
    def __str__(self):
        return "Вы уже стреляли в этот квадрат"


class NumberError(Exception):
    def __init__(self, string):
        self.string = string


class NotIntegerError(NumberError):
    def __str__(self):
        return f'{self.string} - это не целое число'


class NotNumberError(NumberError):
    def __str__(self):
        return f'{self.string} - это не число'


class NotInRangeError(NumberError):
    def __str__(self):
        return f'Число {self.string} не в диапазоне от 1 до 6'