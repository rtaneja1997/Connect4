#ai stuff
import numpy as np
import pygame
import sys
import math
import random
import connect4
import copy
from connect4 import *


#DEPTH=None #initialized by player
INFINITY=100000000000000

#CLASSES
class MoveInfo(object):
	"""Keeps track of a move and its minimax value"""
	def __init__(self, score, move=None):
		self.move=move
		self.score=score

	def __str__(self):

		return "Playing column " + str(self.move) + " has value " + str(self.score)

	def __repr__(self):

		return self.__str__()

#FUNCTIONS FOR PLAYING
def play_random(column):
	"""Randomly chooses open column"""
	col=random.randint(0, column-1)
	return col

def play_smart(board,depth):
	"""uses minimax to play game """
	best_move=minimax(board,1, depth)
	return best_move.move

def play_genius(board,depth):
	"""uses alpha-beta version of minimax to play game """


	best_move=alphabeta(board, 1, depth,-INFINITY,INFINITY)
	return best_move.move



#HELPER FUNCTIONS

def winning_board(board, player):
	"""returns true if the player wins the game
	four pieces in a row
	four pieces in a column
	four pieces diagonally aligned"""
	return has_winning_row(board,player) or has_winning_column(board,player) or has_winning_diag(board, player)


def has_winning_row(board,player):
	"""returns true if player wins a row, false otherwise """
	num_rows=len(board)
	num_cols=len(board[0])
	for row in range(num_rows):
		if four_consecutive(board[row], player):
			return True
	return False

def has_winning_column(board, player):
	"""returns true if player wins a column, false otherwise"""
	num_rows=len(board)
	num_cols=len(board[0])
	for col in range(num_cols):
		current_column=[]
		for row in range(num_rows):
			current_column.append(board[row][col])
		if four_consecutive(current_column, player):
			return True
	return False

def has_winning_diag(board, player):
	"""returns true if a player wins a diagonal, false otherwise"""
	num_rows=len(board)
	num_cols=len(board[0])

	#positively sloped diagonals
	for c in range(num_cols-3):
		for r in range(num_rows-3):
			if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
				return True

	# Check negatively sloped diaganols
	for c in range(num_cols-3):
		for r in range(3, num_rows):
			if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
				return True



def four_consecutive(row, player):
	"""Returns true if player has four consecutive pieces aligned, false otherwise """
	curr_col=0
	while curr_col<len(row)-3:
		is_consecutive=(row[curr_col]==player) and (row[curr_col]==row[curr_col+1]==row[curr_col+2]==row[curr_col+3])
		if is_consecutive:
			return True
		curr_col+=1

	return False



def board_evaluation(board,possible_moves,turn):
	"""evaluation function over a board"""
	eval = 0
	for m in possible_moves:
		row = connect4.get_next_open_row(board, m)
		#print("row" + str(row))
		if (row - 3 >=0):
			if board[row-1][m] == board[row-2][m] == board[row-3][m]:
				if (board[row-1][m] == 2):
					if (turn == 1):
						eval += 0.03
					else:
						eval -= 0.03
				elif(board[row-1][m] == 1):
					if (turn == 1):
						eval -= 0.03
					else:
						eval += 0.03
			elif board[row-1][m] == board[row-1][m] :
				if (board[row-1][m] == 2):
					if (turn == 1):
						eval += 0.003
					else:
						eval -= 0.003
				elif(board[row-1][m] == 1):
					if (turn == 1):
						eval -= 0.003
					else:
						eval += 0.003
		elif (row - 2 >=0):
			if board[row-1][m] == board[row-1][m] :
				if (board[row-1][m] == 2):
					eval += 0.003
				elif(board[row-1][m] == 1):
					eval -= 0.003
		colStart = max(m-3,0)
		colEnd = min(m, connect4.COLUMN_COUNT-4)
		toThree = {}
		toTwo = {}
		if (turn == 1):
			toThree = {2:1,1:-1,0:0}
			toTwo = {2:4,1:-1,0:0}
		else:
			toThree = {2:1,1:-1,0:0}
			toTwo = {2:4,1:-1,0:0}

		for i in range(colStart, colEnd+1):
			count3 = toThree[board[row][i]]+toThree[board[row][i+1]]
			+toThree[board[row][i+2]]+ toThree[board[row][i+3]]
			#print("count3 " + str(count3))
			#print("r" +str(toThree[board[row][i]])+str(toThree[board[row][i+1]])
			#+str(toThree[board[row][i+2]])+ str(toThree[board[row][i+3]]))
			if (count3 == 3):
				eval += 0.03
			elif (count3 == -3):
				eval -= 0.03
		for i in range(colStart, colEnd+1):
			count2 = toTwo[board[row][i]]+toTwo[board[row][i+1]]
			+toTwo[board[row][i+2]]+ toTwo[board[row][i+3]]
			if (count2 == 8):
				eval += 0.003
			elif (count2 == -2):
				eval -= 0.003
		rowStart = max(row - 3, 0)
		rowEnd = min(row, connect4.ROW_COUNT-4)
		diagPosStart = max(rowStart - row,colStart - m)
		diagPosEnd = min(rowEnd - row, colEnd - m)
		for i in range(diagPosStart, diagPosEnd):
			count3 = toThree[board[row+i][m+i]]+toThree[board[row+i+1][m+i+1]]
			+toThree[board[row+i+2][m+i+2]]+ toThree[board[row+i+3][m+i+3]]
			if (count3 == 3):
				eval += 0.03
			elif (count3 == -3):
				eval -= 0.03
		for i in range(diagPosStart, diagPosEnd):
			count2 = toTwo[board[row+i][m+i]]+toTwo[board[row+i+1][m+i+1]]
			+toTwo[board[row+i+2][m+i+2]]+ toTwo[board[row+i+3][m+i+3]]
			if (count2 == 8):
				eval += 0.003
			elif (count2 == -2):
				eval -= 0.003
		# Check negatively sloped diaganols
		diagPosStart = max(row - rowEnd,colStart - m)
		diagPosEnd = min(row - rowStart, colEnd - m)
		for i in range(diagPosStart, diagPosEnd):
			count3 = toThree[board[row-i][m+i]]+toThree[board[row-(i+1)][m+i+1]]
			+toThree[board[row-(i+2)][m+i+2]]+ toThree[board[row-(i+3)][m+i+3]]
			if (count3 == 3):
				eval += 0.03
			elif (count3 == -3):
				eval -= 0.03
		for i in range(diagPosStart, diagPosEnd):
			count2 = toTwo[board[row-i][m+i]]+toTwo[board[row-(i+1)][m+i+1]]
			+toTwo[board[row-(i+2)][m+i+2]]+ toTwo[board[row-(i+3)][m+i+3]]
			if (count2 == 3):
				eval += 0.003
			elif (count2 == -3):
				eval -= 0.003
	return eval

