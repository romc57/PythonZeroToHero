from turtle import Turtle
from random import randint
class Food(Turtle):

    def __init__(self):
        Turtle.__init__(self, shape="circle")
        self.color("red")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.pos = ()
        self.set_pos()

    def set_pos(self):
        self.pos = (randint(-250, 250), randint(-250, 250))
        self.goto(self.pos[0], self.pos[1])

    def get_pos(self):
        return self.pos