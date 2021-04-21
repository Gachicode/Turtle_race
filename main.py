import turtle
import time
import random
from resolution import *

COLORS = ['red', 'green', 'blue', 'cyan', 'yellow',
          'pink', 'black', 'orange', 'purple', 'brown']


def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2-10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Only numbers allowed, try again')
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print('Number is not in range, try again')


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            path = random.randrange(1, 20)
            racer.forward(path)

            x,y = racer.pos()
            if y >= HEIGHT//2 - 15:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors)+1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1)*spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles


def Screen_related():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle racing')

 
racers = get_number_of_racers()
Screen_related()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print('The winner is the turtle with color:', winner)
time.sleep(5)