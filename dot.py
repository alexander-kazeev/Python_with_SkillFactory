# Класс точек игрового поля

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Реализация проверки equal
    def __eq__(self, compare):
        return self.x == compare.x and self.y == compare.y

    # Реализация вывода на печать
    def __repr__(self):
        return f"({self.x}, {self.y})"
