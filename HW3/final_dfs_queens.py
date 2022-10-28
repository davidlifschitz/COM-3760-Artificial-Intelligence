# -*- coding: utf-8 -*-
"""DFS_queens.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1puD0kHn_0jLIZbtEOzNW4Atp2JNHcaYB

This is the notebook version of the code. I will use this to explain the homework.  I used parts of the code from: https://www.sanfoundry.com/python-program-solve-n-queen-problem-without-recursion/

As we did in class, we will represent the board as a one-dimensional array where each position in the arrray is the n'th queen's column value. So if the array is: [1, 3, 0, 2], then the first queen is in position 1 (from 0--3), the second queen is in position 3 (the last column), the third queen is in the first column and the last queen is the in the second position.
"""

# hint -- you will need this for the following code: column=random.randrange(0,size)
from numpy import Infinity
import random
import math

columns = []  # columns is the locations for each of the queens
# columns[r] is a number c if a queen is placed at row r and column c.
size = int(input('Enter n: '))


"""Let's setup one iteration of the British Museum algorithm-- we'll put down 4 queens randomly."""


def place_n_queens(size):
    columns.clear()
    row = 0
    while row < size:
        column = random.randrange(0, size)
        columns.append(column)
        row += 1
    return columns


place_n_queens(size)

"""Now, we can print the result with a simple loop:"""


def display():
    for row in range(len(columns)):
        for column in range(size):
            if column == columns[row]:
                print('♛', end=' ')
            else:
                print(' .', end=' ')
        print()


# place_n_queens(size)
# display()
print(columns)

"""This of course is not necessary legal, so we'll write a simple DFS search with backtracking:"""


def solve_queen(size):
    columns.clear()
    number_of_moves = 0  # where do I change this so it counts the number of Queen moves?
    number_of_iterations = 0
    row = 0
    column = 0
    # iterate over rows of board
    while True:
        # place queen in next row
        ''''print(columns)
        print("I have ", row, " number of queens put down")
        display()
        print(number_of_moves)'''
        while column < size:
            number_of_iterations += 1
            number_of_moves += 1
            if next_row_is_safe(column):
                place_in_next_row(column)
                row += 1
                column = 0
                break
            else:
                column += 1
        # if I could not find an open column or if board is full
        if (column == size or row == size):
            number_of_iterations += 1
            number_of_moves += 1
            # if board is full, we have a solution
            if row == size:
                # print("I did it! Here is my solution")
                # display()
                # print(number_of_moves)
                return number_of_iterations, number_of_moves
            # I couldn't find a solution so I now backtrack
            prev_column = remove_in_current_row()
            if (prev_column == -1):  # I backtracked past column 1
                print("There are no solutions")
                # print(number_of_moves)
                return number_of_iterations, number_of_moves
            # try previous row again
            row -= 1
            # start checking at column = (1 + value of column in previous row)
            column = 1 + prev_column


"""This code is nice, but it uses three functions:

1. place_in_next_row

2. remove_in_current_row

3. next_row_is_safe

That we now have to define


"""


def place_in_next_row(column):
    columns.append(column)


def remove_in_current_row():
    if len(columns) > 0:
        return columns.pop()
    return -1


def next_row_is_safe(column):
    row = len(columns)
    # check column
    for queen_column in columns:
        if column == queen_column:
            return False

    # check diagonal
    for queen_row, queen_column in enumerate(columns):
        if queen_column - queen_row == column - row:
            return False

    # check other diagonal
    for queen_row, queen_column in enumerate(columns):
        if ((size - queen_column) - queen_row
                == (size - column) - row):
            return False
    return True



num_iterations=0
number_moves = 0
iterations = []
moves = []
print("######################################DFS BACKTRACK#########################################")
for i in range(0, 100):
    columns = [] #columns is the locations for each of the queens
    num_iterations, number_moves=solve_queen(size)
    moves.append(number_moves)
    iterations.append(num_iterations)
    display()
    print(columns)


max_iter = max(iterations)
max_moves = max(moves)
min_iter = min(iterations)
min_moves = min(moves)
avg_iterations = sum(iterations)/100
avg_moves = sum(moves)/100

print(f"the avg num of iters for DFS Backtracking are {avg_iterations}")
print(f"the avg num of moves for DFS Backtracking are {avg_moves}")
print(f"the max num of iters for DFS Backtracking are {max_iter}")
print(f"the max num of moves for DFS Backtracking are {max_moves}")
print(f"the min num of iters for DFS Backtracking are {min_iter}")
print(f"the min num of moves for DFS Backtracking are {min_moves}")
# print(num_iterations)
# print(number_moves)
print(columns)
# reset variables for next algorithm
del iterations
del moves
del max_iter
del max_moves
del min_iter
del min_moves
del avg_iterations
del avg_moves
display()
print(columns)
"""Now what?  Can you implement the British Museum Algorithm?  How many iterations did it take to solve the 4 queens problem?  How many did it take to solve the 8 queens (if at all)?"""

