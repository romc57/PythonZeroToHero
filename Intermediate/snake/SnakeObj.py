from turtle import Turtle

class Snake:

    def __init__(self, size=3):
        self.size=size
        self.snake = list()

    def create_snake(self):
        for _ in range(self.size):
            square_obj = Turtle(shape="square",)
            square_obj.shapesize(2,2)
            square_obj.goto(0,0)
            self.snake.append(square_obj)
