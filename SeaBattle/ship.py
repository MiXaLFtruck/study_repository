from dot import Dot


class Ship:
    def __init__(self, length, bow_dot, direction):
        self.length = length
        self.bow_dot = bow_dot
        self.direction = direction
        self.health_rest = length

    @property
    def dots(self):
        ship_dots = []

        for i in range(self.length):
            x = self.bow_dot.x
            y = self.bow_dot.y

            if self.direction == 'v':
                x += i
            else:
                y += i

            ship_dots.append(Dot(x, y))

        return ship_dots
