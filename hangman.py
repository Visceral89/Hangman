#Hangman Game

import pygame
import random

pygame.init()

win_height = 600
win_width = 600
win = pygame.display.set_mode((win_width, win_height))

#-------------------#
# Global Variables
#-------------------#

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0 , 0)
green = (0, 255, 0)
blue = (0, 0, 255)
lgt_blue = (128, 255, 255)

# Fonts
btn_font = pygame.font.SysFont("arial", 20)
guess_font = pygame.font.SysFont("monospace", 24)
lost_font = pygame.font.SysFont("arial", 30)

word = ""
buttons = []
guessed = []
hangmanpics = []

limbs = 0

def redraw_game_window():
    global guessed
    global hangmanpics
    global limbs

    #test change for github
    