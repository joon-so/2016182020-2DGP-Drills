from pico2d import *

import game_framework
import main_state

name = "PauseState"

pause = None
time = 0

def enter():
    global pause
    pause = load_image('pause.png')


def exit():
    global pause
    del (pause)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()
    pass


def update():
    global time
    time += 1
    if time == 40:
        time = 0
    pass


def draw():
    clear_canvas()
    main_state.grass.draw()
    main_state.boy.draw()
    if time <= 20:
        pause.clip_draw(200, 200, 500, 500, 400, 300, 200, 200)
    update_canvas()
    pass