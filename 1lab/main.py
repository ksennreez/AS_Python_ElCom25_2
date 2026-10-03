def toggle_light(board, r_index, c_index):
    # переключение самой клетки
    if board[r_index][c_index] == 1:
        board[r_index][c_index] = 0
    else:
        board[r_index][c_index] = 1

    # сдвиги: вверх, вниз, влево, вправо
    neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    for step in neighbors:
        nr = r_index + step[0]
        nc = c_index + step[1]
        
        # проверка, что сосед не вылез за границы поля
        if 0 <= nr <= 4 and 0 <= nc <= 4:
            if board[nr][nc] == 1:
                board[nr][nc] = 0
            else:
                board[nr][nc] = 1

def check_win(board):
    # если есть хоть одна единица - игра продолжается
    for r in range(5):
        for c in range(5):
            if board[r][c] == 1:
                return False  
    return True  

def main():
    print("Игра 'Выключи свет'. Используется фиксированная решаемая расстановка.")
    
    # 1 - включено (*), 0 - выключено (.)
    board = [
        [1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1]
    ]
    
    moves = 0
    finished = False

    # основной цикл партии
    while not finished:
        print("  1 2 3 4 5")
        for r in range(5):
            row_str = str(r + 1) + " "
            for c in range(5):
                if board[r][c] == 1:
                    row_str = row_str + "* "
                else:
                    row_str = row_str + ". "
            print(row_str)

        print("Введите координаты хода (строка столбец), например 3 2:")
        raw_input = input()

        # защита от падения программы при кривом вводе
        parts = raw_input.split()
        if len(parts) != 2:
            print("Ошибка: нужно ввести ровно два числа через пробел. Попробуйте снова.")
            continue

        if not (parts[0].isdigit() and parts[1].isdigit()):
            print("Ошибка: координаты должны быть числами. Попробуйте снова.")
            continue

        r = int(parts[0])
        c = int(parts[1])

        if r < 1 or r > 5 or c < 1 or c > 5:
            print("Ошибка: координаты вне поля. Введите числа от 1 до 5.")
            continue

        # перевод координат в индексы (с нуля) и ход
        toggle_light(board, r - 1, c - 1)
        moves = moves + 1

        if check_win(board) == True:
            finished = True

    # вывод финального пустого поля
    print("  1 2 3 4 5")
    for r in range(5):
        row_str = str(r + 1) + " "
        for c in range(5):
            if board[r][c] == 1:
                row_str = row_str + "* "
            else:
                row_str = row_str + ". "
        print(row_str)

    print("Поздравляю! Все лампы выключены.")
    print("Сделано ходов:", moves)

if __name__ == "__main__":
    main()