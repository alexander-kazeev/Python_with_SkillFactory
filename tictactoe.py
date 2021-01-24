# Игра крестики-нолики

# функция вывода приветственного окна
def welcome_screen():
    print("====================================")
    print("      Приветствуем вас в игре       ")
    print("         Крестики-нолики!           ")
    print("====================================")
    print("        Чтобы сделать ход,          ")
    print("   укажите две цифры без пробела:   ")
    print("первая цифра - код строки от 0 до 2,")
    print("вторая цифра - код клонки от 0 до 2.")
    print(" Например, 12 (строка 1, колонка 2) ")
    print("====================================")


# функция вывода игрового поля
def show_game_field():
    print("  | 0 | 1 | 2 |")
    print("---------------")
    for i, curr_row in enumerate(game_field):
        print(f"{i} | {' | '.join(curr_row)} |")
        print("---------------")


# функция запроса хода от пользователя и обработки некорректного ввода координат
def user_move():
    while True:
        user_input = input("Укажите две цифры без пробела (каждая от 0 до 2): ")
        if len(user_input) != 2 or (not user_input.isdigit()):
            print("Некорректный ход!")
            continue
        row, col = map(int, user_input)
        if (not (0 <= row <= 2)) or (not (0 <= col <= 2)):
            print("Некорректный ход! Код строки и код колонки должны быть числами от 0 до 2!")
            continue
        if game_field[row][col] != " ":
            print("Такой ход уже был!")
            continue
        return row, col


# функция проверки на выигрыш
def check_win():
    # Создаем новые пустые списки для проверки диагоналей
    diag = []
    rotated_diag = []

    # разворот матрицы игрового поля на 90 градусов: колонки становятся строками
    rotaded_game_field = list(zip(*game_field))[::-1]

    for i in range(3):
        # Проверка на выигрыш строк и колонок
        if game_field[i].count("X") == 3 or rotaded_game_field[i].count("X") == 3:
            print("Поздравляем! Крестик выиграл!")
            return True
        if game_field[i].count("0") == 3 or rotaded_game_field[i].count("0") == 3:
            print("Поздравляем! Нолик выиграл!")
            return True

        # Набор значений в списки для последующей проверки диагоналей
        diag.append(game_field[i][i])
        rotated_diag.append(rotaded_game_field[i][i])

    # Проверка на выигрыш диагоналей
    if diag.count("X") == 3 or rotated_diag.count("X") == 3:
        print("Поздравляем! Крестик выиграл!")
        return True

    if diag.count("0") == 3 or rotated_diag.count("0") == 3:
        print("Поздравляем! Нолик выиграл!")
        return True


# Запуск игры

# вывод приветственного окна
welcome_screen()

# создание игрового поля 3x3 с пробелами вместо значений
game_field = [[" "] * 3 for i in range(3)]

# первичный вывод игрового поля, ходов еще нет
show_game_field()

# Счетчик текущего хода
move_count = 0

# Игровой движок
while True:
    # Увеличение счетчика текущего хода
    move_count += 1

    # Вывод в консоль того, кто сейчас ходит. Нечетный ход - крестик, четный ход - нолик.
    print("Ход", "крестиком" if move_count % 2 == 1 else "ноликом")

    # ход пользователя, получение от пользователя кодов строки и колонки
    row, col = user_move()

    # запись хода пользователя в игровое поле
    if move_count % 2 == 1:
        game_field[row][col] = "X"
    else:
        game_field[row][col] = "0"

    # обновление игрового поля, выводимого в консоль, с учетом всех сделанных ходов
    show_game_field()

    if move_count >= 5:  # Раньше 5-го хода выиграть невозможно
        # Проверка на наличие выигравшего
        if check_win():
            break

        # Если все клетки заполнены и победителя нет, значит, ничья
        if move_count == 9:
            print("Ничья. Повезет в следующий раз.")
            break
