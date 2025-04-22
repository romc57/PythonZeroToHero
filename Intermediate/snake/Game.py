from turtle import Screen
from SnakeObj import Snake
from Food import Food

SNAKE_INIT_SIZE = 3

class Game:

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake sssss")
        self.screen.tracer(SNAKE_INIT_SIZE)
        self.snake = Snake(SNAKE_INIT_SIZE)
        self.food = Food()
        self.screen.update()
        self.screen.onkey(self.snake.turn_up, 'Up')
        self.screen.onkey(self.snake.turn_down, 'Down')
        self.screen.onkey(self.snake.turn_left, 'Left')
        self.screen.onkey(self.snake.turn_right, 'Right')
        self.screen.listen()
        self.score = 0
        self.game_loop()

    def game_loop(self):
        while self.score < 30:
            self.screen.tracer(self.snake.size)
            self.snake.move()
            self.screen.update()
            self.snake.move()
            if self.check_violations():
                self.present_results()
                break
            if self.snake.eating_this(self.food.get_pos()):
                self.ate_that()


    def check_violations(self):
        if self.snake.check_intersection():
            return True
        head = self.snake.get_location()
        if 300 - abs(head[0]) < 10 or 300 - abs(head[1]) < 10:
            return True
        return False

    def present_results(self):
        pass

    def ate_that(self):
        self.update_score()
        self.food.set_pos()


    def update_score(self):
        self.score += 1
        print(self.score)
        # update board
