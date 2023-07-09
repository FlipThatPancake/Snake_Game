from turtle import Screen

class Background:

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor('black')
        self.screen.title('My Snake Game')
        self.screen.tracer(0)
