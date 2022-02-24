# from IPython.display import clear_output
import os
def cls():
    os.system('clear')


def printBoard(board_ptrn):
    # clear_output()
    cls()
    print(board_ptrn[7] + '  |  ' + board_ptrn[8] + '  |  ' + board_ptrn[9])
    print(f'-------------')
    print(board_ptrn[4] + '  |  ' + board_ptrn[5] + '  |  ' + board_ptrn[6])
    print(f'-------------')
    print(board_ptrn[1] + '  |  ' + board_ptrn[2] + '  |  ' + board_ptrn[3])


def start_game(p1, p2):
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while (len(li) != 0):
        v = int(input('enter player 1 position: '))
        while (v not in li):
            v = int(input('please enter valid position'))
        if (p1 == 'x'):
            board[v] = 'X'
            printBoard(board)
        else:
            board[v] = 'O'
            printBoard(board)
        li.remove(v)
        rslt = winner(board)
        if (len(rslt) != 0):
            break
        if (len(li) == 0):
            break
        v = int(input('enter player 2 position: '))
        while (v not in li):
            v = int(input('please enter valid pos:'))
        if (p2 == 'x'):
            board[v] = 'X'
            printBoard(board)
        else:
            board[v] = 'O'
            printBoard(board)

        li.remove(v)
        rslt = winner(board)
        if (len(rslt) != 0):
            break;
        if (len(li) == 0):
            break
    return board


def winner(li):
    if ((li[1] == 'X' and li[2] == 'X' and li[3] == 'X') or (li[1] == 'O' and li[2] == 'O' and li[3] == 'O')):
        # print('1')
        return 'Winner is ' + li[1]
    elif ((li[1] == 'X' and li[5] == 'X' and li[9] == 'X') or (li[1] == 'O' and li[5] == 'O' and li[9] == 'O')):
        # print('2')
        return 'Winner is ' + li[1]
    elif ((li[7] == 'X' and li[5] == 'X' and li[3] == 'X') or (li[7] == 'O' and li[5] == 'O' and li[3] == 'O')):
        # print('3')
        return 'Winner is ' + li[7]
    elif ((li[1] == 'X' and li[4] == 'X' and li[7] == 'X') or (li[1] == 'O' and li[4] == 'O' and li[7] == 'O')):
        # print('4')
        return 'Winner is ' + li[1]
    elif ((li[3] == 'X' and li[6] == 'X' and li[9] == 'X') or (li[3] == 'O' and li[6] == 'O' and li[9] == 'O')):
        # print('5')
        return 'Winner is ' + li[3]
    elif ((li[2] == 'X' and li[5] == 'X' and li[8] == 'X') or (li[2] == 'O' and li[5] == 'O' and li[8] == 'O')):
        # print('6')
        return 'Winner is ' + li[2]
    elif ((li[4] == 'X' and li[5] == 'X' and li[6] == 'X') or (li[4] == 'O' and li[5] == 'O' and li[6] == 'O')):
        # print('7')
        return 'Winner is ' + li[4]
    elif ((li[7] == 'X' and li[8] == 'X' and li[9] == 'X') or (li[7] == 'O' and li[8] == 'O' and li[9] == 'O')):
        # print('8')
        return 'Winner is ' + li[7]
    else:
        return ''


while (input('Do you want to play: Y or N: ').lower() == 'y'):
    p = input('choose player 1 X or O: ').lower()
    while (p != 'x' and p != 'o'):
        p = input('Oops invalid entry. Choose X or O: ').lower()
    if (p == 'x'):
        p1 = 'x'
        p2 = 'o'
    else:
        p1 = 'o'
        p2 = 'x'
    board = ['', '', '', '', '', '', '', '', '', '', '', '']
    i = 0
    printBoard(board)
    ret = start_game(p1, p2)
    rslt = winner(ret)
    if (len(rslt) == 0):
        print('Game is a DRAW')
    else:
        print(rslt)



