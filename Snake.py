from turtle import Turtle

STARTING_POSTIONS = [(0.00, 0.00), (-20, 0.00), (-40, 0.00)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, screen):
        self.the_snake = []
        self.generate_snake()
        self.snake_head = self.the_snake[0]
        self.screen = screen.screen

    def generate_snake(self):
        for _ in STARTING_POSTIONS:
            self.add_segment(_)

    def add_segment(self, position):
        self.segment = Turtle(shape='square')
        self.segment.color('white')
        self.segment.penup()
        self.segment.setpos(position)
        self.the_snake.append(self.segment)

    def reset_func(self):
        for index, segment in enumerate(self.the_snake):
            if index == 0:
                segment.setpos(STARTING_POSTIONS[0])
            elif index == 1:
                segment.setpos(STARTING_POSTIONS[1])
            elif index == 2:
                segment.setpos(STARTING_POSTIONS[2])
            else:
                segment.hideturtle()
                self.the_snake.remove(segment)
        self.snake_head.seth(RIGHT)
        print(self.snake_head.position())


    def extend(self):
        self.add_segment(position=self.the_snake[-1].position())

    def move(self):
        for segment in range(len(self.the_snake) - 1, 0, -1):
            goto_x = self.the_snake[segment - 1].xcor()
            goto_y = self.the_snake[segment - 1].ycor()
            self.the_snake[segment].goto(goto_x, goto_y)
        self.snake_head.fd(MOVE_DISTANCE)

    def start_listening(self):
        self.screen.onkey(self.up, 'Up')
        self.screen.onkey(self.down, 'Down')
        self.screen.onkey(self.left, 'Left')
        self.screen.onkey(self.right, 'Right')
        self.screen.listen()

    # def stop_listening(self):
    #     self.screen.onkey(None, "up")
    #     self.screen.onkey(None, 'Down')
    #     self.screen.onkey(None, 'Left')
    #     self.screen.onkey(None, 'Right')
    #     self.screen.listen()

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.seth(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.seth(DOWN)


    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.seth(LEFT)


    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.seth(RIGHT)
