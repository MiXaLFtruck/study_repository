import time
from errors import *
from dot import Dot


class Board:
    def __init__(self, hid=False):
        self.hid = hid
        self.field = [['*' for _ in range(6)] for _ in range(6)]
        self.busy = []
        self.ships = []
        self.count = 7

    def __str__(self):
        if self.hid:
            res = "%1s Игровое поле Компьютера\n" % ('')
        else:
            res = "%4s Игровое поле Игрока\n" % ('')
        res += "\n  | 1 | 2 | 3 | 4 | 5 | 6 |"

        for i, row in enumerate(self.field):
            res += "\n" + str(i + 1) + " | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace('●', '*')
        return res

    def contour(self, ship, flag=False):
        around = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 0), (0, 1),
                  (1, -1), (1, 0), (1, 1)]

        for d in ship.dots:
            for dx, dy in around:
                neighbor = Dot(d.x + dx, d.y + dy)
                if neighbor.out or neighbor in self.busy:
                    continue
                self.busy.append(neighbor)
                if flag:
                    self.field[neighbor.x][neighbor.y] = '∙'

    def add_ship(self, ship):
        for d in ship.dots:
            if d.out or d in self.busy:
                return False
        for d in ship.dots:
            self.field[d.x][d.y] = '●'
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)
        return True

    def clear_busy(self):
        self.busy = []

    def shot(self, d):
        if d in self.busy:
            raise BoardUsedError

        self.busy.append(d)

        for ship in self.ships:
            if d in ship.dots:
                ship.health_rest -= 1
                self.field[d.x][d.y] = 'X'
                if ship.health_rest == 0:
                    print("Корабль убит!")
                    Board.timer()
                    self.count -= 1
                    self.contour(ship, flag=True)
                    return True
                else:
                    print("Корабль ранен!")
                    Board.timer()
                    return True

        self.field[d.x][d.y] = '∙'
        print("Мимо!")
        Board.timer()
        return False

    @staticmethod
    def timer():
        for i in range(15):
            print('.', end=' '), time.sleep(0.2)
        print('\n')
