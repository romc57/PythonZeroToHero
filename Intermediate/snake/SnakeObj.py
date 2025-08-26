from turtle import Turtle
import math

UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

MOVE_DISTANCE = 20

class Snake:

    def __init__(self, size=3):
        self.snake = list()
        self.create_snake(size)

    def create_snake(self, size):
        for i in range(size):
            square_obj = Turtle(shape="square")
            square_obj.color("white")
            square_obj.penup()
            square_obj.shapesize(stretch_wid=1, stretch_len=1)
            square_obj.goto(-(MOVE_DISTANCE * i),0)

            self.snake.append(square_obj)

    def move(self):
        for i in range(len(self.snake) - 1 , 0 , -1):
            self.snake[i].goto(self.snake[i -1].xcor(), self.snake[i -1].ycor())
        self.snake[0].forward(MOVE_DISTANCE)

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
            self.extend()
            return True
        return False

    def extend(self):
        tail = self.snake[-1]
        square_obj = Turtle(shape="square")
        square_obj.color("white")
        square_obj.penup()
        square_obj.shapesize(stretch_wid=1, stretch_len=1)
        square_obj.goto(tail.xcor(), tail.ycor())
        self.snake.append(square_obj)

    @property
    def size(self):
        return len(self.snake)
