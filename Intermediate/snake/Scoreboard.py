from turtle import Turtle

TOP_Y = 260
FONT = ("Arial", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, TOP_Y)

    def render(self, score: int):
        self.clear()
        self.write(f"Score: {score}    [R] Restart   [Q] Quit", align="center", font=FONT)

    def game_over(self, score: int):
        self.clear()
        self.write(f"Game Over - Score: {score}    [R] Restart   [Q] Quit", align="center", font=FONT)

