# Класс игрока-компьютера

from random import randint
from dot import Dot
from player import Player


class AI(Player):
    # Реализация функции get_shot родителя. Получение точки выстрела от игрока-компьютера
    def get_shot(self):
        while True:
            # Если ранил, надо добивать. А не стрелять рандомно.
            if len(self.opponent.finish_him) > 1:
                i = randint(1, len(self.opponent.finish_him) - 1)
                ai_shot = self.opponent.finish_him[i]
                self.opponent.finish_him.pop(i)
            else:
                ai_shot = Dot(randint(0, self.board.side - 1), randint(0, self.board.side - 1))
            # повторять поиск точки, пока не будет свободная
            if ai_shot in self.opponent.used:
                continue
            else:
                break
        print(f"Выстрел Компьютера: {ai_shot.x + 1} {ai_shot.y + 1}")
        return ai_shot
