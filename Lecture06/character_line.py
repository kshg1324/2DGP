from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)
KPU_GROUND = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

frame = 0
size = 20
points = [(random.randint(0, 1280), random.randint(0, 1080)) for i in range(size)]

def draw_line():
    global frame
    for j in range(0, size):
        for i in range(0, 100 + 1, 2):
            clear_canvas()
            KPU_GROUND.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            t = i / 100
            if j != size - 1:
                x = (1 - t) * (points[j])[0] + t * (points[j+1])[0]
                y = (1 - t) * (points[j])[1] + t * (points[j+1])[1]
            elif j == size - 1:
                x = (1 - t) * (points[j])[0] + t * (points[0])[0]
                y = (1 - t) * (points[j])[1] + t * (points[0])[1]

            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
            frame = (frame + 1) % 8
            delay(0.03)
            update_canvas()
            get_events()


while True:
    clear_canvas()
    KPU_GROUND.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    draw_line()
    update_canvas()
    get_events()


close_canvas()

