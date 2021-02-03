# Класс игрока-человека

from dot import Dot
from player import Player


class Human(Player):
    # Реализация функции get_shot родителя. Получение точки выстрела от игрока-человека
    def get_shot(self):
        while True:
            user_input = input("Укажите две цифры без пробела (каждая от 1 до 6): ")
            if len(user_input) != 2 or (not user_input.isdigit()):
                print("Некорректный ход!")
                continue
            row, col = map(int, user_input)
            return Dot(row - 1, col - 1)
