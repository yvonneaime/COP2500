# Yvonne Aime, COP2500, July 12 2023
#Left / Right Game

import random

def print_board(b):
    print("Board.")
    for i in range(len(b)):
        print(b[i], end=" ")

def main():
    board = []
    for i in range(8):
        num = random.randint(1, 10)
        board.apend(num)
    
    print_board(board)
    turn = 0 
    while(len(board)>0):
        print("It is player #", turn %2, "turn")
        side = input("Would you like the left or right side?\n")
        if(side == "left"):
            if(turn %2 == 0):
                kyle_score += board[0]
                board.pop(0)
                turn += 1
            else:
                class_score += board[0]
                board.pop(0)
                turn += 1
        elif(side == "right"):
             if(turn %2 == 0):
                kyle_score += board[-1]
                board.pop(-1)
                turn += 1
main()