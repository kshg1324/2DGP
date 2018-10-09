from pico2d import *
import random

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Smallball:
    def __init__(self):
        self.x, self.y = random.randint(0,800), 600
        self.image = load_image('ball21x21.png')
    def draw(self):
        self.image.draw(self.x, self.y)

class Bigball:
    def __init__(self):
        self.x, self.y = random.randint(0,800), 600
        self.image = load_image('ball41x41.png')
    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

boy = Boy()
grass = Grass()

running = True


while running:
    handle_events ()
    boy.update ()
    clear_canvas ()
    grass.draw ()
    boy.draw ()
    update_canvas ()
    delay(0.05)
# game main loop code

close_canvas()
# finalization code