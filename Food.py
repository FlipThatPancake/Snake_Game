
from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('green')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        ran_x = random.choice(range(-260, 260, 20))
        ran_y = random.choice(range(-260, 260, 20))
        self.goto(ran_x, ran_y)