def print_board(board):
    print(' {} | {} | {} '.format(board['top-L'],board['top-M'],board['top-R']))
    print('---+---+---')
    print(' {} | {} | {} '.format(board['mid-L'],board['mid-M'],board['mid-R']))
    print('---+---+---')
    print(' {} | {} | {} '.format(board['low-L'],board['low-M'],board['low-R']))

the_board = {
    'top-L':'', 'top-M':'', 'top-R':'',
    'mid-L':'', 'mid-M':'', 'mid-R':'',
    'low-L':'', 'low-M':'', 'low-R':''
    }

turn = 'X'
for i in range(9):
    print_board(the_board)
    print('Turn for {}. Move on which space?'.format(turn))

    move = input()
    the_board[move] = turn
    
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print_board(the_board)
