import random
from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def draw_charecter(p1, p2):
    global direct
    global frame
    if direct == 0:
        character.clip_draw(frame * 100, 100, 100, 100, p1, p2)
        update_canvas()
        frame = (frame + 1) % 8
    elif direct == 1:
        character.clip_draw(frame * 100, 0, 100, 100, p1, p2)
        update_canvas()
        frame = (frame + 1) % 8

    pass


def move_charecter(p1, p2):
    global frame
    global character_x, character_y
    global t
    global i
    i += 10
    t = i / 100
    character_x = (1 - t) * p1 + t * p2
    character_y = (1 - t) * p1 + t * p2

    pass


def handle_events():
    global running
    global mouse_x, mouse_y
    global move_x, move_y
    global character_x, character_y
    global direct
    global t, i
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            move_x = mouse_x
            move_y = mouse_y
            t = 0
            i = 0
            if character_x > move_x:
                direct = 1
            else:
                direct = 0


open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
Mouse = load_image('hand_arrow.png')

running = True
mouse_x, mouse_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
move_x, move_y = 500, 500
character_x, character_y = 500, 500
direct = 0
frame = 0
t = 0
i = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    Mouse.draw_now(mouse_x + 30, mouse_y - 30)

    #move_charecter(move_x, move_y)

    if direct == 0:
        character.clip_draw(frame * 100, 100, 100, 100, move_x, move_y)
        update_canvas()
        frame = (frame + 1) % 8
    elif direct == 1:
        character.clip_draw(frame * 100, 0, 100, 100, move_x, move_y)
        update_canvas()
        frame = (frame + 1) % 8


    update_canvas()
    delay(0.03)
    handle_events()

close_canvas()
