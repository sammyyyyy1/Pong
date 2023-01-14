from turtle import Turtle, Screen
from paddle import Paddle
from wall import Wall
import time
from ball import Ball


screen = Screen()
screen.title("pong")
screen.setup(width=750, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

game = True

paddles = []
paddle_1 = Paddle()
paddle_2 = Paddle()
paddle_1.reset(-225)
paddle_2.reset(225)
paddles.append(paddle_1)
paddles.append(paddle_2)
movements = []
score = [0, 0]
ball = Ball()

wall_1 = Wall("horizontal")
wall_1.wall.goto(x=-150, y=260)
wall_2 = Wall("horizontal")
wall_2.wall.goto(x=-150, y=-260)
wall_3 = Wall("vertical")
wall_3.wall.goto(x=-350, y=0)
wall_4 = Wall("vertical")
wall_4.wall.goto(x=50, y=0)

show_score = Turtle()


def move_left_1():
    if movements.count(paddles[0].move_left) == 0:
        movements.append(paddles[0].move_left)
        stop_right_1()


def move_right_1():
    if movements.count(paddles[0].move_right) == 0:
        movements.append(paddles[0].move_right)
        stop_left_1()


def move_left_2():
    if movements.count(paddles[1].move_left) == 0:
        movements.append(paddles[1].move_left)
        stop_right_2()


def move_right_2():
    if movements.count(paddles[1].move_right) == 0:
        movements.append(paddles[1].move_right)
        stop_left_2()


def stop_left_1():
    if movements.count(paddles[0].move_left) > 0:
        movements.remove(paddles[0].move_left)


def stop_left_2():
    if movements.count(paddles[1].move_left) > 0:
        movements.remove(paddles[1].move_left)


def stop_right_1():
    if movements.count(paddles[0].move_right) > 0:
        movements.remove(paddles[0].move_right)


def stop_right_2():
    if movements.count(paddles[1].move_right) > 0:
        movements.remove(paddles[1].move_right)


def move_paddles():
    for fun in movements:
        fun()


def check_wall_collision():
    for i in range(0, 2):
        if paddles[i].pad.xcor() <= -300 and movements.count(paddles[i].move_left) > 0:
            movements.remove(paddles[i].move_left)
        if paddles[i].pad.xcor() >= 0 and movements.count(paddles[i].move_right) > 0:
            movements.remove(paddles[i].move_right)


def check_ball_hit_wall():
    if ball.xcor() > 40 or ball.xcor() < -340:
        ball.bounce_x()


def check_ball_hit_paddle():
    for pad in paddles:
        if abs(pad.pad.xcor()-ball.xcor()) < 40 and abs(pad.pad.ycor()-ball.ycor()) < 10:
            ball.bounce_y()


def check_ball_out():
    global game
    if ball.ycor() < -250:
        wall_2.wall.color("red")
        game = False
        score[0] += 1
    if ball.ycor() > 250:
        wall_1.wall.color("red")
        game = False
        score[1] += 1


def display_score():
    show_score.penup()
    show_score.hideturtle()
    show_score.color("white")
    show_score.goto(x=200, y=0)
    show_score.write(f"{score[0]} - {score[1]}", align="center", font=('Arial', 48, 'bold'))


def reset_game():
    global game, score, ball
    if not game:
        ball.reset()
        ball = Ball()
        game = True
        wall_1.wall.color("white")
        wall_2.wall.color("white")
        show_score.reset()
        display_score()
        play()


def play():
    while game:
        screen.onkeypress(key="a", fun=move_left_1)
        screen.onkeypress(key="d", fun=move_right_1)
        screen.onkeypress(key="Left", fun=move_left_2)
        screen.onkeypress(key="Right", fun=move_right_2)
        screen.onkeyrelease(key="a", fun=stop_left_1)
        screen.onkeyrelease(key="d", fun=stop_right_1)
        screen.onkeyrelease(key="Left", fun=stop_left_2)
        screen.onkeyrelease(key="Right", fun=stop_right_2)
        check_wall_collision()
        check_ball_hit_wall()
        check_ball_hit_paddle()
        check_ball_out()
        move_paddles()
        ball.move()
        screen.update()
        time.sleep(0.01)


display_score()
play()
screen.onkey(key="space", fun=reset_game)
screen.exitonclick()
