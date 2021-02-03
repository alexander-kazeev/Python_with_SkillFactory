# Класс игрового поля

from dot import Dot
from shipmisplacedexception import ShipMisPlacedException
from boardoutexception import BoardOutException
from dotusedexception import DotUsedException


class Board:
    def __init__(self, hid=False, side=6):
        self.hid = hid
        self.side = side
        self.field = [["О"] * side for _ in range(side)]
        self.ship_count = 0
        self.ships = []
        self.used = []
        self.finish_him = []

    # Добавление корабля на игровое поле
    def add_ship(self, ship):
        for ship_dot in ship.dots:
            if self.out(ship_dot) or ship_dot in self.used:
                raise ShipMisPlacedException()

        for curr_dot in ship.dots:
            self.field[curr_dot.x][curr_dot.y] = "■"
            self.used.append(curr_dot)

        self.ships.append(ship)
        self.contour(ship, shooted=False)

    # Вывод игрового поля на экран (простая версия, когда выводится только одно поле: игрока или компьютера)
    def __str__(self):
        result = ""
        result += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        result += "\n---------------------------"
        for i, curr_row in enumerate(self.field):
            result += f"\n{i + 1} | {' | '.join(curr_row)} |"
        result += "\n---------------------------"

        # Если поле противника, скрывать не подбитые палубы кораблей
        if self.hid:
            result = result.replace("■", "О")
        return result

    # Вывод игрового поля в список строк (потом можно объединить со списком строк второго поля)
    def print_list(self):
        result = []
        result.append("  | 1 | 2 | 3 | 4 | 5 | 6 |")
        result.append("---------------------------")
        for i, curr_row in enumerate(self.field):
            if self.hid:
                result.append(f"{i + 1} | {' | '.join(curr_row)} |".replace("■", "О"))
            else:
                result.append(f"{i + 1} | {' | '.join(curr_row)} |")
        result.append("---------------------------")

        return result

    # Обведение контура подбитого корабля
    def contour(self, ship, shooted=False):
        neighbor = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for ship_dot in ship.dots:
            for neighbor_x, neighbor_y in neighbor:
                current_dot = Dot(ship_dot.x + neighbor_x, ship_dot.y + neighbor_y)
                if not self.out(current_dot) and current_dot not in self.used:
                    self.used.append(current_dot)
                    if shooted:
                        self.field[current_dot.x][current_dot.y] = "∙"

    # Проверка точки выстрела на допустимое значение
    def out(self, current_dot):
        return not ((0 <= current_dot.x < self.side) and (0 <= current_dot.y < self.side))

    # Выстрел
    # Возвращает True, если после текущего выстрела может стрелять тот же игрок (ранил/потопил)
    def shot(self, shot_dot):
        if self.out(shot_dot):
            raise BoardOutException()

        if shot_dot in self.used:
            raise DotUsedException()

        self.used.append(shot_dot)

        for current_ship in self.ships:
            if shot_dot in current_ship.dots:
                current_ship.decks -= 1
                self.field[shot_dot.x][shot_dot.y] = "X"
                if current_ship.decks == 0:
                    self.ship_count += 1
                    self.contour(current_ship, shooted=True)
                    self.clear_finish()  # Потопил, значит, другие направления корабля уже простреливать не надо
                    print("Потопил!")
                    return True
                else:
                    print("Ранен!")
                    if self.hid == False:
                        self.set_finish(shot_dot)
                    return True

        self.field[shot_dot.x][shot_dot.y] = "T"
        print("Промазал!")
        return False

    # Очистка занятых точек
    def clear_used(self):
        self.used = []

    # Очистка точек возможного направления раненого корабля
    def clear_finish(self):
        self.finish_him = []

    # Набор точек возможного продолжения раненого корабля
    def set_finish(self, ship_dot):
        if self.finish_him == []:
            # Добавляем первую точку корабля и возможные направления продолжения
            self.finish_him.append(ship_dot)  # Точка нужна потом для определения направления корабля
            self.insert_finish(ship_dot, [(-1, 0), (1, 0), (0, -1), (0, 1)])  # Слева, справа, сверху и снизу
        else:
            # Удаляем точки, которые не по направлению корабля, добавляем точки по направлению корабля
            if self.finish_him[0].x == ship_dot.x:
                for index, curr_dot in enumerate(self.finish_him):
                    if curr_dot.x != ship_dot.x:
                        self.finish_him.pop(index)
                self.insert_finish(ship_dot, [(0, -1), (0, 1)])  # Сверху и снизу
            else:
                for index, curr_dot in enumerate(self.finish_him):
                    if curr_dot.y != ship_dot.y:
                        self.finish_him.pop(index)
                self.insert_finish(ship_dot, [(-1, 0), (1, 0)])  # Слева и справа

    # Создание точек возможного продолжения корабля, если они внутри игрового поля и не заняты
    def insert_finish(self, ship_dot, diff):
        for curr_diff in diff:
            curr_dot = Dot(ship_dot.x + curr_diff[0], ship_dot.y + curr_diff[1])
            if (not self.out(curr_dot)) and (curr_dot not in self.used):
                self.finish_him.append(curr_dot)
