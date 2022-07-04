from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

TIME_SLEEP = 0.08
R_PADDLE_COR = (350, 0)
L_PADDLE_COR = (-350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

r_paddle = Paddle(R_PADDLE_COR)
l_paddle = Paddle(L_PADDLE_COR)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when R paddle misses
    if ball.xcor() > 380:
        scoreboard.l_scoreboard()
        ball.reset()

    # Detect when L paddle misses
    if ball.xcor() < -380:
        scoreboard.r_scoreboard()
        ball.reset()


screen.exitonclick()
