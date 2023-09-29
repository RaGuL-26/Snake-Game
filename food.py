from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(0.5,0.5)
        self.speed(0)
        self.refresh()
    def refresh(self):
        x_axis = random.randint(-370, 370)
        y_axis = random.randint(-370, 370)
        self.goto(x_axis, y_axis)