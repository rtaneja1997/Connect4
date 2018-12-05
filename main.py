
#runs the game

"""allows user to choose mode of gameplay. If a minimax variant is chosen, user can set the depth of the AI. """


import numpy as np
import pygame
import sys
import math

import connect4
from connect4 import *
import ai
def displayText(screen):
    myfont = pygame.font.SysFont("monospace", 30)
    text = ["Welcome to Connect 4!","Type in the depth of the AI in the box",
    "Recommended range is 1-5 for minimax and 1-15 for minimax_ab","",
    "Press 1 for player vs. random", "Press 2 for player vs. AI"
    ,"Press 3 for AI vs. random", "Press 4 for random vs. AI","Press 5 for AI vs. AI",
    "Press 6 for Automated AI vs. Random", "Press 7 for Automated Random vs. AI",
    "Press 8 for Automated AI vs. AI", "Press 9 for Player vs. Minimax Alpha Beta"]
    label = []
    for line in text:
        label.append(myfont.render(line, 1, (255,255,255)))
    for line in range(len(label)):
        screen.blit(label[line], (40,10 +(line*30+(15*line))))
    pygame.display.update()

def main():
    SQUARESIZE = 100
    RADIUS = int(SQUARESIZE/2 - 5)
    ROW_COUNT = 6
    COLUMN_COUNT = 7
    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT+1) * SQUARESIZE
    size = (width, height)
    pygame.init()
    screen = pygame.display.set_mode(size)
    myfont = pygame.font.SysFont("monospace", 30)

    color_inactive = pygame.Color('white')
    color_active = pygame.Color('red')
    color = color_inactive
    active = False
    text = ''
    #pygame.draw.rect(screen, (255,255,255), input_box, 2)

    pygame.display.update()

    waitStart =True
    ai.DEPTH=int(4)
    while(waitStart):
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        try:
                            ai.DEPTH=int(text)
                            text = 'Depth has been submitted'
                            txt_surface = myfont.render(text, True, color)
                            pygame.display.update()
                        except:
                            text = 'Please input an integer'
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                        print(text)
                    else:
                        text += event.unicode
                    pygame.display.update()
                else:
                    if event.key == pygame.K_1:
                        waitStart = False
                        print(play_game("human_vs_random"))
                    elif event.key == pygame.K_2:
                        print(play_game("human_vs_ai"))
                        waitStart = False
                    elif event.key == pygame.K_3:
                        print(play_game("ai_vs_random"))
                        waitStart = False
                    elif event.key == pygame.K_4:
                        print(play_game("random_vs_ai"))
                        waitStart = False
                    elif event.key == pygame.K_5:
                        print(play_game("ai_vs_ai"))
                        waitStart = False
                    elif event.key == pygame.K_6:
                        for i in range(10):
                            print(play_game("auto_ai_vs_random"))
                        waitStart = False
                    elif event.key == pygame.K_7:
                        for i in range(10):
                            print(play_game("auto_random_vs_ai"))
                        waitStart = False
                    elif event.key == pygame.K_8:
                        for i in range(10):
                            print(play_game("auto_ai_vs_ai"))
                        waitStart = False
                    elif event.key == pygame.K_9:
                        print(play_game("minimax_ab"))
                        waitStart = False
            elif event.type == pygame.QUIT:
                sys.exit()
            screen.fill((0, 0, 0))
            displayText(screen)
            input_box = pygame.Rect(100, 130, 50, 32)
            txt_surface = myfont.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            # Blit the text.
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.update()

if __name__ == "__main__": main()

# import connect4
# import ai
# from connect4 import *
#
# def isInteger(string):
# 	try:
# 		return int(string)
# 	except:
# 		return False
#
# #prompt user to pick a game mode
# game_type=input("Choose a game type among the following: minimax, minimax_ab, random\n")
# while game_type.lower() not in ['minimax', 'minimax_ab', 'random']:
# 	game_type=input("Please pick a correct game type\n")
#
# #allow user to set depth of AI for minimax modes
# if game_type.lower() in ['minimax', 'minimax_ab']:
# 	depth_value=input("Choose a depth value. The recommended range is 1 to 5 for minimax and 1 to 15 for minimax_ab\n")
# 	while not isInteger(depth_value):
# 		depth_value=input("Please pick a valid integer greater than or equal to 1\n")
# 	ai.DEPTH=int(depth_value)
#
# play_game(game_type.lower())
# >>>>>>> 3f31cfa7f8a153353165645081209134822f8a1d
