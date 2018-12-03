import random
import json
import os

import game_framework
import main_state
from pico2d import *

name = "Cooking_State"
font = None

cook_stack_1 = 0
cook_stack_2 = 0
cook_stack_3 = 0
cook_stack_4 = 0
cook_stack_5 = 0
cook_stack_6 = 0
cook_type = 0
is_cooking_fail = 0
class Cooking:
    def __init__(self):
        self.image1 = load_image('cooking_background.png')
        self.image2 = load_image('menu2.png')
        self.font = load_font('ENCR10B.TTF', 16)
    def update(self):
        pass
    def draw(self):
        global cook_stack_1,cook_stack_2,cook_stack_3,cook_stack_4,cook_stack_5,cook_stack_6,cook_type,is_cooking_fail
        self.image1.draw(400, 300)
        if (cook_type == 0):
            self.image2.clip_draw(100 * 1, 100 * 9, 100, 100, 50 + 400 + 100 * -3, 400)
            self.image2.clip_draw(100 * 3, 100 * 1, 100, 100, 50 + 400 + 100 * -2, 400)
            self.image2.clip_draw(100 * 0, 100 * 5, 100, 100, 50 + 400 + 100 * -1, 400)
            self.image2.clip_draw(100 * 4, 100 * 5, 100, 100, 50 + 400 + 100 * 0, 400)
            self.image2.clip_draw(100 * 0, 100 * 7, 100, 100, 50 + 400 + 100 * 1, 400)
            self.image2.clip_draw(100 * 2, 100 * 6, 100, 100, 50 + 400 + 100 * 2, 400)
        elif (cook_type == 1):
            self.image2.clip_draw(100 * 1, 100 * 9, 100, 100, 50 + 400 + 100 * -1 + 50, 400)
            if cook_stack_1 == 0:
                self.font.draw(400, 300, '(o m e l e t)', (0, 0, 0))
            elif cook_stack_1 == 1:
                self.font.draw(400, 300, '(m e l e t)', (0, 0, 0))
            elif cook_stack_1 == 2:
                self.font.draw(400, 300, '(e l e t)', (0, 0, 0))
            elif cook_stack_1 == 3:
                self.font.draw(400, 300, '(l e t)', (0, 0, 0))
            elif cook_stack_1 == 4:
                self.font.draw(400, 300, '(e t)', (0, 0, 0))
            elif cook_stack_1 == 5:
                self.font.draw(400, 300, '(t)', (0, 0, 0))
        elif (cook_type == 2):
            self.image2.clip_draw(100 * 3, 100 * 1, 100, 100, 50 + 400 + 100 * -1 + 50, 400)
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
        elif (cook_type == 3):
            self.image2.clip_draw(100 * 0, 100 * 5, 100, 100, 50 + 400 + 100 * -1 + 50, 400)
            if cook_stack_3 == 0:
                self.font.draw(400, 300, '(c o f f e e)', (0, 0, 0))
            elif cook_stack_3 == 1:
                self.font.draw(400, 300, '(o f f e e)', (0, 0, 0))
            elif cook_stack_3 == 2:
                self.font.draw(400, 300, '(f f e e)', (0, 0, 0))
            elif cook_stack_3 == 3:
                self.font.draw(400, 300, '(f e e)', (0, 0, 0))
            elif cook_stack_3 == 4:
                self.font.draw(400, 300, '(e e)', (0, 0, 0))
            elif cook_stack_3 == 5:
                self.font.draw(400, 300, '(e)', (0, 0, 0))
        elif (cook_type == 4):
            self.image2.clip_draw(100 * 4, 100 * 5, 100, 100, 50 + 400 + 100 * -1 + 50, 400)
            if cook_stack_4 == 0:
                self.font.draw(400, 300, '(p i z z a)', (0, 0, 0))
            elif cook_stack_4 == 1:
                self.font.draw(400, 300, '(i z z a)', (0, 0, 0))
            elif cook_stack_4 == 2:
                self.font.draw(400, 300, '(z z a)', (0, 0, 0))
            elif cook_stack_4 == 3:
                self.font.draw(400, 300, '(z a)', (0, 0, 0))
            elif cook_stack_4 == 4:
                self.font.draw(400, 300, '(a)', (0, 0, 0))
        elif (cook_type == 5):
            self.image2.clip_draw(100 * 2, 100 * 5, 100, 100, 50 + 400 + 100 * -1 + 50, 400)
            if cook_stack_5 == 0:
                self.font.draw(400, 300, '(f i s h)', (0, 0, 0))
            elif cook_stack_5 == 1:
                self.font.draw(400, 300, '(i s h)', (0, 0, 0))
            elif cook_stack_5 == 2:
                self.font.draw(400, 300, '(s h)', (0, 0, 0))
            elif cook_stack_5 == 3:
                self.font.draw(400, 300, '(h)', (0, 0, 0))
        elif (cook_type == 6):
            self.image2.clip_draw(100 * 0, 100 * 7, 100, 100, 50 + 400 + 100 * -1 + 50, 400)
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
    global cooking
    cooking = Cooking()

def exit():
    global cooking
    del(cooking)

def pause():
    pass

def resume():
    pass

