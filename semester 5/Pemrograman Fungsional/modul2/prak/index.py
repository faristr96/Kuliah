import random
import msvcrt
import os

generateRandomInt = lambda max_value: random.randint(0, max_value - 1)

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def createBoard():
    clear()
    print('~~ Selamat Bermain ~~\n')
    width, height = map(int, input('Enter the board width and height ("5 5"): ').split())
    print('\nNew board generated')

    boards = [['-' for _ in range(width)] for _ in range(height)]

    a_x, a_y = generateRandomInt(width), generateRandomInt(height)
    o_x, o_y = generateRandomInt(width), generateRandomInt(height)

    while (a_x, a_y) == (o_x, o_y):
        o_x, o_y = generateRandomInt(width), generateRandomInt(height)

    boards[a_y][a_x] = "A"
    boards[o_y][o_x] = "O"

    positions = {
        'matrix': [width, height],
        'bidak': [a_y, a_x],
        'goals': [o_y, o_x],
    }

    return boards, positions

def printBoard(board):
    print('\n')
    for row in board:
        print(' '.join(row))

def movement(board):
    boards, positions = board
    printBoard(boards)

    while True:
        a_y, a_x = positions['bidak']
        o_y, o_x = positions['goals']

        if a_y == o_y and a_x == o_x:
            print('You Win !!!')
            break

        key = msvcrt.getch()

        if key == b'w' and a_y > 0:
            boards[a_y][a_x] = '-'
            boards[a_y - 1][a_x] = 'A'
            positions['bidak'] = a_y - 1, a_x
        elif key == b'a' and a_x > 0:
            boards[a_y][a_x] = '-'
            boards[a_y][a_x - 1] = 'A'
            positions['bidak'] = a_y, a_x - 1
        elif key == b's' and a_y < positions['matrix'][1] - 1:
            boards[a_y][a_x] = '-'
            boards[a_y + 1][a_x] = 'A'
            positions['bidak'] = a_y + 1, a_x
        elif key == b'd' and a_x < positions['matrix'][0] - 1:
            boards[a_y][a_x] = '-'
            boards[a_y][a_x + 1] = 'A'
            positions['bidak'] = a_y, a_x + 1
        elif key == b'q':
            break

        clear()
        printBoard(boards)

boards, positions = createBoard()
movement((boards, positions))
