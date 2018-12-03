import random
import json
import os

import game_framework
import main_state
import cooking_state
import start_state
from pico2d import *

name = "Gameover_State"
font = None

gameover_state = 0

class Game_over:
    def __init__(self):
        self.image = load_image('game_over.png')
    def update(self):
        pass
    def draw(self):
        global serving
        self.image.draw(400, 300)


def enter():
    global game_over
    game_over =Game_over()

def exit():
    global game_over
    del(game_over)


def pause():
    pass


def resume():
    pass



def handle_events():
    global serving
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE)):
            main_state.boy = None
            main_state.floor = None
            main_state.burner = None
            main_state.refrig = None
            main_state.sink = None
            main_state.cabinet = None
            main_state.kitchen_floor = None
            main_state.frame = None
            main_state.table = None
            main_state.font = None
            main_state.customer = None
            main_state.messeage = None
            main_state.Money = 100
            main_state.Left_time = 300
            main_state.life = 3
            main_state.x = 0

            main_state.food_1_stack = 0
            main_state.food_2_stack = 0
            main_state.food_3_stack = 0
            main_state.food_4_stack = 0
            main_state.food_5_stack = 0
            main_state.food_6_stack = 0

            main_state.Table_1 = 0
            main_state.Table_2 = 0
            main_state.Table_3 = 0
            main_state.Table_4 = 0
            main_state.Table_5 = 0
            main_state.Table_6 = 0

            main_state.Table_1_order = 0
            main_state.Table_2_order = 0
            main_state.Table_3_order = 0
            main_state.Table_4_order = 0
            main_state.Table_5_order = 0
            main_state.Table_6_order = 0

            main_state.Table_1_orderd_Q = 0
            main_state.Table_1_orderd_W = 0
            main_state.Table_1_orderd_E = 0
            main_state.Table_1_orderd_R = 0
            main_state.Table_1_orderd_T = 0
            main_state.Table_1_orderd_Y = 0

            main_state.Table_2_orderd_Q = 0
            main_state.Table_2_orderd_W = 0
            main_state.Table_2_orderd_E = 0
            main_state.Table_2_orderd_R = 0
            main_state.Table_2_orderd_T = 0
            main_state.Table_2_orderd_Y = 0

            main_state.Table_3_orderd_Q = 0
            main_state.Table_3_orderd_W = 0
            main_state.Table_3_orderd_E = 0
            main_state.Table_3_orderd_R = 0
            main_state.Table_3_orderd_T = 0
            main_state.Table_3_orderd_Y = 0

            main_state.Table_4_orderd_Q = 0
            main_state.Table_4_orderd_W = 0
            main_state.Table_4_orderd_E = 0
            main_state.Table_4_orderd_R = 0
            main_state.Table_4_orderd_T = 0
            main_state.Table_4_orderd_Y = 0

            main_state.Table_5_orderd_Q = 0
            main_state.Table_5_orderd_W = 0
            main_state.Table_5_orderd_E = 0
            main_state.Table_5_orderd_R = 0
            main_state.Table_5_orderd_T = 0
            main_state.Table_5_orderd_Y = 0

            main_state.Table_6_orderd_Q = 0
            main_state.Table_6_orderd_W = 0
            main_state.Table_6_orderd_E = 0
            main_state.Table_6_orderd_R = 0
            main_state.Table_6_orderd_T = 0
            main_state.Table_6_orderd_Y = 0

            main_state.time_literal = 0
            main_state.time_literal_2 = 0

            main_state.customer_timer = 0.0
            main_state.messeage_timer = 0.0
            main_state.customer_frame = 0
            main_state.frame_time = 0.0
            main_state.order = 0

            cooing_state.cook_stack_1 = 0
            cooing_state.cook_stack_2 = 0
            cooing_state.cook_stack_3 = 0
            cooing_state.cook_stack_4 = 0
            cooing_state.cook_stack_5 = 0
            cooing_state.cook_stack_6 = 0
            cooing_state.cook_type = 0
            cooing_state.is_cooking_fail = 0

            game_framework.push_state(start_state)


def update():
    game_over.update()
    #pass


def draw():
    clear_canvas()
    game_over.draw()
    update_canvas()