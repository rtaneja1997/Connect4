"""allows user to choose mode of gameplay. If a minimax variant is chosen, user can set the depth of the AI. """

import numpy as np
import pygame
import sys
import math
import connect4 
import ai 
from connect4 import * 

def isInteger(string): 
	try: 
		return int(string) 
	except: 
		return False 

#prompt user to pick a game mode 
game_type=input("Choose a game type among the following: minimax, minimax_ab, random\n") 
while game_type.lower() not in ['minimax', 'minimax_ab', 'random']: 
	game_type=input("Please pick a correct game type\n")

#allow user to set depth of AI for minimax modes 
if game_type.lower() in ['minimax', 'minimax_ab']: 
	depth_value=input("Choose a depth value. The recommended range is 1 to 5 for minimax and 1 to 15 for minimax_ab\n") 
	while not isInteger(depth_value): 
		depth_value=input("Please pick a valid integer greater than or equal to 1\n") 
	ai.DEPTH=int(depth_value) 

play_game(game_type.lower())
