"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

from random import randint 
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
        "se agregó estas dos lineas que simulan el movimiento aleatorio de la comida"
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    clear()

    snakecol = ''
    foodcol = ''
    snakecolnum = randint(1,5)
    foodcolnum = randint(1,5)
    
    while snakecolnum == foodcolnum:
        foodcolnum = randint(1,5)

    if snakecolnum == 1:
        snakecol = 'green'
    elif snakecolnum == 2:
        snakecol = 'blue'
    elif snakecolnum == 3:
        snakecol = 'black'
    elif snakecolnum == 4:
        snakecol = 'yellow'
    elif snakecolnum == 5:
        snakecol = 'purple'
    
    if foodcolnum == 1:
        foodcol = 'green'
    elif foodcolnum == 2:
        foodcol = 'blue'
    elif foodcolnum == 3:
        foodcol = 'black'
    elif foodcolnum == 4:
        foodcol = 'yellow'
    elif foodcolnum == 5:
        foodcol = 'purple'

    for body in snake:
        square(body.x, body.y, 9, snakecol)

    square(food.x, food.y, 9, foodcol)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()