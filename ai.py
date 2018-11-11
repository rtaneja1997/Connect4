#ai stuff
import numpy as np
import pygame
import sys
import math
import random
import connect4
from connect4 import *

def play_random():
	col = random.randint(0, COLUMN_COUNT-1)

	if is_valid_location(board, col):
		row = get_next_open_row(board, col)
		drop_piece(board, row, col, 2)

		if winning_move(board, 2):
			label = myfont.render("Player 2 wins!!", 1, YELLOW)
			screen.blit(label, (40,10))
			game_over = True