print("######################################British Museum Algorithm#########################################")
def check_if_correct(columns):
    temp_cols = columns.copy()
    columns.clear()
    for i in temp_cols:
        if not next_row_is_safe(i):
            return False
        place_in_next_row(i)
    return True


def BM(columns):
    #set
    correct = False
    num_of_iterations = 0
    num_of_moves = 0
    while(not correct):
        num_of_iterations+=1
        num_of_moves+=size
        #Randomly place queens and check if placement is a solution
        place_n_queens(size)
        correct = check_if_correct(columns)
    return num_of_iterations, num_of_moves

num_of_iterations = 0
num_of_moves = 0

iterations = []
moves = []
#because 100 loops was taking way too long i did 10 loops.
num_of_loops = 1
for i in range(num_of_loops):
    iters, mvs = BM(columns)
    iterations.append(iters)
    moves.append(mvs)
    display()
    print(columns)

max_iter = max(iterations)
max_moves = max(moves)
min_iter = min(iterations)
min_moves = min(moves)
avg_iterations = math.ceil(sum(iterations)/num_of_loops)
avg_moves = math.ceil(sum(moves)/num_of_loops)

print(f"the avg num of iters for British Museum Algorithm are {avg_iterations}")
print(f"the avg num of moves for British Museum Algorithm are {avg_moves}")
print(f"the max num of iters for British Museum Algorithm are {max_iter}")
print(f"the max num of moves for British Museum Algorithm are {max_moves}")
print(f"the min num of iters for British Museum Algorithm are {min_iter}")
print(f"the min num of moves for British Museum Algorithm are {min_moves}")

#reset variables for next algorithm
del iterations
del moves
del max_iter
del max_moves
del min_iter
del min_moves
del avg_iterations
del avg_moves
del mvs
del iters
del i
del num_iterations
del number_moves

display()
print(columns)
print("######################################Heuristic Repair/Stochastic Search/Hill Climbing#########################################")
## the main heuristic here is the largest number of threats the queen has, and to minimize that as much as possible.

# create a random (size x size) board of with placed queens

def return_n_queens(size):
    columns = []
    row = 0
    while row < size:
        column = random.randrange(0, size)
        columns.append(column)
        row += 1
    return columns

# function to determine if there is a conflict between two queens


def is_threat(row1, column1, row2, column2):
    # checking for columns
    if(column1 == column2):
        return True
    #checking for rows
    if(row1 == row2):
        return True
    # checking for diagonals - absolute value makes it work for both diagonals
    #                         for bottom left -> top right diagonals which would be adding the two rows,
    #                         and for top left -> bottom right diagonals which would be subtracting the two rows
    if(abs(column2 - column2) == abs(row1 - row2)):
        return True

    # yay no threat!
    return False

# Determine which of the queens on the board has the maximum threat level, given a board of n queens.


def max_threat_level(columns):
    max_index = -Infinity
    max_count = 0
    for first_index, i in enumerate(columns):
        cur = 0
        for second_index, j in enumerate(columns):
            if first_index != second_index:
                if is_threat(first_index, i, second_index, j) is True:
                    cur += 1
                    if(cur >= max_count):
                        max_count = cur
                        max_index = first_index
    return max_index, max_count

# will be used to determine where the queen has to go by the smallest number of conflicts returned
# given the board - columns and the row of the queen - index
def num_of_threats(board, row):
    cur = 0
    for index, i in enumerate(board):
        if index != row:
            if is_threat(index, i, row, board[row]) is True:
                cur += 1
    return cur


def climb_that_hill(size):
    iters = 1
    num_of_moves = size
    #set global var columns so it can be changed. This will affect the display() function so it should display the correct board.
    global columns
    columns = return_n_queens(size)
    while True:
        # get the max_threat_level queen
        highest_index, hueristic_cnt = max_threat_level(columns)
        found_better_place = False
        # WOOHOOO WE DID IT!!
        if(hueristic_cnt == 0):
            break
        # AWWW, KEEP ON GOING
        # now it's time to see if there are better places to put our max level threat queen
        for i in range(len(columns)):
            temp = columns.copy()
            temp[highest_index] = i
            #Phew, we found a better spot for our Queen to be less of a threat. BH
            if(num_of_threats(columns, highest_index) > num_of_threats(temp, highest_index)):
                columns = temp
                iters += 1
                num_of_moves += 1
                found_better_place = True
                break
        # Oh no! We couldn't find a better place, time to restart the board. Better luck next time!
        if found_better_place is False:
            
            columns = return_n_queens(size)
            #increment number of iterations by 1
            iters += 1
            #increment number of moves by the num of queens on the board.
            num_of_moves += size
            
    return num_of_moves, iters
