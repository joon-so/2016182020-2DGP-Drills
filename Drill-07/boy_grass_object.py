from Tools.demo.beer import n
from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(50, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Small_Ball:
    def __init__(self):
        self.x, self.y = random.randint(20, 780), 599
        self.image = load_image('ball21x21.png')
        self.speed = random.randint(5, 20)

    def update(self):
        self.y -= self.speed
        if self.y <= 65:
            self.y = 65

    def draw(self):
        self.image.clip_draw(0, 0, 21, 21, self.x, self.y)


class Big_Ball:
    def __init__(self):
        self.x, self.y = random.randint(20, 780), 599
        self.image = load_image('ball41x41.png')
        self.speed = random.randint(5, 20)

    def update(self):
        self.y -= self.speed
        if self.y <= 75:
            self.y = 75

    def draw(self):
        self.image.clip_draw(0, 0, 41, 41, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
open_canvas()

grass = Grass()
team = [Boy() for i in range(11)]
x = random.randint(5, 15)
small_ball_team = [Small_Ball() for i in range(x)]
big_ball_team = [Big_Ball() for i in range(20 - x)]

running = True

# game main loop code

while running:
    handle_events()

    for boy in team:
        boy.update()
    for small_ball in small_ball_team:
        small_ball.update()
    for big_ball in big_ball_team:
        big_ball.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for small_ball in small_ball_team:
        small_ball.draw()
    for big_ball in big_ball_team:
        big_ball.draw()
    update_canvas()

    delay(0.03)

# finalization code

close_canvas()
