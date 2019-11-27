import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import world_build_state

name = "Rankstate"
rank = []
font = None
Ranking = []

boy = None

def enter():
    global font
    hide_cursor()
    hide_lattice()
    load_rank()
    font = load_font('ENCR10B.TTF', 20)

def exit():
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
            game_framework.change_state(world_build_state)



def update():
    pass


def draw():
    global rank
    global font
    clear_canvas()
    count = 0
    i = 16
    font.draw(550, 900, '[Totla]')

    for data in rank:
        count += 20
        i -= 1
        font.draw(550, 850 - count,'%d. %3.2f' % (i, data[1]), (0, 0, 0))

    update_canvas()


def load_rank():
    global rank
    global Ranking

    with open('rank_data.json', 'r') as f:
        rank = json.load(f)

    rank.sort(key=lambda element: element[1])