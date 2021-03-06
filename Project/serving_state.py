import random
import json
import os

import game_framework
import main_state
from pico2d import *

name = "Serving_State"
font = None

serving_table = 0

class Serving:
    def __init__(self):
        self.image1 = load_image('cooking_background.png')
        self.image2 = load_image('menu.png')
        self.font = load_font('ENCR10B.TTF', 16)
    def update(self):
        pass
    def draw(self):
        global serving
        self.image1.draw(400, 300)
        self.image2.clip_draw(100 * 0, 100 * 6, 100, 100 , 50 + 400+ 100 * -3, 400)
        self.image2.clip_draw(100 * 0, 100 * 0, 100, 100 , 50 + 400+ 100 * -2, 400)
        self.image2.clip_draw(100 * 5, 100 * 4, 100, 100 , 50 + 400+ 100 * -1, 400)
        self.image2.clip_draw(100 * 2, 100 * 3, 100, 100 , 50 + 400+ 100 * 0, 400)
        self.image2.clip_draw(100 * 2, 100 * 5, 100, 100 , 50 + 400+ 100 * 1, 400)
        self.image2.clip_draw(100 * 2, 100 * 4, 100, 100 , 50 + 400+ 100 * 2, 400)


def enter():
    global serving
    serving = Serving()

def exit():
    global serving
    del(serving)


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
        elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE)):
            game_framework.pop_state()
        elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_q)) and main_state.food_1_stack > 0:
            main_state.food_1_stack-=1
            if(serving_table == 1):
                main_state.Table_1_orderd_Q-=1
            elif(serving_table == 2):
                main_state.Table_2_orderd_Q-=1
            elif(serving_table == 3):
                main_state.Table_3_orderd_Q-=1
            elif(serving_table == 4):
                main_state.Table_4_orderd_Q-=1
            elif(serving_table == 5):
                main_state.Table_5_orderd_Q-=1
            elif(serving_table == 6):
                main_state.Table_6_orderd_Q-=1
        elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_w)) and main_state.food_2_stack > 0:
            main_state.food_2_stack-=1
            if(serving_table == 1):
                main_state.Table_1_orderd_W-=1
            elif(serving_table == 2):
                main_state.Table_2_orderd_W-=1
            elif(serving_table == 3):
                main_state.Table_3_orderd_W-=1
            elif(serving_table == 4):
                main_state.Table_4_orderd_W-=1
            elif(serving_table == 5):
                main_state.Table_5_orderd_W-=1
            elif(serving_table == 6):
                main_state.Table_6_orderd_W-=1
        elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_e)) and main_state.food_3_stack > 0:
            main_state.food_3_stack-=1
            if(serving_table == 1):
                main_state.Table_1_orderd_E-=1
            elif(serving_table == 2):
                main_state.Table_2_orderd_E-=1
            elif(serving_table == 3):
                main_state.Table_3_orderd_E-=1
            elif(serving_table == 4):
                main_state.Table_4_orderd_E-=1
            elif(serving_table == 5):
                main_state.Table_5_orderd_E-=1
            elif(serving_table == 6):
                main_state.Table_6_orderd_E-=1
        elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_r)) and main_state.food_4_stack > 0:
            main_state.food_4_stack-=1
            if(serving_table == 1):
                main_state.Table_1_orderd_R-=1
            elif(serving_table == 2):
                main_state.Table_2_orderd_R-=1
            elif(serving_table == 3):
                main_state.Table_3_orderd_R-=1
            elif(serving_table == 4):
                main_state.Table_4_orderd_R-=1
            elif(serving_table == 5):
                main_state.Table_5_orderd_R-=1
            elif(serving_table == 6):
                main_state.Table_6_orderd_R-=1
        elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_t)) and main_state.food_5_stack > 0:
            main_state.food_5_stack-=1
            if(serving_table == 1):
                main_state.Table_1_orderd_T-=1
            elif(serving_table == 2):
                main_state.Table_2_orderd_T-=1
            elif(serving_table == 3):
                main_state.Table_3_orderd_T-=1
            elif(serving_table == 4):
                main_state.Table_4_orderd_T-=1
            elif(serving_table == 5):
                main_state.Table_5_orderd_T-=1
            elif(serving_table == 6):
                main_state.Table_6_orderd_T-=1
        elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_y)) and main_state.food_6_stack > 0:
            main_state.food_6_stack-=1
            if(serving_table == 1):
                main_state.Table_1_orderd_Y-=1
            elif(serving_table == 2):
                main_state.Table_2_orderd_Y-=1
            elif(serving_table == 3):
                main_state.Table_3_orderd_Y-=1
            elif(serving_table == 4):
                main_state.Table_4_orderd_Y-=1
            elif(serving_table == 5):
                main_state.Table_5_orderd_Y-=1
            elif(serving_table == 6):
                main_state.Table_6_orderd_Y-=1




        # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_w):
        #     main_state.food_2_stack+=1
        # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_e):
        #     main_state.food_3_stack+=1
        # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
        #     main_state.food_4_stack+=1
        # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_t):
        #     main_state.food_5_stack+=1
        # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_y):
        #     main_state.food_6_stack+=1
        # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        #     game_framework.pop_state()
            #game_framework.change_state(main_state)


def update():
    serving.update()
    #pass


def draw():
    #global boy, floor, burner, refrig, sink, cabinet, kitchen_floor, wall, frame, table
    clear_canvas()
    main_state.floor.draw()
    main_state.burner.draw()
    main_state.refrig.draw()
    main_state.sink.draw()
    main_state.cabinet.draw()
    main_state.kitchen_floor.draw()
    main_state.wall.draw()
    main_state.frame.draw()
    main_state.table.draw()
    main_state.customer.draw()
    serving.draw()
    update_canvas()