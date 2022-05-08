import random
from errors import *
from dot import Dot


class Player:
    def __init__(self, enemy_board):
        self.enemy_board = enemy_board


#    def move(self):


class User(Player):
    def ask(self):
        while True:
            try:
                x = input("Ваш выстрел. Введите номер строки (от 1 до 6): ")
                if not x.isdigit():
                    tmp = x.replace('.', '')
                    if tmp.isdigit():
                        raise NotIntegerError(x)
                    else:
                        raise NotNumberError(x)
                if not (1 <= int(x) <= 6):
                    raise NotInRangeError(x)
            except NumberError as s:
                print(s)
            else:
                x = int(x)
                break

        while True:
            try:
                y = input("Введите номер столбца (от 1 до 6): ")
                if not y.isdigit():
                    tmp = y.replace('.', '')
                    if tmp.isdigit():
                        raise NotIntegerError(y)
                    else:
                        raise NotNumberError(y)
                if not (1 <= int(y) <= 6):
                    raise NotInRangeError(y)
            except NumberError as s:
                print(s)
            else:
                y = int(y)
                break

        return Dot(x - 1, y - 1)


class Comp(Player):
    def ask(self):
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        return Dot(x, y)
