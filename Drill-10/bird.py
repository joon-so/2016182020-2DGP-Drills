import game_framework
from pico2d import *
from ball import Ball

import game_world

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class RunState:
    @staticmethod
    def enter(bird, event):
        if bird.dir == 1:
            bird.velocity += RUN_SPEED_PPS
        elif bird.dir == -1:
            bird.velocity -= RUN_SPEED_PPS
        bird.dir = clamp(-1, bird.velocity, 1)
        pass

    @staticmethod
    def exit(bird, event):
        pass

    @staticmethod
    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        bird.x += bird.velocity * game_framework.frame_time
        bird.x = clamp(25, bird.x, 1600 - 25)

    @staticmethod
    def draw(bird):
        if bird.dir == 1:
            if bird.frame_y == 0:
                if int(bird.frame) == 4:
                    bird.frame = 0
                    bird.frame_y = 2
            bird.image.clip_draw(int(bird.frame) * 182, bird.frame_y * 168, 182, 168, bird.x, bird.y)
            if int(bird.frame) == 4:
                bird.frame_y -= 1
        else:
            bird.image.clip_draw(int(bird.frame) * 182, 338, 182, 169, bird.x, bird.y)


class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.cur_state = RunState
        self.frame = 0
        self.frame_y = 2

    def update(self):
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))