board = list(range(1, 10))

win_game = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    print("         |     |")
    print("      {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print("    -----+-----+-----")
    print("      {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print("    -----+-----+-----")
    print("      {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("         |     |")


def input_values(player_token):
    while True:
        value = input("Куда вывести " + player_token + ' ? ')
        if not (value in '123456789'):
            print("Ошибка ввода! Введите число от 1 до 9 ")
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print("Эта ячейка занята! ")
            continue
        board[value - 1] = player_token
        break


def win_check():
    for i in win_game:
        if (board[i[0] - 1]) == (board[i[1] - 1]) == (board[i[2] - 1]):
            return board[i[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            input_values('X')
        else:
            input_values('O')
        if counter > 3:
            winner = win_check()
            if winner:
                draw_board()
                print(winner, "Снимаю пред Вами шляпу. Вы победили!!! ")
                break
        counter += 1
        if counter > 8:
            draw_board()
            print("Чтож, согласен и на ничью :) ")
            break


main()
