import turtle
import random
from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def stop():
    turtle.bye()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     ' + str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)

    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        draw_point((x, y))

    draw_point(p2)
    pass


def handle_events():
    global running
    global mouse_x, mouse_y
    global move_x, move_y
    global character_x, character_y
    global direct
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

hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    Mouse.draw_now(mouse_x, mouse_y)
    if direct == 0:
        character.clip_draw(frame * 100, 100, 100, 100, character_x, character_y)
        update_canvas()
        frame = (frame + 1) % 8
        #character_x += 15
        #if x >= 760:
           # direct = 1
    if direct == 1:
        character.clip_draw(frame * 100, 0, 100, 100, character_x, character_y)
        update_canvas()
        frame = (frame + 1) % 8
        #x -= 15
        #if x <= 40:
            #direct = 0
    delay(0.03)
    update_canvas()

    handle_events()

close_canvas()
