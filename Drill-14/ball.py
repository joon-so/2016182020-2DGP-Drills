import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.cx, self.cy = 0, 0
        self.x, self.y = random.randint(50, 1500 - 50), random.randint(50, 1100 - 50)
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()

    def get_bb(self):
        return self.cx - 10, self.cy - 10, self.cx + 10, self.cy +10

    def set_background(self, bg):
        self.bg = bg
        self.x, self.y = random.randint(50, 1700 - 50), random.randint(50, 1100 - 50)

    def draw(self):
        self.cx, self.cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.draw(self.cx, self.cy)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass
