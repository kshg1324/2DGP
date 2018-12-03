import random
import json
import os

import game_framework
import main_state
from pico2d import *

name = "Cooking_6_State"
font = None
cook_stack_6 = 0
class Cooking_6:
    def __init__(self):
        self.image1 = load_image('cooking_background.png')
        self.image2 = load_image('menu.png')
        self.font = load_font('ENCR10B.TTF', 16)
    def update(self):
        pass
    def draw(self):
        global cook_stack_6
        self.image1.draw(400, 300)
        # self.image2.clip_draw(100 * 0, 100 * 6, 100, 100 , 50 + 400 + 100 * -3, 400)
        # self.image2.clip_draw(100 * 0, 100 * 0, 100, 100 , 50 + 400+ 100 * -2, 400)
        # self.image2.clip_draw(100 * 5, 100 * 4, 100, 100 , 50 + 400+ 100 * -1, 400)
        # self.image2.clip_draw(100 * 2, 100 * 3, 100, 100 , 50 + 400+ 100 * 0, 400)
        # self.image2.clip_draw(100 * 2, 100 * 5, 100, 100 , 50 + 400+ 100 * 1, 400)
        self.image2.clip_draw(100 * 0, 100 * 0, 100, 100 , 50 + 400+ 100 * 2, 400)
        if cook_stack_6 == 0:
            self.font.draw(400, 300, '(p u d d i n g)', (0, 0, 0))
        elif cook_stack_6 == 1:
            self.font.draw(400, 300, '(u d d i n g)', (0, 0, 0))
        elif cook_stack_6 == 2:
            self.font.draw(400, 300, '(d d i n g)', (0, 0, 0))
        elif cook_stack_6 == 3:
            self.font.draw(400, 300, '(d i n g)', (0, 0, 0))
        elif cook_stack_6 == 4:
            self.font.draw(400, 300, '(i n g)', (0, 0, 0))
        elif cook_stack_6 == 5:
            self.font.draw(400, 300, '(n g)', (0, 0, 0))
        elif cook_stack_6 == 6:
            self.font.draw(400, 300, '(g)', (0, 0, 0))
def enter():
    global cooking_6
    cooking_6 = Cooking_6()

def exit():
    global cooking_6
    del(cooking_6)


def pause():
    pass


def resume():
    pass



def handle_events():
    global cook_stack_6
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            cook_stack_6 += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_u) and cook_stack_6 == 1:
            cook_stack_6 += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_d)and cook_stack_6 == 2:
            cook_stack_6 += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_d)and cook_stack_6 == 3:
            cook_stack_6 += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_i)and cook_stack_6 == 4:
            cook_stack_6 += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_n)and cook_stack_6 == 5:
            cook_stack_6 += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_g)and cook_stack_6 == 6:
            main_state.food_6_stack += 1
            cook_stack_6 = 0
            game_framework.pop_state()
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
    cooking_6.update()
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
    cooking_6.draw()
    update_canvas()