num_of_loops = 1
iterations = []
moves = []
#because 100 loops was taking way too long i did 10 loops.
for i in range(num_of_loops):
    iters, mvs = climb_that_hill(size)
    iterations.append(iters)
    moves.append(mvs)
    display()
    print(columns)

max_iter = max(iterations)
max_moves = max(moves)
min_iter = min(iterations)
min_moves = min(moves)
avg_iterations = math.ceil(sum(iterations)/num_of_loops)
avg_moves = math.ceil(sum(moves)/num_of_loops)

print(f"the avg num of iters for Hill Climbing Algorithm are {avg_iterations}")
print(f"the avg num of moves for Hill Climbing Algorithm are {avg_moves}")
print(f"the max num of iters for Hill Climbing Algorithm are {max_iter}")
print(f"the max num of moves for Hill Climbing Algorithm are {max_moves}")
print(f"the min num of iters for Hill Climbing Algorithm are {min_iter}")
print(f"the min num of moves for Hill Climbing Algorithm are {min_moves}")

#reset variables for next algorithm
del iterations
del moves
del max_iter
del max_moves
del min_iter
del min_moves
del avg_iterations
del avg_moves
del mvs
del iters
del i
print("######################################Forward Checking#########################################")

# def forward_checking(size):
#     global columns
#     columns.clear()
#     num_of_moves = 0
#     num_of_iterations = 0
#     r = row = 0 # using r to be simple
#     c = column = 0 # using c to be simple
    
#     #instantiate a map for each of the columns (ie queens) to a list of the other places the queen cannot be put down
#     nu_uh = {i:[] for i in range(size)}
    
#     while True:
#         while c < size:
            
#             #if the column is not a future threat, then move it, and increment accordingly
#             if c not in nu_uh.get(r):
#                 num_of_moves +=1
#                 num_of_iterations +=1
#                 place_in_next_row(c)
#                 # nu_uh = {i:[] for i in range(size)}
#                 #now we need to check which of the future places are threats to this queen
#                 for temp_row in range(size):
#                     for temp_col in range(size):
#                         if is_threat(r,c,temp_row,temp_col) is True:
#                             nu_uh[temp_row].append(temp_col)
                
#                 r += 1 #increment row
#                 c = 0 #start over columns to be used again
#                 break 
#             else:
#                 c += 1 #increment column
#         # if we got all the way to the end of both the row and col and couldn't find a space that wasn't a threat
#         if c == size or r == size: 
#                 #woohoo we found a winner!
#                 if r == size:
#                     return num_of_iterations,num_of_moves
#                 #aw man, but don't worry, we have the back track! (which includes reseting all the forward checking)
#                 p_col = remove_in_current_row()
#                 nu_uh = {i:[] for i in range(size)}
#                 for temp_row in range(size):
#                     for temp_col in range(size):
#                         if is_threat(r,c,temp_row,temp_col) is True:
#                             nu_uh[temp_row].append(temp_col)
#                 if p_col is -1:
#                     #the columns is now sized 0. We have failed.
#                     return num_of_iterations,num_of_moves
#                 r = r -1 #move back one row
#                 c = p_col + 1 #increment col by 1 and add the previous col to it            


# num_of_loops = 10
# iterations = []
# moves = []
# #because 100 loops was taking way too long i did 10 loops.
# for i in range(num_of_loops):
#     iters, mvs = forward_checking(size)
#     iterations.append(iters)
#     moves.append(mvs)
#     display()
#     print(columns)

# max_iter = max(iterations)
# max_moves = max(moves)
# min_iter = min(iterations)
# min_moves = min(moves)
# avg_iterations = math.ceil(sum(iterations)/num_of_loops)
# avg_moves = math.ceil(sum(moves)/num_of_loops)

# print(f"the avg num of iters for Forward Checking Algorithm are {avg_iterations}")
# print(f"the avg num of moves for Forward Checking Algorithm are {avg_moves}")
# print(f"the max num of iters for Forward Checking Algorithm are {max_iter}")
# print(f"the max num of moves for Forward Checking Algorithm are {max_moves}")
# print(f"the min num of iters for Forward Checking Algorithm are {min_iter}")
# print(f"the min num of moves for Forward Checking Algorithm are {min_moves}")

# #reset variables for next algorithm
# del iterations
# del moves
# del max_iter
# del max_moves
# del min_iter
# del min_moves
# del avg_iterations
# del avg_moves
# del mvs
# del iters
# del i

                            
display()
print(columns)