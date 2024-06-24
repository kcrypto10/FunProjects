import random

def create_sudoku():
    #insert logic
    pass

def display_sudoku(board):
    for row in board: 
        print(" ".join(str(num) for num in row))

def is_valid_move(board, row, col, num):
    #check if num can be placed at board[row][col]
    pass

def solve_sudoku(board):
    #Logic to solve the puzzle
    pass

if __name__ == "__main__":
    board = create_sudoku()
    display_sudoku(board)
    if solve_sudoku(board):
        print("Sudoku Solved!")
        display_sudoku(board)
    else: 
        print("Try again!")