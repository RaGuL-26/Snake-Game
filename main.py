import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
screen = Screen()
screen.setup(800,800)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')
game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        score.inc_score()
        snake.extend()
    if snake.turtles[0].xcor()>380 or snake.turtles[0].xcor()<-380 or snake.turtles[0].ycor()>380 or snake.turtles[0].ycor()<-380:
        game_on=False
        score.game_over()
    for seg in snake.turtles[1:]:
        if snake.turtles[0].distance(seg) < 5:
            game_on = False
            score.game_over()


screen.exitonclick()
