import random
import json
import os

from pico2d import *

import game_framework
import title_state
import cooking_1_state
import cooking_2_state
import cooking_3_state
import cooking_4_state
import cooking_5_state
import cooking_6_state
import time
import random
import pause_state


name = "MainState"

boy = None
floor = None
burner = None
refrig = None
sink = None
cabinet = None
kitchen_floor = None
frame = None
font = None
customer = None
Money = 100
Left_time = 300
life = 3
food_1_stack = 0
food_2_stack = 0
food_3_stack = 0
food_4_stack = 0
food_5_stack = 0
food_6_stack = 0

Table_1 = 0
Table_2 = 0
Table_3 = 0
Table_4 = 0
Table_5 = 0
Table_6 = 0

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

timer = 0.0
customer_frame = 0
frame_time = 0.0

def run(start_state):
    global running, stack
    running = True
    stack = [start_state]
    start_state.enter()

    global frame_time
    current_time = time.time()
    while (running):
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()
        frame_time = time.time() - current_time
        #frame_rate = 1.0 / frame_time
        current_time += frame_time

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

class Frame:
    def __init__(self):
        global Money
        self.image1 = load_image('frame2.png')
        self.image2 = load_image('menu.png')
        self.image3 = load_image('life_3.png')
        self.image4 = load_image('life_2.png')
        self.image5 = load_image('life_1.png')
        self.image6 = load_image('life_0.png')
        self.image7 = load_image('life.png')
        self.image8 = load_image('clock.png')
        self.image9 = load_image('money.png')
        self.font = load_font('ENCR10B.TTF', 16)

    def draw(self):

        self.image2.clip_draw(100 * 0, 100 * 6, 100, 100 , 50 + 100 * 0, 50 + 100 * 5)
        self.image2.clip_draw(100 * 0, 100 * 0, 100, 100 , 50 + 100 * 1, 50 + 100 * 5)
        self.image2.clip_draw(100 * 5, 100 * 4, 100, 100 , 50 + 100 * 2, 50 + 100 * 5)
        self.image2.clip_draw(100 * 2, 100 * 3, 100, 100 , 50 + 100 * 3, 50 + 100 * 5)
        self.image2.clip_draw(100 * 2, 100 * 5, 100, 100 , 50 + 100 * 4, 50 + 100 * 5)
        self.image2.clip_draw(100 * 2, 100 * 4, 100, 100 , 50 + 100 * 5, 50 + 100 * 5)
        if life == 3:
            self.image3.draw(50 + 100 * 7 - 5, 16.5 + 100 * 5 + 5)
        elif life == 2:
            self.image4.draw(50 + 100 * 7 - 5, 16.5 + 100 * 5 + 5)
        elif life == 1:
            self.image5.draw(50 + 100 * 7 - 5, 16.5 + 100 * 5 + 5)
        #self.image3.draw(50 + 100 * 7 - 5, 16.5 + 100 * 5 + 5)
        self.image7.draw(50 + 100 * 6 - 5, 16.5 + 100 * 5 )
        self.image8.draw(50 + 100 * 6 - 5, 49.5 + 100 * 5 )
        self.image9.draw(50 + 100 * 6 - 5, 82.5 + 100 * 5 )
        self.image1.draw(100 * 4, 50 + 100 * 5)
        self.font.draw(25 + 100 * 7 -10,  49.5 + 100 * 5 , '(%3.2f)' % (get_time()), (0, 0, 0))
        self.font.draw(25 + 100 * 7 - 10, 82.5  + 100 * 5 , '(%3.2f)' % (Money), (0, 0, 0))

        self.font.draw(50 + 100 * 0 + 20, 50 + 100 * 5 - 30 , '(%d)' % (food_1_stack), (0, 0, 0))
        self.font.draw(50 + 100 * 1 + 20, 50 + 100 * 5 - 30, '(%d)' % (food_2_stack), (0, 0, 0))
        self.font.draw(50 + 100 * 2 + 20, 50 + 100 * 5 - 30, '(%d)' % (food_3_stack), (0, 0, 0))
        self.font.draw(50 + 100 * 3 + 20, 50 + 100 * 5 - 30, '(%d)' % (food_4_stack), (0, 0, 0))
        self.font.draw(50 + 100 * 4 + 20, 50 + 100 * 5 - 30, '(%d)' % (food_5_stack), (0, 0, 0))
        self.font.draw(50 + 100 * 5 + 20, 50 + 100 * 5 - 30, '(%d)' % (food_6_stack), (0, 0, 0))
        #self.image1.draw(100 * 4, 50 + 100 * 5)
        #self.image1.draw(100 * 4, 50 + 100 * 5)
        #character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)

