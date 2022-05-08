def print_gamefield(L):  # функция печати игрового поля
    print("%10s%5s%5s" % ("1", "2", "3"))
    for row in range(3):
        print("%5d%5s%5s%5s" % (row + 1, L[row * 3], L[row * 3 + 1], L[row * 3 + 2]))


def usermove_to_index(s):  # функция конвертирует номера строки и столбца, введенные пользователем в индекс массива игрового поля
    row_col = list(map(int, s))
    return (row_col[0] - 1) * 3 + row_col[1] - 1


def is_win(M):  # функция проверяет не появилась ли выигрышная комбинация
    wins = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8},
            {2, 4, 6}]  # все возможные выигрышные комбинации
    for i in wins:
        if set(M).intersection(i) == i:
            return True


game_field = ['-' for i in range(9)]  # игровое поле в начале игры
crosses = []  # индексы "крестиков"
zeroes = []  # индексы "ноликов"

print("Игровое поле в начале игры: ")
print_gamefield(game_field)

for move in range(9):  # 9 - максимально возможное количество ходов

    if not move % 2:
        user_move = input(
            "Ход игрока, играющего крестиками. Введите номер строки и номер столбца через пробел: ").replace(" ", "")
        char = 'X'
    else:
        user_move = input(
            "Ход игрока, играющего ноликами. Введите номер строки и номер столбца через пробел: ").replace(" ", "")
        char = '0'

    while True:
        if len(user_move) != 2 or not user_move.isdigit():
            user_move = input("Введите два числа - номер строки (от 1 до 3) и номер столбца (от 1 до 3): ").replace(" ",
                                                                                                                    "")
        elif user_move[0] not in ['1', '2', '3'] or user_move[1] not in ['1', '2', '3']:
            user_move = input("Числа должны быть от 1 до 3. Введите числа заново: ").replace(" ", "")
        elif game_field[usermove_to_index(user_move)] != '-':
            user_move = input("Этот ход уже был сделан. Введите числа заново: ").replace(" ", "")
        else:
            index = usermove_to_index(user_move)
            game_field[index] = char
            break

    print("\nВаш ход засчитан. Игровое поле после сделанного хода:")
    print_gamefield(game_field)

    if not move % 2:
        crosses.append(index)
        for_check = crosses
    else:
        zeroes.append(index)
        for_check = zeroes

    if move > 3 and is_win(for_check):
        print("Победил игрок, играющий ", "крестиками" if char == 'X' else "ноликами")
        break

    if move == 8:
        print("Победитель не выявлен")
