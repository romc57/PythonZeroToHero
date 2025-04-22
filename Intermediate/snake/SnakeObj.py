from turtle import Turtle
import time
import math

UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

class Snake:

    def __init__(self, size=3):
        self.size=size
        self.snake = list()
        self.create_snake()

    def create_snake(self):
        for i in range(self.size):
            square_obj = Turtle(shape="square")
            square_obj.color("white")
            square_obj.penup()
            square_obj.shapesize(stretch_wid=1, stretch_len=1)
            square_obj.goto(-(20 * i),0)

            self.snake.append(square_obj)

    def move(self):
        time.sleep(0.3)
        for i in range(self.size -1 ,0 ,-1):
            self.snake[i].goto(self.snake[i -1].xcor(), self.snake[i -1].ycor())
        self.snake[0].forward(20)

    def turn_left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def turn_right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)

    def turn_up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def turn_down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def get_location(self):
        return math.floor(self.snake[0].xcor()), math.floor(self.snake[0].ycor())

    def check_intersection(self):
        head = self.get_location()
        for i in range(1, len(self.snake)):
            if (math.floor(self.snake[i].xcor()), math.floor(self.snake[i].ycor())) == head:
                return True
        return False

    def eating_this(self, pos):
        if math.dist(list(self.get_location()), list(pos)) < 30:
            square_obj = Turtle(shape="square")
            square_obj.color("white")
            square_obj.penup()
            square_obj.shapesize(stretch_wid=1, stretch_len=1)
            square_obj.goto(self.snake[-1].xcor(), self.snake[-1].ycor())
            self.snake.append(square_obj)
            self.size += 1
            return True
        return False
