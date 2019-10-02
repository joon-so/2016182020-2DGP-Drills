from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


x = 0
direct = 0
frame = 0
while x < 800:
    clear_canvas()
    grass.draw(400, 30)
    if direct == 0:
        character.clip_draw(frame * 100, 100, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x += 15
        if x >= 760:
            direct = 1
    if direct == 1:
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 15
        if x <= 40:
            direct = 0
    delay(0.03)
    get_events()

close_canvas()
