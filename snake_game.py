import turtle
import time
import random

delay = 0.1

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle("square", "black")
head.penup()

# Snake food
food = turtle.Turtle("circle", "red")
food.penup()
food.goto(0, 100)

# Pen
pen = turtle.Turtle("square", "white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Score
score, high_score = 0, 0

# Functions
def go(direction):
    def move():
        if head.direction != direction:
            head.direction = direction

    return move

wn.listen()
wn.onkeypress(go("up"), "w")
wn.onkeypress(go("down"), "s")
wn.onkeypress(go("left"), "a")
wn.onkeypress(go("right"), "d")

# Main game loop
while True:
    wn.update()

    # Check for collision with the border
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        pen.clear()
        pen.write("Score: 0  High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal"))
        time.sleep(1)

    # Check for collision with the food
    if head.distance(food) < 20:
        x, y = random.randint(-290, 290), random.randint(-290, 290)
        food.goto(x, y)
        delay -= 0.001
        score += 10
        high_score = max(high_score, score)
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the snake
    x, y = head.xcor(), head.ycor()
    head.setx(x + 20) if head.direction == "right" else head.setx(x - 20)
    head.sety(y + 20) if head.direction == "up" else head.sety(y - 20)

    # Check for head collision with body segments
    for segment in segments[1:]:
        if head.distance(segment) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: 0  High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal"))

    # Move the segments
    if len(segments) > 0:
        x, y = head.xcor(), head.ycor()
        segments[0].goto(x, y)
        segments = [head] + segments[:-1]

    time.sleep(delay)
