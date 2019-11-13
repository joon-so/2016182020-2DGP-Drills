import game_framework
from pico2d import *

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
    def enter(brick, event):
        pass

    @staticmethod
    def exit(brick, event):
        pass

    @staticmethod
    def do(brick):
        brick.add_event(FLY)

    @staticmethod
    def draw(brick):
        pass


class RunState:
    @staticmethod
    def enter(brick, event):
        pass

    @staticmethod
    def exit(brick, event):
        pass

    @staticmethod
    def do(brick):
        brick.velocity = 0
        if brick.direct == 1:
            brick.velocity += RUN_SPEED_PPS
        elif brick.direct == -1:
            brick.velocity -= RUN_SPEED_PPS

        brick.x += brick.velocity * game_framework.frame_time
        brick.x = clamp(80, brick.x, 1600 - 130)
        if brick.x == 1600 - 130:
            brick.direct = -1
        elif brick.x == 80:
            brick.direct = 1

    @staticmethod
    def draw(brick):
        brick.image.clip_draw(0, 0, 180, 40, brick.x, brick.y)


next_state_table = {
    IdleState: {FLY: RunState}
}


class Brick:

    def __init__(self):
        self.x, self.y = 1600 // 2, 200
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('brick180x40.png')
        self.direct = 1
        self.velocity = 0
        self.cur_state = IdleState
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def get_bb(self):
        return self.x - 90, self.y + 20, self.x + 90, self.y + 20

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
        draw_rectangle(*self.get_bb())