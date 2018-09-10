from pico2d import *
from math import *
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 0
count = 0
theta = -90

radian = math.radians(theta)

while True:
    if(count % 2 == 0):

        while(x < 800 - 42):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 90)
            x = x + 10
            delay(0.01)

        while(y < 600 - 120):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(800 - 42 , y + 90)
            y = y + 10
            delay(0.01)

        while(x > 0 + 84):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x - 84, 600 - 60)
            x = x - 10
            delay(0.01)

        while(y > 132):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(0 + 42 , y - 42)
            y = y - 10
            delay(0.01)

        while(x <= 400):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 90)
            x = x + 10
            delay(0.01)
            
            
        count = count + 1
    if(count % 2 == 1):
        clear_canvas_now() 
        grass.draw_now(400, 30) 
        x = 400 + 250 * cos(radian) 
        y = 300 + 250 * sin(radian)
        character.draw_now(x, y) 
        theta = theta + 1
        radian = radians(theta) 
        delay(0.01) 
        
        if (theta > 270): 
            x = 400 
            y = 30 
            theta = -90 
            count = count + 1
    
close_canvas()