def handle_events():
    global cook_stack_1, cook_stack_2, cook_stack_3, cook_stack_4, cook_stack_5, cook_stack_6, cook_type, is_cooking_fail
    events = get_events()
    for event in events:
        if (event.type == SDL_KEYDOWN):
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif (cook_type == 0):
                if ((event.type, event.key) == (SDL_KEYDOWN, SDLK_q)):
                    cook_type = 1
                    main_state.Money -= 5
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_w)):
                    cook_type = 2
                    main_state.Money -= 5
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_e)):
                    cook_type = 3
                    main_state.Money -= 5
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_r)):
                    cook_type = 4
                    main_state.Money -= 5
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_t)):
                    cook_type = 5
                    main_state.Money -= 5
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_y)):
                    cook_type = 6
                    main_state.Money -= 5
            elif(cook_type == 1):
                if ((event.type, event.key) == (SDL_KEYDOWN, SDLK_o)) and cook_stack_1 == 0:
                    cook_stack_1 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_m)) and cook_stack_1 == 1:
                    cook_stack_1 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_e))and cook_stack_1 == 2:
                    cook_stack_1 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_l))and cook_stack_1 == 3:
                    cook_stack_1 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_e))and cook_stack_1 == 4:
                    cook_stack_1 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_t))and cook_stack_1 == 5:
                    main_state.food_1_stack += 1
                    cook_stack_1 = 0
                    cook_type = 0
                    game_framework.pop_state()
                else:
                    is_cooking_fail = 1
                    main_state.messeage_timer = 0
                    cook_stack_1 = 0
                    cook_type = 0
                    game_framework.pop_state()
            elif (cook_type == 2):
                if ((event.type, event.key) == (SDL_KEYDOWN, SDLK_h))and cook_stack_2 == 0:
                    cook_stack_2 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_a)) and cook_stack_2 == 1:
                    cook_stack_2 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_m)) and cook_stack_2 == 2:
                    cook_stack_2 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_b)) and cook_stack_2 == 3:
                    cook_stack_2 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_u)) and cook_stack_2 == 4:
                    cook_stack_2 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_r)) and cook_stack_2 == 5:
                    cook_stack_2 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_g)) and cook_stack_2 == 6:
                    cook_stack_2 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_e)) and cook_stack_2 == 7:
                    cook_stack_2 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_r)) and cook_stack_2 == 8:
                    main_state.food_2_stack += 1
                    cook_stack_2 = 0
                    cook_type = 0
                    game_framework.pop_state()
                else:
                    is_cooking_fail = 1
                    main_state.messeage_timer = 0
                    cook_stack_2 = 0
                    cook_type = 0
                    game_framework.pop_state()
            elif (cook_type == 3):
                if ((event.type, event.key) == (SDL_KEYDOWN, SDLK_c))and cook_stack_3 == 0:
                    cook_stack_3 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_o)) and cook_stack_3 == 1:
                    cook_stack_3 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_f)) and cook_stack_3 == 2:
                    cook_stack_3 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_f)) and cook_stack_3 == 3:
                    cook_stack_3 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_e)) and cook_stack_3 == 4:
                    cook_stack_3 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_e)) and cook_stack_3 == 5:
                    main_state.food_3_stack += 1
                    cook_stack_3 = 0
                    cook_type = 0
                    game_framework.pop_state()
                else:
                    is_cooking_fail = 1
                    main_state.messeage_timer = 0
                    cook_stack_3 = 0
                    cook_type = 0
                    game_framework.pop_state()
            elif (cook_type == 4):
                if ((event.type, event.key) == (SDL_KEYDOWN, SDLK_p))and cook_stack_4 == 0:
                    cook_stack_4 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_i)) and cook_stack_4 == 1:
                    cook_stack_4 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_z)) and cook_stack_4 == 2:
                    cook_stack_4 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_z)) and cook_stack_4 == 3:
                    cook_stack_4 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_a)) and cook_stack_4 == 4:
                    main_state.food_4_stack += 1
                    cook_stack_4 = 0
                    cook_type = 0
                    game_framework.pop_state()
                else:
                    is_cooking_fail = 1
                    main_state.messeage_timer = 0
                    cook_stack_4 = 0
                    cook_type = 0
                    game_framework.pop_state()
            elif (cook_type == 5):
                if ((event.type, event.key) == (SDL_KEYDOWN, SDLK_f))and cook_stack_5 == 0:
                    cook_stack_5 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_i)) and cook_stack_5 == 1:
                    cook_stack_5 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_s)) and cook_stack_5 == 2:
                    cook_stack_5 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_h)) and cook_stack_5 == 3:
                    main_state.food_5_stack += 1
                    cook_stack_5 = 0
                    cook_type = 0
                    game_framework.pop_state()
                else:
                    is_cooking_fail = 1
                    main_state.messeage_timer = 0
                    cook_stack_5 = 0
                    cook_type = 0
                    game_framework.pop_state()
            elif (cook_type == 6):
                if ((event.type, event.key) == (SDL_KEYDOWN, SDLK_p)) and cook_stack_6 == 0:
                    cook_stack_6 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_u)) and cook_stack_6 == 1:
                    cook_stack_6 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_d)) and cook_stack_6 == 2:
                    cook_stack_6 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_d)) and cook_stack_6 == 3:
                    cook_stack_6 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_i)) and cook_stack_6 == 4:
                    cook_stack_6 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_n)) and cook_stack_6 == 5:
                    cook_stack_6 += 1
                elif ((event.type, event.key) == (SDL_KEYDOWN, SDLK_g)) and cook_stack_6 == 6:
                    main_state.food_6_stack += 1
                    cook_stack_6 = 0
                    cook_type = 0
                    game_framework.pop_state()
                else:
                    is_cooking_fail = 1
                    main_state.messeage_timer = 0
                    cook_stack_6 = 0
                    cook_type = 0
                    game_framework.pop_state()

def update():
    cooking.update()

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
    cooking.draw()
    update_canvas()