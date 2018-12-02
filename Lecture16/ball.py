import random
from pico2d import *
import boy
import game_world
import game_framework
#from background import FixedBackground as Background
import background


class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1837)-self.bg.window_left, random.randint(0, 1109), 0


    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def set_background(self, bg):


    def update(self):
        self.x = clamp(50, self.x, 1800-50)
        self.y = clamp(20,self.y, 1100-25)
        self.y -= self.fall_speed * game_framework.frame_time
        #cx, cy = boy.x - boy.bg.window_left, boy.y - boy.bg.window_bottom
