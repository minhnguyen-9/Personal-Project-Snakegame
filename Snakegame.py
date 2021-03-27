#This is my first ever game
#Just like the one everyone played when they were young

import random 

WINDOW_HEIGHT = 480
WINDOW_WIDTH = 640

class Snake:
    def __init__(self):
        self.snake_head = [100, 50]
        self.snake_direction = "RIGHT"
        self.snake_body = [
            self.snake_head,
            [self.snake_head[0] - 10, self.snake_head[1]],
            [self.snake_head[0] - 20, self.snake_head[1]]
        ]

    def snake_change_direction(self, new_direction: str):
        if new_direction == self.snake_direction:
            return
        if self.snake_direction == 'DOWN' and new_direction == 'UP':
            return
        if self.snake_direction == 'UP' and new_direction == 'UP':
            return
        if self.snake_direction == 'LEFT' and new_direction == 'UP':
            return
        if self.snake_direction == 'RIGHT' and new_direction == 'UP':
            return
        salf.snake_direction = new_direction

    def snake_move(self):
        if self.snake_direction == 'UP':
            new_snake_head = [self.snake_head[0], self.snake_head[1] + 10]
        if self.snake_direction == 'DOWN':
            new_snake_head = [self.snake_head[0], self.snake_head[1] - 10]
        if self.snake_direction == 'RIGHT':
            new_snake_head = [self.snake_head[0] + 10, self.snake_head[1]]
        if self.snake_direction == 'LEFT':
            new_snake_head = [self.snake_head[0] - 10, self.snake_head[1]] 
        self.snake_body.insert(0, new_snake_head)
        self.snake_body.pop()

    def snake_eat(self):
        self.snake_body.insert(0, self.snake_head)
        self.snake_move()


class Food:
    def __init__(self):
        self.position = [100, 100]

    def food_repawn(self):
        self.position = [random.randrange(1, WINDOW_HEIGHT // 10) *10,
                         random.randrange(1, WINDOW_HEIGHT // 10) * 10]

class Score:
    def __init__(self):
        self.score = 0

    def increase(self):
        self.score += 1

class Game:

    def __init__(self):
        self.snake = Snake()

    def game_over(self):
        if self.snake.snake.head[0] < 0 or self.snake.snake_head[0] > WINDOW_WIDTH:
            return null
        if self.snake.snake.head[0] < 0 or self.snake.snake_head[0] > WINDOW_HEIGHT:
            return null

        for block in self.snake.snake_body[1:]:
            if block[0] == self.snake.snake_head[0] and block[1] == self.snake.snake_head[1]:
                return null
    



