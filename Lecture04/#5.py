from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')



def move_to_destination(x, y):
    Cx, Cy, frame = 0 + 25, 90, 0


    while (x > Cx):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, Cx, Cy)
        update_canvas()
        frame = (frame + 1) % 8
        Cx += 1
        delay(0.01)

    while (y > Cy):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, Cx, Cy)
        update_canvas()
        frame = (frame + 1) % 8
        Cy += 1
        delay(0.01)

    while (x < Cx):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, Cx, Cy)
        update_canvas()
        frame = (frame + 1) % 8
        Cx -= 1
        delay(0.01)

    while (y < Cy):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, Cx, Cy)
        update_canvas()
        frame = (frame + 1) % 8
        Cy -= 1
        delay(0.01)


while True:
    move_to_destination(203, 535)



close_canvas()
