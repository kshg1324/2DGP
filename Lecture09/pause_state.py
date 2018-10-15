import random
import json
import os

from pico2d import *

import game_framework
import main_state



name = "PauseState"

boy = None
grass = None
font = None



class Pause:
    def __init__(self):
        self.image = load_image('pause.png')

    def draw(self):
        self.image.draw(400, 300)

def enter():
    global pause
    pause = Pause()

def exit():
    global pause
    del(pause)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.pop_state()


def update():
    pass


def draw():
    clear_canvas()
    pause.draw()
    update_canvas()





