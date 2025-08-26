from turtle import Screen
from SnakeObj import Snake
from Food import Food
from Scoreboard import Scoreboard

SNAKE_INIT_SIZE = 3
BOARD_SIZE = 600
HALF_BOARD = BOARD_SIZE // 2
WALL_MARGIN = 10
MOVE_DELAY = 0.1

class Game:

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=BOARD_SIZE, height=BOARD_SIZE)
        self.screen.bgcolor("black")
        self.screen.title("Snake sssss")
        self.screen.tracer(0)
        self.snake = Snake(SNAKE_INIT_SIZE)
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.screen.update()
        self.bind_keys()
        self.screen.listen()
        self.score = 0
        self.running = True
        self.scoreboard.render(self.score)
        self.game_loop()
        # Keep the window open and process events
        self.screen.mainloop()

    def game_loop(self):
        if not self.running:
            return
        self.snake.move()
        if self.check_violations():
            self.present_results()
            return
        if self.snake.eating_this(self.food.get_pos()):
            self.ate_that()
        self.screen.update()
        self.screen.ontimer(self.game_loop, int(MOVE_DELAY * 1000))


    def check_violations(self):
        if self.snake.check_intersection():
            return True
        head = self.snake.get_location()
        if HALF_BOARD - abs(head[0]) < WALL_MARGIN or HALF_BOARD - abs(head[1]) < WALL_MARGIN:
            return True
        return False

    def present_results(self):
        self.running = False
        self.scoreboard.game_over(self.score)

    def ate_that(self):
        self.update_score()
        self.food.set_pos()


    def update_score(self):
        self.score += 1
        self.scoreboard.render(self.score)

    def restart(self):
        if self.running:
            return
        # clear snake
        for segment in self.snake.snake:
            segment.hideturtle()
        self.snake = Snake(SNAKE_INIT_SIZE)
        self.bind_keys()
        self.food.set_pos()
        self.score = 0
        self.scoreboard.render(self.score)
        self.running = True
        self.game_loop()

    def quit(self):
        self.screen.bye()

    def bind_keys(self):
        # Rebind controls to the current snake instance and game actions
        self.screen.onkey(self.snake.turn_up, 'Up')
        self.screen.onkey(self.snake.turn_down, 'Down')
        self.screen.onkey(self.snake.turn_left, 'Left')
        self.screen.onkey(self.snake.turn_right, 'Right')
        self.screen.onkey(self.restart, 'r')
        self.screen.onkey(self.quit, 'q')
