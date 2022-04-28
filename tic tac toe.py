# Tic Tac Toe Game
# Jonatan Troche - Author

import os

# clean screen
os.system("cls")

# Introduction
print("Wellcome to Tic Tac Toe Game")
print("Is a game for two players")
player_1 = input("player 1 name: ")
player_2 = input("Player 2 name: ")
os.system("cls")
print(f"Wellcome {player_1} and {player_2}")
print("Good luck")
print()


# game program
def main():
    player = next_player("")
    board = new_board()
    while not (winner(board) or draw(board)):
        display_board(board)
        make_move(player, board)
    display_board(board)
    print("Finish of the game")
    
# board
def new_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(f"  {board[0]} | {board[1]} | {board[2]}")
    print('  ---------')
    print(f"  {board[3]} | {board[4]} | {board[5]}")
    print('  ---------')
    print(f"  {board[6]} | {board[7]} | {board[8]}")
    print()

# all posible winning combinations
def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

# check if the game is draw
def draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 

def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()