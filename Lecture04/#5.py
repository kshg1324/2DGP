from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

Cx, Cy = 0 + 25, 90

def move_to_destination(x, y):
    frame = 0
    global Cx, Cy

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
    move_to_destination(132, 243)
    move_to_destination(535, 470)
    move_to_destination(477, 203)
    move_to_destination(715, 136)
    move_to_destination(316, 225)
    move_to_destination(510, 92)
    move_to_destination(692, 518)
    move_to_destination(682, 336)
    move_to_destination(712, 349)
    move_to_destination(0 + 25, 90)

close_canvas()
