import random
import json
import os

import game_framework
import main_state
import cooking_state
import start_state
from pico2d import *

name = "Stageclear_Stage"
font = None

gameover_state = 0

class Stage_Clear:
    def __init__(self):
        self.image = load_image('stage_clear.png')
        self.bgm = load_music('clear.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
    def update(self):
        pass
    def draw(self):
        self.image.draw(400, 300)


def enter():
    global stage_clear
    stage_clear = Stage_Clear()

def exit():
    global stage_clear
    del(stage_clear)


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

            main_state.Table_1_timer = 0
            main_state.Table_2_timer = 0
            main_state.Table_3_timer = 0
            main_state.Table_4_timer = 0
            main_state.Table_5_timer = 0
            main_state.Table_6_timer = 0

            main_state.time_literal = 0
            main_state.time_literal_2 = 0
            main_state.time_literal_3 = 0

            main_state.food_literal_1 = 0.0
            main_state.food_literal_2 = 0.0
            main_state.food_literal_3 = 0.0
            main_state.food_literal_4 = 0.0
            main_state.food_literal_5 = 0.0
            main_state.food_literal_6 = 0.0

            main_state.customer_literal_1 = 0
            main_state.customer_literal_2 = 0
            main_state.customer_literal_3 = 0
            main_state.customer_literal_4 = 0
            main_state.customer_literal_5 = 0
            main_state.customer_literal_6 = 0

            main_state.a = 0
            main_state.b = 0
            main_state.c = 0
            main_state.d = 0
            main_state.e = 0
            main_state.f = 0

            main_state.food_timer = 0.0
            main_state.customer_timer = 0.0
            main_state.messeage_timer = 0.0
            main_state.customer_frame = 0
            main_state.frame_time = 0.0
            main_state.order = 0

            cooking_state.cook_stack_1 = 0
            cooking_state.cook_stack_2 = 0
            cooking_state.cook_stack_3 = 0
            cooking_state.cook_stack_4 = 0
            cooking_state.cook_stack_5 = 0
            cooking_state.cook_stack_6 = 0
            cooking_state.cook_type = 0
            cooking_state.is_cooking_fail = 0

            game_framework.push_state(start_state)


def update():
    stage_clear.update()
    #pass


def draw():
    clear_canvas()
    stage_clear.draw()
    update_canvas()