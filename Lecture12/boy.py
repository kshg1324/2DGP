import game_framework
from pico2d import *
from ball import Ball

import game_world
import time
import math

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER_X = (10.0 / 0.3)
PIXEL_PER_METER_Y = (72.0 / 2.2)
PIXEL_PER_METER_CIRCLE = ( 1/3 * 314.1592 / 3.141592 / 6)

RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER_X)
RUN_SPEED_PPS_Y = (RUN_SPEED_MPS * PIXEL_PER_METER_Y)

DRAW_SPEED_KMPH = 2 * 3.141592
DRAW_SPEED_MPM = (DRAW_SPEED_KMPH * 1000.0 / 60.0)
DRAW_SPEED_MPS =  (DRAW_SPEED_MPM / 60.0)
DRAW_SPEED_PPS = (DRAW_SPEED_MPS * PIXEL_PER_METER_CIRCLE)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

COUNT = 0
Revise_Value = 0

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, GHOST_TIMER, SPACE, LSHIFT_DOWN, LSHIFT_UP, RSHIFT_DOWN, RSHIFT_UP, DASH_TIMER = range(12)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_LSHIFT): LSHIFT_DOWN,
    (SDL_KEYDOWN, SDLK_RSHIFT): RSHIFT_DOWN,
    (SDL_KEYUP, SDLK_LSHIFT): LSHIFT_UP,
    (SDL_KEYUP, SDLK_RSHIFT): RSHIFT_UP
}

# Boy States
############
class IdleState:


    @staticmethod
    def enter(boy, event):
        global COUNT, Revise_Value
        boy.Start_Time = get_time()
        if COUNT == 0:
            Revise_Value = boy.Start_Time
            COUNT = COUNT + 1
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.Ticking_Time = get_time()
        print("Start Time: %f sec" % (boy.Start_Time))
        print("Ticking Time: %f sec" % (boy.Ticking_Time))
        print("Revise Value: %f sec" % (Revise_Value))
        if boy.Ticking_Time - boy.Start_Time >= 10:
            boy.add_event(GHOST_TIMER)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 200, 100, 100, boy.x, boy.y)


class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.dir = clamp(-1, boy.velocity, 1)

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x += boy.velocity * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1600 - 25)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)


class SleepState:

    @staticmethod
    def enter(boy, event):
        boy.frame = 0
        boy.radian = 3.141592 / 2
    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        if boy.radian > 0:
            boy.radian = (boy.radian - game_framework.frame_time)
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)

class GhostState:

    @staticmethod
    def enter(boy, event):
        boy.frame = 0
        boy.radian_ghost = 3.141592 / 2
        boy.Float_Y = 0
        boy.radian_circle = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        #boy.radian_circle +=  4 * 3.141592 * boy.Ticking_Time
        boy.Ticking_Time = get_time()
        if boy.Float_Y < 300:
            boy.Float_Y += RUN_SPEED_PPS_Y * game_framework.frame_time
        if boy.radian_ghost > 0:
            boy.radian_ghost = (boy.radian_ghost - game_framework.frame_time)


        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.opacify(1)
            boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
            boy.image.opacify(0.5)
            boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, boy.radian_ghost, '', boy.x - 25 + 100 * math.cos( 4 * 3.141592 * boy.Ticking_Time), boy.y + boy.Float_Y - 25 + 100 * math.sin( 4 * 3.141592 * boy.Ticking_Time), 100, 100)
            boy.image.opacify(1.0)
        else:
            boy.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)
            boy.image.opacify(0.5)
            boy.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100, boy.radian_ghost, '',boy.x + 25 + 100 * math.cos(4 * 3.141592 * boy.Ticking_Time),boy.y + boy.Float_Y - 25 + 100 * math.sin(4 * 3.141592 * boy.Ticking_Time),100, 100)
            boy.image.opacify(1.0)

class DashState:

    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.dir = clamp(-1, boy.velocity, 1)
        boy.timer_for_Dash = 150
    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()


    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer_for_Dash -= 1
        if boy.timer_for_Dash == 0:
            boy.add_event(DASH_TIMER)
        boy.x += boy.velocity * game_framework.frame_time * 3
        boy.x = clamp(25, boy.x, 1600 - 25)

    @staticmethod
    def draw(boy):
        if boy.dir >= 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)





next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState,GHOST_TIMER: GhostState, SPACE: IdleState, LSHIFT_DOWN: IdleState, RSHIFT_DOWN: IdleState, LSHIFT_UP: IdleState, RSHIFT_UP: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState, LSHIFT_DOWN: DashState, RSHIFT_DOWN: DashState, LSHIFT_UP: RunState, RSHIFT_UP: RunState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState, LSHIFT_UP: IdleState, RSHIFT_UP: IdleState, LSHIFT_DOWN: IdleState, RSHIFT_DOWN: IdleState},
    DashState: { LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, RIGHT_UP: IdleState, LEFT_UP: IdleState, SPACE: DashState, LSHIFT_DOWN: RunState, RSHIFT_DOWN: RunState, LSHIFT_UP: RunState, RSHIFT_UP: RunState, DASH_TIMER: RunState},
    GhostState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState, LSHIFT_UP: IdleState, RSHIFT_UP: IdleState, LSHIFT_DOWN: IdleState, RSHIFT_DOWN: IdleState}
}

class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('animation_sheet.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir*3)
        game_world.add_object(ball, 1)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        global Revise_Value
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % (get_time() - Revise_Value), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

