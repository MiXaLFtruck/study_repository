import random
from errors import *
from dot import Dot
from ship import Ship
from board import Board
from player import *


class Game:
    def __init__(self):
        self.pl = User(self.random_board())
        self.comp = Comp(self.random_board())
        self.pl.enemy_board.hid = True

    def try_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board()
        attempts = 0

        for ln in lens:
            while True:
                if attempts > 2000:
                    return None
                shp = Ship(ln, Dot(random.randint(0, 5), random.randint(0, 5)), random.choice(['h', 'v']))
                if board.add_ship(shp):
                    break
                attempts += 1

        board.clear_busy()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()

        return board

    def loop(self):
        move = 0
        while True:
            print(self.comp.enemy_board, '\n')
            print(self.pl.enemy_board, '\n')
            if move % 2 == 0:
                try:
                    repeat = self.pl.enemy_board.shot(self.pl.ask())
                    if self.pl.enemy_board.count == 0:
                        print("ВЫ ПОБЕДИЛИ!!!")
                        break
                except BoardUsedError as s:
                    print(s)
                    repeat = True
            else:
                while True:
                    target = self.comp.ask()
                    if target in self.comp.enemy_board.busy:
                        continue
                    break
                print(f"Компьютер стреляет в Квадрат[{target.x + 1}, {target.y + 1}]")
                repeat = self.comp.enemy_board.shot(target)
                if self.comp.enemy_board.count == 0:
                    print("Победил компьютер!")
                    break

            if repeat:
                move -= 1

            move += 1

    def greet(self):
        print("    -------------------")
        print("      Приветсвуем вас  ")
        print("          в игре       ")
        print("        Морской бой    ")
        print("    -------------------\n")


g = Game()
g.greet()
g.loop()