class Table:
    def __init__(self):
        self.image = load_image('table.png')

    def draw(self):
        for i in range(3):
            for j in range(2):
                self.image.draw(100 + 300 * i, 75 + 150 * j)
class Customer:
    def __init__(self):
        self.image = load_image('animation_sheet.png')
        #self.customer_frame = 0
    def draw(self):
        #self.customer_frame = (self.customer_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * frame_time) % FRAMES_PER_ACTION
        global customer_frame, timer,Table_1,Table_2,Table_3,Table_4,Table_5,Table_6
        customer_frame = (customer_frame + 0.05) % 8
        if (Table_1 == 1):
            self.image.clip_draw(int(customer_frame) * 100, 100, 100, 100, 100 + 300 * 0, 150 + 150 * 0)
        if (Table_2 == 1):
            self.image.clip_draw(int(customer_frame) * 100, 100, 100, 100, 100 + 300 * 1, 150 + 150 * 0)
        if (Table_3 == 1):
            self.image.clip_draw(int(customer_frame) * 100, 100, 100, 100, 100 + 300 * 2, 150 + 150 * 0)
        if (Table_4 == 1):
            self.image.clip_draw(int(customer_frame) * 100, 100, 100, 100, 100 + 300 * 0, 150 + 150 * 1)
        if (Table_5 == 1):
            self.image.clip_draw(int(customer_frame) * 100, 100, 100, 100, 100 + 300 * 1, 150 + 150 * 1)
        if (Table_6 == 1):
            self.image.clip_draw(int(customer_frame) * 100, 100, 100, 100, 100 + 300 * 2, 150 + 150 * 1)

        if timer < 1000:
            timer = (timer + 1)
        if timer == 1000:
            timer = timer - 1000
            x = random.randint(0,5)
            if(x == 0):
                Table_1 = 1
            if(x == 1):
                Table_2 = 1
            if(x == 2):
                Table_3 = 1
            if(x == 3):
                Table_4 = 1
            if(x == 4):
                Table_5 = 1
            if(x == 5):
                Table_6 = 1


def enter():
    global boy, floor, burner, refrig, sink, cabinet, kitchen_floor, wall, frame, table, customer
    floor = Floor()
    burner = Burner()
    refrig = Refrig()
    sink = Sink()
    kitchen_floor = Kitchen_Floor()
    cabinet = Cabinet()
    wall = Wall()
    frame = Frame()
    table = Table()
    customer = Customer()

def exit():
    global boy, floor, burner, refrig, sink, cabinet, kitchen_floor, wall, frame, table, customer
    del(floor)
    del(burner)
    del(refrig)
    del(sink)
    del (kitchen_floor)
    del(cabinet)
    del(wall)
    del(frame)
    del(table)
    del(customer)
def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        if (event.type == SDL_KEYDOWN) and (event.key == SDLK_q):
            # game_framework.change_state(cooking_state)
            game_framework.push_state(cooking_1_state)
        if (event.type == SDL_KEYDOWN) and (event.key == SDLK_w):
            # game_framework.change_state(cooking_state)
            game_framework.push_state(cooking_2_state)
        if (event.type == SDL_KEYDOWN) and (event.key == SDLK_e):
            # game_framework.change_state(cooking_state)
            game_framework.push_state(cooking_3_state)
        if (event.type == SDL_KEYDOWN) and (event.key == SDLK_r):
            # game_framework.change_state(cooking_state)
            game_framework.push_state(cooking_4_state)
        if (event.type == SDL_KEYDOWN) and (event.key == SDLK_t):
            # game_framework.change_state(cooking_state)
            game_framework.push_state(cooking_5_state)
        if (event.type == SDL_KEYDOWN) and (event.key == SDLK_y):
            # game_framework.change_state(cooking_state)
            game_framework.push_state(cooking_6_state)
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.push_state(pause_state)


def update():
    pass


def draw():

    clear_canvas()
    floor.draw()
    burner.draw()
    refrig.draw()
    sink.draw()
    cabinet.draw()
    kitchen_floor.draw()
    wall.draw()
    frame.draw()
    table.draw()
    customer.draw()
    update_canvas()





