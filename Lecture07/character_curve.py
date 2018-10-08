from pico2d import *
import random
import turtle
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)
KPU_GROUND = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

count = 0
frame = 0
size = 10
prev_x = 0

#points_x = [(random.randint(0, 1280)) for i in range(size)]
#points_y = [(random.randint(0, 1024)) for i in range(size)]

points = [(random.randint(0, 1280),random.randint(0, 1024)) for i in range(size)]

def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))

def draw_linked_curve_10_points():
    # draw p1-p2
    global count, size, frame, prev_x


    for i in range(0, 50, 2):
        clear_canvas()
        KPU_GROUND.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = (2*t**2-3*t+1)*points[0][0]+(-4*t**2+4*t)*points[1][0]+(2*t**2-t)*points[2][0]
        y = (2*t**2-3*t+1)*points[0][1]+(-4*t**2+4*t)*points[1][1]+(2*t**2-t)*points[2][1]
        if prev_x > x:
            character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
        elif prev_x <= x:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

        prev_x = x
        frame = (frame + 1) % 8
        delay(0.03)
        update_canvas()
        get_events()

    for count in range(0, size - 3):
        for i in range(0, 100, 2):
            clear_canvas()
            KPU_GROUND.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            t = i / 100
            x = ((-t**3 + 2*t**2 - t)*(points[count])[0] + (3*t**3 - 5*t**2 + 2)*(points[count+1])[0] + (-3*t**3 + 4*t**2 + t)*(points[count+2])[0] + (t**3 - t**2)*(points[count+3])[0])/2
            y = ((-t**3 + 2*t**2 - t)*(points[count])[1] + (3*t**3 - 5*t**2 + 2)*(points[count+1])[1] + (-3*t**3 + 4*t**2 + t)*(points[count+2])[1] + (t**3 - t**2)*(points[count+3])[1])/2
            if prev_x > x:
                character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
            elif prev_x <= x:
                character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

            prev_x = x
            frame = (frame + 1) % 8
            delay(0.03)
            update_canvas()
            get_events()

    for i in range(0, 100, 2):
        clear_canvas()
        KPU_GROUND.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * (points[size - 3])[0] + (3 * t ** 3 - 5 * t ** 2 + 2) *(points[size - 2])[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * (points[size - 1])[0] + (t ** 3 - t ** 2) * points[0][0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * (points[size - 3])[1] + (3 * t ** 3 - 5 * t ** 2 + 2) *(points[size - 2])[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * (points[size - 1])[1] + (t ** 3 - t ** 2) * points[0][1]) / 2
        if prev_x > x:
            character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
        elif prev_x <= x:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

        prev_x = x
        frame = (frame + 1) % 8
        delay(0.03)
        update_canvas()
        get_events()

    # draw p1-p2
    for i in range(0, 100, 2):
        clear_canvas()
        KPU_GROUND.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * (points[8])[0] + (3 * t ** 3 - 5 * t ** 2 + 2) *(points[9])[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * (points[0])[0] + (t ** 3 - t ** 2) * points[1][0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * (points[8])[1] + (3 * t ** 3 - 5 * t ** 2 + 2) *(points[9])[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * (points[0])[1] + (t ** 3 - t ** 2) * points[1][1]) / 2
        if prev_x > x:
            character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
        elif prev_x <= x:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

        prev_x = x
        frame = (frame + 1) % 8
        delay(0.03)
        update_canvas()
        get_events()


while True:
    clear_canvas()
    KPU_GROUND.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    #character.clip_draw(frame * 100, 100 * 1, 100, 100, points_x[count], points_y[count])
    draw_linked_curve_10_points()
    update_canvas()
    get_events()


close_canvas()
#

