in_path = "day4-input.txt"

import numpy as np

# lame solution
def score(board, d):
    return (board.sum()  - (board > 0).sum()) * d

# check a board for victory
def check(board):
    return np.any(board.sum(axis=0) == 0) or np.any(board.sum(axis=1) == 0)

# find the first winning board 
def lame_p1(boards, draws):

    cpy = np.copy(boards) + 1
    for d in draws:

        # turn draws to 0
        cpy[cpy == d+1] = 0
        wins = list(filter(check, cpy))

        if len(wins):
            return score(wins[0], d)
    return 0 


def wins_at_turn(board):
    pass

# find last winning board 
def nth_win_board(boards, draws, n):

    # preprocess. number in boards <==> turn it will be drawn
    masks = np.zeros_like(boards)
    for time, d in enumerate(draws):
        masks[boards == d] = time + 1

    # board wins at turn i <=> the minimum row/col with no 0s in the mask has `i` as max 
    win_at_turn = [wins_at_turn(m) - 1 for m in masks]
    
    # get the nth winning board, and return its scorer.
    b_index, d_index = get_nth(win_at_turn)
    return score(boards[b_index], draws[d_index])





def p1(bingo, numbers):
    pass

# preprocess
with open(in_path) as infile:
    draws = np.array(infile.readline().strip().split(','), dtype=np.int32)
    
    # woo assuming boards are of equal length and width because I'm lazy. 
    boards = np.loadtxt(infile)
    boards = boards.reshape(-1, 5, 5)
print("lame part 1: ", lame_p2(boards, draws))
#print("part 1, shadow's idea again:", p1(boards, draws))
