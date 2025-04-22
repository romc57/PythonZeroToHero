from turtle import Screen
from SnakeObj import Snake

SNAKE_INIT_SIZE = 3

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake sssss")

screen.tracer(12)
snake = Snake(12)
screen.update()

screen.onkey(snake.turn_up, 'Up')
screen.onkey(snake.turn_down, 'Down')
screen.onkey(snake.turn_left, 'Left')
screen.onkey(snake.turn_right, 'Right')
screen.listen()

for i in range(670):
    screen.tracer(snake.size)
    snake.move()
    screen.update()
    if snake.check_intersection():
        break
    head = snake.get_location()
    if 300 - abs(head[0]) < 10 or 300 - abs(head[1]) < 10:
        break

screen.exitonclick()