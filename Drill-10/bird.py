import game_framework
from pico2d import *
from ball import Ball

import game_world

# Boy Run Speed
PIXEL_PER_METER = (1.0 / 0.03) # 1 pixel 3cm
RUN_SPEED_KMPH = 40.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

FLY = range(1)

class IdleState:

    @staticmethod
    def enter(bird, event):
        pass

    @staticmethod
    def exit(bird, event):
        pass

    @staticmethod
    def do(bird):
        bird.add_event(FLY)

    @staticmethod
    def draw(bird):
        pass


class RunState:
    @staticmethod
    def enter(bird, event):
        pass

    @staticmethod
    def exit(bird, event):
        pass

    @staticmethod
    def do(bird):
        bird.velocity = 0
        if bird.direct == 1:
            bird.velocity += RUN_SPEED_PPS
        elif bird.direct == -1:
            bird.velocity -= RUN_SPEED_PPS
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        bird.x += bird.velocity * game_framework.frame_time
        bird.x = clamp(75, bird.x, 1600 - 75)
        if bird.x == 1600 - 75:
            bird.direct = -1
        elif bird.x == 75:
            bird.direct = 1

    @staticmethod
    def draw(bird):
        if bird.direct == 1:
            if bird.frame_y == 0:
                if int(bird.frame) == 4:
                    bird.frame = 0
                    bird.frame_y = 2
            bird.image.clip_draw(int(bird.frame) * 182, bird.frame_y * 168, 182, 168, bird.x, bird.y)
            if int(bird.frame) == 4:
                bird.frame_y -= 1
        else:
            if bird.frame_y == 0:
                if int(bird.frame) == 4:
                    bird.frame = 0
                    bird.frame_y = 2
            bird.image.clip_composite_draw(int(bird.frame) * 182, bird.frame_y * 168, 182, 168, 3.141592 / 1, 'v', bird.x,
                                          bird.y, 182, 168)
            if int(bird.frame) == 4:
                bird.frame_y -= 1

next_state_table = {
    IdleState: {FLY: RunState}
}


class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 400
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.direct = 1
        self.velocity = 0
        self.cur_state = IdleState
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.frame = 0
        self.frame_y = 2

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
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))