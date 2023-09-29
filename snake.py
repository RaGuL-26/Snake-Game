from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST=20
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()

    def create_snake(self):
        for pos in START_POS:
            self.add_turtles(pos)

    def add_turtles(self,pos):
        new_turtle = Turtle('circle')
        new_turtle.color('red')
        new_turtle.penup()
        new_turtle.goto(pos)
        self.turtles.append(new_turtle)

    def extend(self):
        self.add_turtles(self.turtles[-1].position())



    def move(self):
        for movement in range(len(self.turtles) - 1, 0, -1):
            pos_x = self.turtles[movement - 1].xcor()
            pos_y = self.turtles[movement - 1].ycor()
            self.turtles[movement].goto(pos_x, pos_y)
        self.turtles[0].forward(MOVE_DIST)

    def up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(UP)
    def down(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(DOWN)
    def left(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(LEFT)
    def right(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(RIGHT)


