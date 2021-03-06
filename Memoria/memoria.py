from random import *
from turtle import *
from freegames import path

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'aa', 'ab', 'ac', 'ad', 'ae']*2

car = path('car.gif')
tiles = characters
state = {'mark': None}
writer = Turtle(visible=False)
clicks = {'score': 0}

hide = [True] * 64

if hide == [False] * 64:
    quit()

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    writer.write(clicks['score'])

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        clicks['score'] += 1
        
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        clicks['score'] += 1
        
        

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 9.5, y + 6)
        color('black')
        write(tiles[mark], font=('Arial', 25, 'normal'))

    update()
    ontimer(draw, 100)
writer.goto(160, 160)
writer.write(clicks['score'])
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()