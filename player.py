# Класс игроков - родитель

from boardexception import BoardException


class Player:
    def __init__(self, board, opponent):
        self.board = board
        self.opponent = opponent
        self.finish_ship = []

    # Получение точки выстрела от игрока
    def get_shot(self):
        raise NotImplementedError()

    # Ввод выстрела, полученного от игрока (человека или компьютера)
    def move(self):
        while True:
            try:
                curr_dot = self.get_shot()
                another_shot = self.opponent.shot(curr_dot)
                return another_shot
            except BoardException as e:
                print(e)
