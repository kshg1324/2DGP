from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)
KPU_GROUND = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

while True:
    clear_canvas()
    KPU_GROUND.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    update_canvas()
    get_events()


close_canvas()

