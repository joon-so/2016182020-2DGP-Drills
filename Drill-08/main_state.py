import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

boy = None
grass = None
font = None



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    def __init__(self):
        self.x, self.y = 40, 90
        self.frame_x = 0
        self.frame_y = 100
        self.image = load_image('animation_sheet.png')
        self.dir = 15

    def update(self):
        self.frame_x = (self.frame_x + 1) % 8
        self.x += self.dir
        if self.x >= 760:
            self.dir = -15
            if self.x == 760:
                self.frame_y = 0
        elif self.x <= 40:
            self.dir = 15
            if self.x == 40:
                self.frame_y = 100

    def draw(self):
        self.image.clip_draw(self.frame_x * 100, self.frame_y, 100, 100, self.x, self.y)

def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()
    pass


def exit():
    global boy, grass
    del (boy)
    del (grass)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
    pass


def update():
    boy.update()
    pass


def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
    delay(0.03)
    pass





