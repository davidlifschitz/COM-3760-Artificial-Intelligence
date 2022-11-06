import copy
import numpy as np
import random
# from termcolor import colored  # can be taken out if you don't like it...

# # # # # # # # # # # # # # global values  # # # # # # # # # # # # # #
ROW_COUNT = 6
COLUMN_COUNT = 7

RED_CHAR = 'X' #colored('X', 'red')  # RED_CHAR = 'X'
BLUE_CHAR = 'O' #colored('O', 'blue')  # BLUE_CHAR = 'O'

EMPTY = 0
RED_INT = 1
BLUE_INT = 2

RED_WINS = False
BLUE_WINS = False
DRAW = False


# # # # # # # # # # # # # # functions definitions # # # # # # # # # # # # # #
def create_board():
    """creat empty board for new game"""
    board = np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)
    return board


def drop_chip(board, row, col, chip):
    """place a chip (red or BLUE) in a certain position in board"""
    board[row][col] = chip


def is_valid_location(board, col):
    """check if a given column in the board has a room for extra dropped chip"""
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    """assuming column is available to drop the chip,
    the function returns the lowest empty row  """
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    """print current board with all chips put in so far"""
    # print(np.flip(board, 0))
    print(" 1 2 3 4 5 6 7 \n" "|" + np.array2string(np.flip(np.flip(board, 1)))
        .replace("[", "").replace("]", "").replace(" ", "|").replace("0", "_")
        .replace("1", RED_CHAR).replace("2", BLUE_CHAR).replace("\n", "|\n") + "|")

def game_is_won(board, chip):
    """check if current board contain a sequence of 4-in-a-row of in the board
    for the player that play with "chip"  """

    winning_Sequence = np.array([chip, chip, chip, chip])
    # Check horizontal sequences
    for r in range(ROW_COUNT):
        if "".join(list(map(str, winning_Sequence))) in "".join(list(map(str, board[r, :]))):
            return True
    # Check vertical sequences
    for c in range(COLUMN_COUNT):
        if "".join(list(map(str, winning_Sequence))) in "".join(list(map(str, board[:, c]))):
            return True
    # Check positively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, winning_Sequence))) in "".join(list(map(str, board.diagonal(offset)))):
            return True
    # Check negatively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, winning_Sequence))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            return True
def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations

def two_in_same_row(board, chip):
    #check if the board contains one of the following sequences in the board 
    #that will give it a chance to get four in a row
    count = 0
    s_1 = np.array([chip, chip, EMPTY, EMPTY])
    s_2 = np.array([chip, EMPTY,EMPTY,chip])
    s_3 = np.array([EMPTY, EMPTY, chip, chip])
    s_4 = np.array([EMPTY, chip, EMPTY, chip])
    s_5 = np.array([chip,EMPTY, chip, EMPTY])
    s_6 = np.array([EMPTY, chip, chip,EMPTY])



    # Check -- sequences
    for r in range(ROW_COUNT):
        if "".join(list(map(str, s_1))) in "".join(list(map(str, board[r, :]))):
            count+=1
    # for r in range(ROW_COUNT):
        if "".join(list(map(str, s_2))) in "".join(list(map(str, board[r, :]))):
            count+=1
    # for r in range(ROW_COUNT):
        if "".join(list(map(str, s_3))) in "".join(list(map(str, board[r, :]))):
            count+=1
    # for r in range(ROW_COUNT):
        if "".join(list(map(str, s_4))) in "".join(list(map(str, board[r, :]))):
            count+=1
    # for r in range(ROW_COUNT):
        if "".join(list(map(str, s_5))) in "".join(list(map(str, board[r, :]))):
            count+=1
    # for r in range(ROW_COUNT):
        if "".join(list(map(str, s_6))) in "".join(list(map(str, board[r, :]))):
            count+=1
        
    # Check vertical sequences
    for c in range(COLUMN_COUNT):
        # print(list(map(str, s_1)))
        # print(list(map(str, board[:, c])))
        if "".join(list(map(str, s_1))) in "".join(list(map(str, board[:, c]))):
            count+=1
    # for c in range(COLUMN_COUNT):
        if "".join(list(map(str, s_2))) in "".join(list(map(str, board[:, c]))):
            count+=1
    # for c in range(COLUMN_COUNT):
        if "".join(list(map(str, s_3))) in "".join(list(map(str, board[:, c]))):
            count+=1
    # for c in range(COLUMN_COUNT):
        if "".join(list(map(str, s_4))) in "".join(list(map(str, board[:, c]))):
            count+=1
    # for c in range(COLUMN_COUNT):
        if "".join(list(map(str, s_5))) in "".join(list(map(str, board[:, c]))):
            count+=1
    # for c in range(COLUMN_COUNT):
        if "".join(list(map(str, s_6))) in "".join(list(map(str, board[:, c]))):
            count+=1
    
    # Check / diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, s_1))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
    # for offset in range(-2, 4):
        if "".join(list(map(str, s_2))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
    # for offset in range(-2, 4):
        if "".join(list(map(str, s_3))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
    # for offset in range(-2, 4):
        if "".join(list(map(str, s_4))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
    # for offset in range(-2, 4):
        if "".join(list(map(str, s_5))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
    # for offset in range(-2, 4):
        if "".join(list(map(str, s_6))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
            
    # Check / diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, s_1))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
    # for offset in range(-2, 4):
        if "".join(list(map(str, s_2))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
    # for offset in range(-2, 4):
        if "".join(list(map(str, s_3))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
    # for offset in range(-2, 4):
        if "".join(list(map(str, s_4))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
    # for offset in range(-2, 4):
        if "".join(list(map(str, s_5))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
    # for offset in range(-2, 4):
        if "".join(list(map(str, s_6))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
    return count


def three_in_same_row(board,chip):
    #check if the board contains one of the following sequences in the board 
    #that will give it a chance to get four in a row
    count = 0
    s_1 = np.array([chip,chip,chip,0])
    s_2 = np.array([chip,chip,0,chip])
    s_3 = np.array([chip,0,chip,chip])
    s_4 = np.array([0,chip,chip,chip])
    
    
    # Check -- seqs
    for r in range(ROW_COUNT):
        if "".join(list(map(str, s_1))) in "".join(list(map(str, board[r, :]))):
            count+=1    
        if "".join(list(map(str, s_2))) in "".join(list(map(str, board[r, :]))):
            count+=1    
        if "".join(list(map(str, s_3))) in "".join(list(map(str, board[r, :]))):
            count+=1
        if "".join(list(map(str, s_4))) in "".join(list(map(str, board[r, :]))):
            count+=1
            
            
    # Check | seqs
    for c in range(COLUMN_COUNT):
        if "".join(list(map(str, s_1))) in "".join(list(map(str, board[:, c]))):
            count+=1
        if "".join(list(map(str, s_2))) in "".join(list(map(str, board[:, c]))):
            count+=1
        if "".join(list(map(str, s_3))) in "".join(list(map(str, board[:, c]))):
            count+=1
        if "".join(list(map(str, s_4))) in "".join(list(map(str, board[:, c]))):
            count+=1
            
            
    # Check / diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, s_1))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
        if "".join(list(map(str, s_2))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
        if "".join(list(map(str, s_3))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
        if "".join(list(map(str, s_4))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
            
    # Check \ diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, s_1))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
        if "".join(list(map(str, s_2))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
        if "".join(list(map(str, s_3))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
        if "".join(list(map(str, s_4))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
    return count

# value inspired by https://github.com/jhaller19/AI/
def value(board,color):
        opponent_color = -2
        if color == RED_INT:
            opponent_color = BLUE_INT
        else:
            opponent_color = RED_INT
        val = 0
        
        #return
        if(game_is_won(board,color)):
            return 10000000
        if(game_is_won(board,opponent_color)):
            return -10000001
        # heuristic value is increased by 1 for each 2 pieces in a row by the colors player, decreased by 1 for each 2 pieces in a row by opponent colors player.
        val += two_in_same_row(board,color)
        val -= two_in_same_row(board,opponent_color)
        # heuristic value is increased by 10 for each 3 pieces in a row by the opponent colors player, -45 for each 3 pieces in a row by by the opponent colors player.
        val += three_in_same_row(board,color)*9
        val -= three_in_same_row(board,opponent_color)*45
        return val



def MoveRandom(board, color):
    valid_locations = get_valid_locations(board)
    column = random.choice(valid_locations)   # you can replace with input if you like... -- line updated with Gilad's code-- thanks!
    row = get_next_open_row(board, column)
    drop_chip(board, row, column, color)

# # # # # # # # # # # # # # main execution of the game # # # # # # # # # # # # # #
turn = 0

board = create_board()
# print_board(board)
game_over = False




def get_next_move(board,chip):
    next_boards = []
    for i in range(COLUMN_COUNT):
        if(is_valid_location(board,i)):
            current_board = copy.deepcopy(board)
            row = get_next_open_row(board,i)
            drop_chip(current_board,row,i,chip)
            next_boards.append(current_board)
    return next_boards


#defining ab_max and ab_min who keep duking it out until there's a conclusion

def ab_max(board,depth,alpha,beta,color):
    #s is max's turn ie the state
    #should return [state's value, the state after the recommended move]
    #if state is a terminal state this should return 0
    opponent_color = -1
    if color == RED_INT:
        opponent_color = BLUE_INT
    else:
        opponent_color = RED_INT
    #if search is done
    if depth == 0 or game_is_won(board,RED_INT) or game_is_won(board,BLUE_INT):
        return [value(board,color),0]
    
    val = float("-inf")
    next_state = get_next_move(board,color)
    best_move = 0
    #continue search
    for i in next_state:
        temp = ab_min(copy.deepcopy(i), depth-1,alpha,beta,color)
        if temp[0] > val:
            val = temp[0]
            best_move=i
        if val >= beta:
            return [val,i]
        if val > alpha:
            alpha = val
    return [val,best_move]
    
def ab_min(board, depth,alpha,beta,color):
    opponent_color = -1
    if color == RED_INT:
        opponent_color = BLUE_INT
    else:
        opponent_color = RED_INT
    #if search is done 
    if depth == 0 or game_is_won(board,RED_INT) or game_is_won(board,BLUE_INT):
        return [value(board,color),0]
    
    val = float("inf")
    next_state = get_next_move(board,opponent_color)
    best_move = 0
    for i in next_state:
        temp = ab_max(copy.deepcopy(i), depth-1,alpha,beta,color)
        if temp[0] < val:
            val = temp[0]
            best_move=i
        if val <= alpha:
            return [val,i]
        if val < beta:
            beta = val
    return [val,best_move]
    
    

def agent1_find_best_row(board,color):
    #for implementation made the search depth 2, can be changed
    temp_board = ab_max(board=board,depth=2,alpha=float("-inf"),beta=float("inf"),color=BLUE_INT)[1]
    for i in range(ROW_COUNT):
        for j in range(COLUMN_COUNT):
            if temp_board[i][j] != board[i][j]:
                return j
    return -1

# num_of_red_random_wins = 0
# num_of_blue_ab_minmax_wins = 0
# num_of_draws = 0
# num_of_turns = []
# for i in range(0,100):
#     game_over = False
#     board = create_board()
#     while not game_over:
#         if turn % 2 == 0:
#             # inp = input("RED please choose a column(1-7): ")
#             # while len(inp) == 0:
#             #     inp = input("Please enter an integer")
#             # print(type(inp))
#             # col = int(inp)
#             MoveRandom(board,RED_INT)
#             # while col > 7 or col < 1:
#             #     col = int(input("Invalid column, pick a valid one: "))
#             # while not is_valid_location(board, col - 1):
#             #     col = int(input("Column is full. pick another one..."))
#             # col -= 1
#             # row = get_next_open_row(board, col)
#             # drop_chip(board, row, col, RED_INT)
#             # print_board(board)
#         if turn % 2 == 1 and not game_over:
#             #here is where we implement agent1 ie the ai
#             col = agent1_find_best_row(board,BLUE_INT)
#             row = get_next_open_row(board,col)
#             drop_chip(board,row,col,BLUE_INT)
#             #MoveRandom(board,BLUE_INT)

#         # print_board(board)
        
#         if game_is_won(board, RED_INT):
#             game_over = True
#             RED_WINS = True
#             print("Red wins!")
#         if game_is_won(board, BLUE_INT):
#             game_over = True
#             BLUE_WINS = True
#             print("Blue wins!")
#         if len(get_valid_locations(board)) == 0:
#             game_over = True
#             DRAW = True
#             print("Draw!")
#         turn += 1
#     if RED_WINS:
#         num_of_red_random_wins += 1
#     if BLUE_WINS:
#         num_of_blue_ab_minmax_wins += 1
#     if DRAW:
#         num_of_draws += 1
#     num_of_turns.append(turn)
#     #tmp = copy.deepcopy(board)
# print("num_of_red_random_wins: " + str(num_of_red_random_wins))
# print("num_of_blue_ab_minmax_wins: " + str(num_of_blue_ab_minmax_wins))
# print("num_of_draws: " + str(num_of_draws))
# print(np.average(num_of_turns))

#output of red (random) vs blue (ab min-max):
#output:
# num_of_red_random_wins: 0
# num_of_blue_ab_minmax_wins: 100
# num_of_draws: 0
# 785.26


# num_of_red_ab_minmax_wins = 0
# num_of_blue_ab_minmax_wins = 0
# num_of_draws = 0
# num_of_turns = []
# for i in range(0,10):
#     turn = 0
#     game_over = False
#     board = create_board()
#     while not game_over:
#         if turn % 2 == 0:
#             # inp = input("RED please choose a column(1-7): ")
#             # while len(inp) == 0:
#             #     inp = input("Please enter an integer")
#             # print(type(inp))
#             # col = int(inp)
#             # MoveRandom(board,RED_INT)
#             col = agent1_find_best_row(board,RED_INT)
#             row = get_next_open_row(board,col)
#             drop_chip(board,row,col,RED_INT)
#             # while col > 7 or col < 1:
#             #     col = int(input("Invalid column, pick a valid one: "))
#             # while not is_valid_location(board, col - 1):
#             #     col = int(input("Column is full. pick another one..."))
#             # col -= 1
#             # row = get_next_open_row(board, col)
#             # drop_chip(board, row, col, RED_INT)
#         # print_board(board)
#         if turn % 2 == 1 and not game_over:
#             #here is where we implement agent1 ie the ai
#             col = agent1_find_best_row(board,BLUE_INT)
#             row = get_next_open_row(board,col)
#             drop_chip(board,row,col,BLUE_INT)
#             #MoveRandom(board,BLUE_INT)

#         # print_board(board)
        
#         if game_is_won(board, RED_INT):
#             game_over = True
#             RED_WINS = True
#             print("Red wins!")
#         if game_is_won(board, BLUE_INT):
#             game_over = True
#             BLUE_WINS = True
#             print("Blue wins!")
#         if len(get_valid_locations(board)) == 0:
#             game_over = True
#             DRAW = True
#             print("Draw!")
#         turn += 1
#     if RED_WINS:
#         num_of_red_ab_minmax_wins += 1
#     if BLUE_WINS:
#         num_of_blue_ab_minmax_wins += 1
#     if DRAW:
#         num_of_draws += 1
#     num_of_turns.append(turn)
#     #tmp = copy.deepcopy(board)
# print("num_of_red_ab_minmax_wins: " + str(num_of_red_ab_minmax_wins))
# print("num_of_blue_ab_minmax_wins: " + str(num_of_blue_ab_minmax_wins))
# print("num_of_draws: " + str(num_of_draws))
# print(np.average(num_of_turns))

# #Outputs
# # num_of_red_ab_minmax_wins: 10
# # num_of_blue_ab_minmax_wins: 0
# # num_of_draws: 0
# # 33.0

#user vs AI
game_over = False
board = create_board()
print_board(board)
while not game_over:
    if turn % 2 == 0:
        inp = input("RED please choose a column(1-7): ")
        while len(inp) == 0:
            inp = input("Please enter an integer")
        print(type(inp))
        col = int(inp)
        # MoveRandom(board,RED_INT)
        while col > 7 or col < 1:
            col = int(input("Invalid column, pick a valid one: "))
        while not is_valid_location(board, col - 1):
            col = int(input("Column is full. pick another one..."))
        col -= 1
        row = get_next_open_row(board, col)
        drop_chip(board, row, col, RED_INT)
        print_board(board)
    if turn % 2 == 1 and not game_over:
        #here is where we implement agent1 ie the ai
        col = agent1_find_best_row(board,BLUE_INT)
        row = get_next_open_row(board,col)
        drop_chip(board,row,col,BLUE_INT)
        #MoveRandom(board,BLUE_INT)
        print_board(board)
    
    if game_is_won(board, RED_INT):
        game_over = True
        RED_WINS = True
        print("Red wins!")
    if game_is_won(board, BLUE_INT):
        game_over = True
        BLUE_WINS = True
        print("Blue wins!")
    if len(get_valid_locations(board)) == 0:
        game_over = True
        DRAW = True
        print("Draw!")
    turn += 1