"""Module for data structures for game as well as creating GUI.
Citation: We got this module from the github repo of https://github.com/KeithGalli/Connect4-Python/blob/master/connect4.py, a public 
Connect4 game implementation

We made changes to the source code to allow the game logic to account for multiple modes of gameplay as well as an AI player
"""


import numpy as np
import pygame
import sys
import math
import random
import ai
from ai import *

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)

AI_TURN=0
PLAYER_TURN=1
AI_PIECE=2
PLAYER_PIECE=3
AI1_DEPTH = None
AI2_DEPTH = None

ROW_COUNT = 6
COLUMN_COUNT = 7
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

def create_board():
	#board = np.zeros([ROW_COUNT, COLUMN_COUNT])
	board=[[0 for i in range(COLUMN_COUNT)] for j in range(ROW_COUNT)]
	return board

def drop_piece(board, row, col, piece):
	board[row][col] = piece

def is_valid_location(board, col):
	return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):

	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r

#def print_board(board):
	#print (np.flip(board))
	#print ("ignore")

def winning_move(board, piece):
	# Check horizontal locations for win
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check positively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

def draw_board(board, screen):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			if board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2:
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()

def play_game(mode):
	mode = mode;
	board = create_board()
	#print_board(board)
	game_over = False
	to_game_over = False
	turn = 0
	winner = -1

	pygame.init()

	size = (width, height)

	screen = pygame.display.set_mode(size)
	draw_board(board, screen)
	pygame.display.update()

	myfont = pygame.font.SysFont("monospace", 50)
	if( mode == "auto_ai_vs_ai" or mode == "auto_ai_vs_random" or mode == "auto_random_vs_ai"
		or mode == "auto_random_vs_ab" or mode == "auto_ai_vs_ab" or mode == "auto_ab_vs_ab"):
		while not game_over:
			if turn == 0:
				if (mode == "auto_random_vs_ai" or mode == "auto_random_vs_ab") :
					col = play_random(COLUMN_COUNT)
					if is_valid_location(board, col):
						row = get_next_open_row(board, col)
						drop_piece(board, row, col, 1)
				elif (mode == "auto_ab_vs_ab"):

					#make move
					col=play_genius(board, AI1_DEPTH)
					if col is None:
						if (get_next_open_row(board, col) != None):
							winner = 2
						else:
							winner = 0
						label = myfont.render("Player 2 wins!! Press any key to exit.", 1, RED)
						screen.blit(label, (40,10))
						game_over = True
						break
					row=get_next_open_row(board, col)
					drop_piece(board,row,col,1)

				else:
					col=play_smart(board,AI1_DEPTH)
					if col is None:
						for col in range(COLUMN_COUNT ):
							if (get_next_open_row(board, col) != None):
								winner = 2
							else:
								winner = 0
						label = myfont.render("Tie!! Press any key to exit.", 1, RED)
						screen.blit(label, (40,10))
						break
					row=get_next_open_row(board, col)
					drop_piece(board,row,col,1)

				if winning_move(board, 1):
					game_over = True
					label = myfont.render("Player 1 wins!! Press any key to exit", 1, RED)
					screen.blit(label, (40,10))
					winner = 1



			# # Ask for Player 2 Input
			else:

				turn += 1
				turn = turn % 2
			if( not game_over):
				if (mode == "auto_ai_vs_random"):

					col = play_random(COLUMN_COUNT)
					if is_valid_location(board, col):
						row = get_next_open_row(board, col)
						drop_piece(board, row, col, 2)

					if winning_move(board, 2):
						game_over = True #ai stuff
						label = myfont.render("Player 2 wins!! Press any key to exit", 1, YELLOW)
						#time.sleep(1)
						screen.blit(label, (40,10))
						winner = 2

				elif (mode == "auto_ai_vs_ai" or mode == "auto_random_vs_ai"):

					#make move
					col=play_smart(board,AI2_DEPTH)
					if col is None:
						if (get_next_open_row(board, col) != None):
							winner = 1
						else:
							winner = 0
						label = myfont.render("Tie!! Press any key to exit.", 1, RED)
						screen.blit(label, (40,10))
						break

					row=get_next_open_row(board, col)
					drop_piece(board,row,col,2)

					#check for win
					if winning_move(board,2):
						game_over = True
						label = myfont.render("Player 2 wins!! Press any key to exit.", 1, YELLOW)
						screen.blit(label, (40,10))
						winner = 2
				elif (mode == "auto_ab_vs_ab" or mode == "auto_ai_vs_ab" or mode == "auto_random_vs_ab"):
					col=play_genius(board, AI2_DEPTH)
					if col is None:
						if (get_next_open_row(board, col) != None):
							winner = 1
						else:
							winner = 0
						label = myfont.render("Player 1 wins!! Press any key to exit.", 1, RED)
						screen.blit(label, (40,10))
						break
					row=get_next_open_row(board, col)
					drop_piece(board,row,col,2)

					if winning_move(board,2):
						to_game_over = True
						label = myfont.render("Player 2 wins!! Press any key to exit.", 1, YELLOW)
						screen.blit(label, (40,10))
						winner = 2

			#print_board(board)
			draw_board(board, screen)


	else:
		while not game_over:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.MOUSEMOTION:
					pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
					posx = event.pos[0]
					if turn == 0:
						pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
					else:
						pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
				pygame.display.update()

				if event.type == pygame.MOUSEBUTTONDOWN:
					pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
					#print(event.pos)
					# Ask for Player 1 Input
					if turn == 0:
						if (mode == "human_vs_random" or mode == "human_vs_ai" or mode == "human_vs_ab") and not game_over:
							posx = event.pos[0]
							col = int(math.floor(posx/SQUARESIZE))

							if is_valid_location(board, col):
								row = get_next_open_row(board, col)
								drop_piece(board, row, col, 1)

						elif (mode == "random_vs_ai" and not game_over):
							col = play_random(COLUMN_COUNT)
							if is_valid_location(board, col):
								row = get_next_open_row(board, col)
								drop_piece(board, row, col, 1)
						else:
							col=play_smart(board, AI1_DEPTH)
							row=get_next_open_row(board, col)
							drop_piece(board,row,col,1)

						if winning_move(board, 1):
							label = myfont.render("Player 1 wins!! Press any key to exit", 1, RED)
							#time.sleep(1)
							screen.blit(label, (40,10))
							winner = 1
							to_game_over = True


					# # Ask for Player 2 Input
					else:
						if (mode == "human"):
							posx = event.pos[0]
							col = int(math.floor(posx/SQUARESIZE))

							if is_valid_location(board, col):
								row = get_next_open_row(board, col)
								drop_piece(board, row, col, 2)

								if winning_move(board, 2):
									label = myfont.render("Player 2 wins!! Press any key to exit", 1, YELLOW)
									#time.sleep(1)
									screen.blit(label, (40,10))
									winner = 2
									to_game_over = True

							turn += 1
							turn = turn % 2
					if not to_game_over and not game_over:
						if (mode == "human_vs_random" or mode == "ai_vs_random"):

							col = play_random(COLUMN_COUNT)
							if is_valid_location(board, col):
								row = get_next_open_row(board, col)
								drop_piece(board, row, col, 2)

							if winning_move(board, 2):
								to_game_over = True #ai stuff
								label = myfont.render("Player 2 wins!! Press any key to exit", 1, YELLOW)
								#time.sleep(1)
								screen.blit(label, (40,10))
								winner = 2

						if (mode == "human_vs_ai" or mode == "ai_vs_ai" or mode == "random_vs_ai") and not game_over:
							#make move
							col=play_smart(board, AI2_DEPTH)
							print ("AI is choosing column " + str(col))
							row=get_next_open_row(board, col)
							drop_piece(board,row,col,2)

							#check for win
							if winning_move(board,2):
								to_game_over = True
								label = myfont.render("Player 2 wins!! Press any key to exit.", 1, YELLOW)
								screen.blit(label, (40,10))
								winner = 2
						if (mode == "human_vs_ab") and not game_over:

							#make move
							col=play_genius(board, AI2_DEPTH)
							if col is None:
								if (get_next_open_row(board, col) != None):
									winner = 1
								else:
									winner = 0
								label = myfont.render("Player 1 wins!! Press any key to exit.", 1, RED)
								screen.blit(label, (40,10))
								break
							row=get_next_open_row(board, col)
							drop_piece(board,row,col,2)

							if winning_move(board,2):
								to_game_over = True
								label = myfont.render("Player 2 wins!! Press any key to exit.", 1, YELLOW)
								screen.blit(label, (40,10))
								winner = 2


					#print_board(board)
					draw_board(board, screen)

					if to_game_over:
						waitExit = True
						while(waitExit):
							for event in pygame.event.get():
								if (event.type == pygame.KEYDOWN or event.type == pygame.QUIT):
									waitExit = False
						game_over = True
						#label=myfont.render("Player 2 wins!!", 1, YELLOW)

						#screen.blit(label, (40,10))

						#pygame.time.wait(3000)
	return winner
