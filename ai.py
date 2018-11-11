#ai stuff
import numpy as np
import pygame
import sys
import math
import random
import connect4
from connect4 import *

def play_random(column):
    col = random.randint(0, column-1)
    return col


