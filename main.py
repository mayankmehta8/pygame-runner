from ast import Pass
from multiprocessing import Event
import pygame
from sys import exit

game= pygame
game.init()
game.display.set_caption("Runner")
screen = game.display.set_mode((800,400))
while True:
    for event in game.event.get():
        if event == game.QUIT:
            game.quit()
            exit()
    game.display.update()