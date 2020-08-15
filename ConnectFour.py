#!/usr/bin/env python3

from Board import Board
from Player import Player
import random

def print_who_won_or_tie(curr_player, red_player, yellow_player, tie):
    if curr_player == red_player:
        print("Red Player won!")
    elif curr_player == yellow_player:
        print("Yellow Player won!")
    elif tie:
        print("Tie!")

def change_turn(curr_player, red_player, yellow_player):
    if curr_player == red_player:
        curr_player = yellow_player
    elif curr_player == yellow_player:
        curr_player = red_player
    return curr_player
        
def main():
    b = Board(6, 7)
    red_player, yellow_player = Player('R'), Player('Y')

    curr_player = red_player
    game_won, tie = False, False
    max_moves, curr_num_moves = 42, 0

    # keep playing as long there are still open slots and the game is not won
    while not game_won:
        val = curr_player.get_val()
        col = random.randint(0, 6)

        b.make_move(curr_player, col)
        curr_num_moves += 1

        if curr_num_moves >= max_moves:
            tie = True
            break 

        print(b)
        if b.game_is_won(val):
            game_won = True
            break
        
        curr_player = change_turn(curr_player, red_player, yellow_player)         

    print_who_won_or_tie(curr_player, red_player, yellow_player, tie)
    

if __name__ == '__main__':
    main()