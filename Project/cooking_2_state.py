import random
import json
import os

import game_framework
import main_state
from pico2d import *

name = "cooking_2_State"
font = None
cook_stack_2 = 0
class Cooking_2:
    def __init__(self):
        self.image1 = load_image('cooking_background.png')
        self.image2 = load_image('menu.png')
        self.font = load_font('ENCR10B.TTF', 16)
    def update(self):
        pass
    def draw(self):
        global cook_stack_2
        self.image1.draw(400, 300)
        #self.image2.clip_draw(100 * 0, 100 * 6, 100, 100 , 50 + 400 + 100 * -3, 400)
        self.image2.clip_draw(100 * 0, 100 * 0, 100, 100 , 50 + 400+ 100 * -1 + 50, 400)
        # self.image2.clip_draw(100 * 5, 100 * 4, 100, 100 , 50 + 400+ 100 * -1, 400)
        # self.image2.clip_draw(100 * 2, 100 * 3, 100, 100 , 50 + 400+ 100 * 0, 400)
        # self.image2.clip_draw(100 * 2, 100 * 5, 100, 100 , 50 + 400+ 100 * 1, 400)
        # self.image2.clip_draw(100 * 0, 100 * 0, 100, 100 , 50 + 400+ 100 * 2, 400)
        if cook_stack_2 == 0:
            self.font.draw(400, 300, '(h a m b u r g e r)', (0, 0, 0))
        elif cook_stack_2 == 1:
            self.font.draw(400, 300, '(a m b u r g e r)', (0, 0, 0))
        elif cook_stack_2 == 2:
            self.font.draw(400, 300, '(m b u r g e r)', (0, 0, 0))
        elif cook_stack_2 == 3:
            self.font.draw(400, 300, '(b u r g e r)', (0, 0, 0))
        elif cook_stack_2 == 4:
            self.font.draw(400, 300, '(u r g e r)', (0, 0, 0))
        elif cook_stack_2 == 5:
            self.font.draw(400, 300, '(r g e r)', (0, 0, 0))
        elif cook_stack_2 == 6:
            self.font.draw(400, 300, '(g e r)', (0, 0, 0))
        elif cook_stack_2 == 7:
            self.font.draw(400, 300, '(e r)', (0, 0, 0))
        elif cook_stack_2 == 8:
            self.font.draw(400, 300, '(r)', (0, 0, 0))
def enter():
    global cooking_2
    cooking_2 = Cooking_2()

def exit():
    global cooking_2
    del(cooking_2)


def pause():
    pass


def resume():
    pass



def handle_events():
    global cook_stack_2
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_h):
            cook_stack_2+=1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a) and cook_stack_2 == 1:
            cook_stack_2 += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_m)and cook_stack_2 == 2:
            cook_stack_2 += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_b)and cook_stack_2 == 3:
            cook_stack_2 += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_u)and cook_stack_2 == 4:
            cook_stack_2 += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_r)and cook_stack_2 == 5:
            cook_stack_2 += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_g)and cook_stack_2 == 6:
            cook_stack_2 += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_e)and cook_stack_2 == 7:
            cook_stack_2 += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_r)and cook_stack_2 == 8:
            main_state.food_2_stack += 1
            cook_stack_2 = 0
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
    cooking_2.update()
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
    cooking_2.draw()
    update_canvas()