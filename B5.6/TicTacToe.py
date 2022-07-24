# board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(*board[0:3])
# print(*board[3:6])
# print(*board[6:9])


def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    # print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print(f"\t  {values[6]}  |  {values[7]}  |  {values[8]}")
    print("\t     |     |")
    print("\n")

if __name__ == "__main__":
    # print_tic_tac_toe([1, 2, 3, 4, 5, 6, 7, 8, 9])
    values = [1, 2, 3, 4, 5, 6, 17, 8, 9]
    print(f"\t  {values[6] : ^ 16}  |  {values[7]: ^ 16}  |  {values[8]: ^ 16}")
