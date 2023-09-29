from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.penup()
        self.goto(0, 360)
        self.hideturtle()
        self.update_score()

    def inc_score(self):
        self.score+=1
        self.clear()
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over! :( Your Score Is: {self.score}",align="center",font=("Arial",24,"normal"))

    def update_score(self):
        self.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))
