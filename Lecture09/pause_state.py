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

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('animation_sheet.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        if(self.dir == 1):
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        elif(self.dir == -1):
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Pause:
    def __init__(self):
        self.image = load_image('pause.png')

    def draw(self):
        self.image.draw(400, 300)

def enter():
    global grass, boy, pause
    grass = Grass()
    boy = Boy()
    pause = Pause()

def exit():
    global grass, boy, pause
    del(grass)
    del(boy)
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
    grass.draw()
    boy.draw()
    pause.draw()
    update_canvas()





