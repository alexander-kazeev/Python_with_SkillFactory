# Класс корабля

from dot import Dot


class Ship:
    def __init__(self, coord, direction, length):
        self.coord = coord
        self.direction = direction
        self.length = length
        self.decks = length

    # Получение всех точек корабля
    @property
    def dots(self):
        ship_dots = []

        for i in range(self.length):
            curr_ship_x = self.coord.x
            curr_ship_y = self.coord.y

            if self.direction == 0:
                curr_ship_x += i
            else:
                curr_ship_y += i

            ship_dots.append(Dot(curr_ship_x, curr_ship_y))

        return ship_dots

    # Проверка на попадание выстрелом
    def hitted(self, shot):
        return shot in self.dots
