import game_framework
import main_state
import start_state
from pico2d import *


name = "StartState"
image = None
image2 = None
image3 = None

def enter():
    global image
    image = load_image('main2.png')



def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if ((event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE)):
                game_framework.change_state(main_state)



def draw():
    clear_canvas()
    image.draw(400 ,300)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






