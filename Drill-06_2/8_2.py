from pico2d import *

import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def move_charecter(p1, p2):
    global frame, direct
    global t
    global i
    global character_x, character_y, move_x, move_y, x, y
    if i != 100:
        i += 10
    elif i == 100:
        character_x = move_x
        character_y = move_y
    t = 1 / 100 * i
    x = (1 - t) * p1[0] + t * p2[0]
    y = (1 - t) * p1[1] + t * p2[1]
    if direct == 0:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
    elif direct == 1:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
    pass


def draw_curve_4_points(p1, p2, p3, p4):
    # draw p1-p2
    global t, i
    global to
    global ch_i
    global frame

    for i in range(0, 100, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 200
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8

    # draw p2-p3
    for i in range(0, 200, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 200
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] +
             (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] +
             (t ** 3 - t ** 2) * p4[1]) / 2
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8

    for i in range(50, 200, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 200
        x = (2 * t ** 2 - 3 * t + 1) * p2[0] + (-4 * t ** 2 + 4 * t) * p3[0] + (2 * t ** 2 - t) * p4[0]
        y = (2 * t ** 2 - 3 * t + 1) * p2[1] + (-4 * t ** 2 + 4 * t) * p3[1] + (2 * t ** 2 - t) * p4[1]
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8



    ch_i += 1
    if ch_i == 10:
        ch_i = 0

    pass

def draw_curve_10_points(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    global frame
    # draw p1-p2
    for i in range(0, 500, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 1000
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8


    # draw p2-p3
    for i in range(0, 1000, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 1000
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p3[0] +
    (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p3[1] +
    (t ** 3 - t ** 2) * p4[1]) / 2
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8



    # draw p3-p4
    for i in range(0, 1000, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 1000
        x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p4[0] +
    (t ** 3 - t ** 2) * p5[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p4[1] +
    (t ** 3 - t ** 2) * p5[1]) / 2
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8

    # draw p4-p5
    for i in range(0, 1000, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 1000
        x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p5[0] +
    (t ** 3 - t ** 2) * p6[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p5[1] +
    (t ** 3 - t ** 2) * p6[1]) / 2
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8

    # draw p5-p6
    for i in range(0, 1000, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 1000
        x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p6[0] +
    (t ** 3 - t ** 2) * p7[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p6[1] +
    (t ** 3 - t ** 2) * p7[1]) / 2
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8

    # draw p6-p7
    for i in range(0, 1000, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 1000
        x = ((-t ** 3 + 2 * t ** 2 - t) * p5[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p7[0] +
    (t ** 3 - t ** 2) * p8[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p5[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p7[1] +
    (t ** 3 - t ** 2) * p8[1]) / 2
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8


    # draw p7-p8
    for i in range(500, 1000, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 1000
        x = ((-t ** 3 + 2 * t ** 2 - t) * p6[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p8[0] +
    (t ** 3 - t ** 2) * p9[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p6[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p8[1] +
    (t ** 3 - t ** 2) * p9[1]) / 2
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8


    # draw p8-p9
    for i in range(0, 1000, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 1000
        x = ((-t ** 3 + 2 * t ** 2 - t) * p7[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p9[0] +
    (t ** 3 - t ** 2) * p10[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p7[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p9[1] +
    (t ** 3 - t ** 2) * p10[1]) / 2
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8

    # draw p9-p10
    for i in range(0, 1000, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 1000
        x = ((-t ** 3 + 2 * t ** 2 - t) * p8[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p10[0] +
    (t ** 3 - t ** 2) * p1[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p8[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p10[1] +
    (t ** 3 - t ** 2) * p1[1]) / 2
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8

    # draw p10-p1
    for i in range(0, 1000, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 1000
        x = ((-t ** 3 + 2 * t ** 2 - t) * p9[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p1[0] +
    (t ** 3 - t ** 2) * p2[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p9[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p1[1] +
    (t ** 3 - t ** 2) * p2[1]) / 2
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8

    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True

frame = 0

ch = [(random.randint(300, 900), random.randint(300, 900)) for k in range(10)]

hide_cursor()

while running:
    draw_curve_10_points(ch[0], ch[1], ch[2], ch[3], ch[4], ch[5], ch[6], ch[7], ch[8], ch[9])


close_canvas()