#ACTUAL MINIMAX LOGIC
def get_possible_moves(board):
	"""gets available moves for given board """
	poss_moves = []
	num_cols=len(board[0])
	for col in range(num_cols):
		if connect4.is_valid_location(board,col):
			poss_moves.append(col)
	"""print (poss_moves)"""
	return poss_moves


def minimax(board, turn, depth):
	"""performs minimax algorithm on board bounded by [depth] value given """

	possible_moves=get_possible_moves(board)

	#Case 1: board is a winning state for human
	if winning_board(board,1):
		return MoveInfo(-1)

	#Case 2: board is a winning state for ai
	elif winning_board(board,2):
	    return MoveInfo(1)

    #Case 3: tie
	elif possible_moves==[]:
		return MoveInfo(0)

	elif depth==0:
		return MoveInfo(board_evaluation(board, possible_moves, turn))

	move_information=[] #keeps track of minimax values for moves

	for move in possible_moves:

		#get board generated by playing move
		if turn==0:
			piece_type=1
		else:
			piece_type=2

		new_board=copy.deepcopy(board)
		row=connect4.get_next_open_row(new_board, move)
		connect4.drop_piece(new_board, row, move, piece_type)

		#minimax on board
		move_info=minimax(new_board, (turn+1)%2, depth-1)
		move_info.move=move

		#track move information
		move_information.append(move_info)

	#maximize score for ai

	if turn==1:
		bestScore=-10000
		curr_idx=0
		best_idx=0
		while curr_idx<len(move_information):
			#print(turn)
			#print(move_information[curr_idx])
			if move_information[curr_idx].score>bestScore:
				bestScore=move_information[curr_idx].score
				best_idx=curr_idx
			elif move_information[curr_idx].score==bestScore:
				new_best = random.randint(0,1)
				if (new_best == 1):
					best_idx=curr_idx
			curr_idx+=1
		return move_information[best_idx]

	#minimize score for human
	bestScore=10000
	curr_idx=0
	best_idx=0
	while curr_idx<len(move_information):
		#print(turn)
		#print(move_information[curr_idx])
		if move_information[curr_idx].score<bestScore:
			bestScore=move_information[curr_idx].score
			best_idx=curr_idx
		elif move_information[curr_idx].score==bestScore:
			new_best = random.randint(0,1)
			if (new_best == 1):
				best_idx=curr_idx
		curr_idx+=1
	return move_information[best_idx]



def alphabeta(board, turn, depth, a, b):

	possible_moves=get_possible_moves(board)

	#TERMINAL CASES 
	#Case 1: board is a winning state for human
	if winning_board(board,1):
		return MoveInfo(-1)

	#Case 2: board is a winning state for ai
	elif winning_board(board,2):
	    return MoveInfo(1)

    #Case 3: tie
	elif possible_moves==[] or depth==0:
		return MoveInfo(board_evaluation(board, possible_moves, turn)) 


	#search for move 
	best_move=None 
	value= -INFINITY if turn==1 else INFINITY 

	for move in possible_moves: 
		piece_type=turn+1 

		new_board=copy.deepcopy(board) 
		row=connect4.get_next_open_row(new_board,move) 
		connect4.drop_piece(new_board,row,move,piece_type) 

		child=alphabeta(new_board,(turn+1)%2, depth-1, a, b) 
		if (child.score>value and turn==1) or (child.score<value and turn!=1):  
			best_move=move 
			value=child.score 

		if turn==1: 
			a=max(a,value) 

		if turn!=1: 
			b=min(b,value) 

		if a>=b: 
			break 
	return MoveInfo(value, best_move)



	
