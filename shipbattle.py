# Класс игры "Морской бой"

from random import randint
from ai import AI
from board import Board
from human import Human
from ship import Ship
from dot import Dot
from shipmisplacedexception import ShipMisPlacedException


class ShipBattle:
    def __init__(self):
        human_board = self.create_board()
        ai_board = self.create_board()
        ai_board.hid = True
        self.human = Human(human_board, ai_board)
        self.ai = AI(ai_board, human_board)

    # Окно приветствия
    def welcome_screen(self):
        print("=" * 57)
        print("Приветствуем вас в игре".center(57))
        print("Морской Бой!".center(57))
        print("=" * 57)
        print("Чтобы сделать ход,".center(57))
        print("укажите две цифры без пробела:".center(57))
        print("первая цифра - код строки от 1 до 6,".center(57))
        print("вторая цифра - код клонки от 1 до 6.".center(57))
        print("Например, 12 (строка 1, колонка 2)".center(57))
        print("=" * 57)

    # Добавление доски и расстановка кораблей на доске
    def place_ships(self):
        ship_length = [3, 2, 2, 1, 1, 1, 1]
        board = Board()
        count = 0
        for curr_length in ship_length:
            while True:
                count += 1
                if count > 5000:
                    return None
                ship = Ship(Dot(randint(0, board.side - 1), randint(0, board.side - 1)), randint(0, 1), curr_length)
                try:
                    board.add_ship(ship)
                    break
                except ShipMisPlacedException:
                    pass
        board.clear_used()
        return board

    # Добавление доски с кораблями
    def create_board(self):
        board = None
        while board is None:
            board = self.place_ships()
        return board

    # Игровой цикл
    def game_cycle(self):
        move_count = 0
        player = ("Пользователь", "Компьютер")
        while True:
            self.print_boards()

            if move_count % 2 == 0:
                print(f"Ходит {player[0]}:")
                another_shot = self.human.move()
                if another_shot:
                    move_count -= 1
                if self.ai.board.ship_count == 7:
                    self.end_footer(player[0])
                    break
            else:
                print(f"Ходит {player[1]}:")
                another_shot = self.ai.move()
                if another_shot:
                    move_count -= 1
                if self.human.board.ship_count == 7:
                    self.end_footer(player[1])
                    break
            move_count += 1

    def print_boards(self):
        human_board_list = self.human.board.print_list()
        ai_board_list = self.ai.board.print_list()
        print(f"{'Ваше поле'.center(27)}   {'Поле компьютера'.center(27)}")
        for index, curr_line in enumerate(human_board_list):
            print(f"{curr_line}   {ai_board_list[index]}")

    def end_footer(self, player):
        self.print_boards()
        print(f"Игра окончена! Победил {player}!")

    def run_game(self):
        self.welcome_screen()
        self.game_cycle()


game = ShipBattle()
game.run_game()
