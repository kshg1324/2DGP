import game_framework
import main_state
from pico2d import *


name = "StartState"
image = None
image2 = None
image3 = None
CX = 0
CY = 0

def enter():
    global image, image2, image3
    image = load_image('main2.png')
    image2 = load_image('game_start.png')
    image3 = load_image('game_quit.png')


def exit():
    global image, image2, image3
    del(image)
    del (image2)
    del (image3)

def handle_events():
    events = get_events()
    global CX, CY
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            CX, CY = event.x, 600 - 1 - event.y
            #print("CX =", CX)
            #print("CY =", CY)
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            if event.type == SDL_MOUSEBUTTONDOWN:
                if (150 <= CX <= 250 and 35 <= CY <= 65):
                    game_framework.change_state(main_state)
            if event.type == SDL_MOUSEBUTTONDOWN:
                if (550 <= CX <= 650 and 35 <= CY <= 65):
                    game_framework.quit()


def draw():
    clear_canvas()
    image.draw(400 ,300)
    image2.draw(200,50)
    image3.draw(600,50)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






