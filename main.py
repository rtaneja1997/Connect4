#runs the game based on given game mode 

import numpy as np
import pygame
import sys
import math
import connect4 
from connect4 import * 

game_type=input("Choose a game type among the following: minimax, minimax_ab, random\n") 
while game_type.lower() not in ['minimax', 'minimax_ab', 'random']: 
	game_type=input("Please pick a correct game type\n")
play_game(game_type.lower())

