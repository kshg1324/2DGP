import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state


name = "MainState"

boy = None
floor = None
burner = None
refrig = None
sink = None
cabinet = None
kitchen_floor = None
font = None
logo_time = 0.0


class Floor:
    def __init__(self):
        self.image = load_image('floor.png')

    def draw(self):
        for i in range(8):
            for j in range(3):
                self.image.draw(50 + 100 * i, 50 + 100 * j)

class Kitchen_Floor:
    def __init__(self):
        self.image = load_image('floor3.png')

    def draw(self):
        for i in range(8):
            self.image.draw(50 + 100 * i, 50 + 100 * 3)

class Burner:
    def __init__(self):
        self.image1 = load_image('burner.png')
        self.image2 = load_image('stove.png')
    def draw(self):
        self.image1.draw(50 + 100 * 4, 25 + 100 * 4)
        self.image2.draw(50 + 100 * 4, 75 + 100 * 4)

class Refrig:
    def __init__(self):
        self.image1 = load_image('refrig.png')
        self.image2 = load_image('mini_refrig.png')
    def draw(self):
        self.image1.draw(50 + 100 * 2, 50 + 100 * 4)
        self.image2.draw(25 + 100 * 5, 50 + 100 * 4)
        self.image2.draw(75 + 100 * 5, 50 + 100 * 4)

class Sink:
    def __init__(self):
        self.image1 = load_image('cabinet2_under.png')
        self.image2 = load_image('sink.png')

    def draw(self):
        self.image1.draw(50 + 100 * 3, 25 + 100 * 4)
        self.image2.draw(50 + 100 * 3, 75 + 100 * 4)

class Cabinet:
    def __init__(self):
        self.image1 = load_image('cabinet2_under.png')
        self.image2 = load_image('cabinet2_above.png')
    def draw(self):
        for i in range(2):
            self.image1.draw(50 + 100 * i, 25 + 100 * 4)
            self.image2.draw(50 + 100 * i, 75 + 100 * 4)
        self.image1.draw(50 + 100 * 6, 25 + 100 * 4)
        self.image2.draw(50 + 100 * 6, 75 + 100 * 4)
        self.image1.draw(50 + 100 * 7, 25 + 100 * 4)
        self.image2.draw(50 + 100 * 7, 75 + 100 * 4)

class Wall:
    def __init__(self):
        self.image1 = load_image('wall_under.png')
        self.image2 = load_image('wall_above.png')

    def draw(self):
        for i in range(8):
            self.image1.draw(50 + 100 * i, 12.5 + 100 * 3)
            self.image2.draw(50 + 100 * i, 37.5 + 100 * 3)



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


def enter():
    global boy, floor, burner, refrig, sink, cabinet, kitchen_floor, wall
    boy = Boy()
    floor = Floor()
    burner = Burner()
    refrig = Refrig()
    sink = Sink()
    kitchen_floor = Kitchen_Floor()
    cabinet = Cabinet()
    wall = Wall()
def exit():
    global boy, floor, burner, refrig, sink, cabinet, kitchen_floor, wall
    del(boy)
    del(floor)
    del(burner)
    del(refrig)
    del(sink)
    del(cabinet)
    del(wall)

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.push_state(pause_state)


def update():
    boy.update()


def draw():
    clear_canvas()
    floor.draw()
    burner.draw()
    refrig.draw()
    sink.draw()
    cabinet.draw()
    kitchen_floor.draw()
    wall.draw()
    boy.draw()
    update_canvas()





