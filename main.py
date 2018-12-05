#runs the game

import numpy as np
import pygame
import sys
import math
import connect4
from connect4 import *

def displayText(screen):
    myfont = pygame.font.SysFont("monospace", 30)
    text = ["Welcome to Connect 4!","Press 1 for player vs. random", "Press 2 for player vs. AI"
    ,"Press 3 for AI vs. random", "Press 4 for random vs. AI","Press 5 for AI vs. AI",
    "Press 6 for Automated AI vs. Random", "Press 7 for Automated Random vs. AI",
    "Press 8 for Automated AI vs. AI"]
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
    displayText(screen)
    pygame.display.update()

    waitStart =True
    while(waitStart):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
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
            elif event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__": main()
