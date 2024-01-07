import turtle
import time
import random

delay = 0.3
score = 0
bonus_counter = 0
paused = False

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")  # Changing shape to round
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Right"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Bonus food
bonus_food = turtle.Turtle()
bonus_food.speed(0)
bonus_food.shape("triangle")
bonus_food.color("blue")
bonus_food.penup()
bonus_food.goto(0, -100)
bonus_food.hideturtle()

segments = []
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Function to pause the game
def toggle_pause():
    global paused
    paused = not paused
    if paused:
        pen.clear()
        pen.write("Game Paused", align="center", font=("Courier", 24, "normal"))
    else:
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Function definitions
def go_up():
    if head.direction != "Down":
        head.direction = "Up"

def go_down():
    if head.direction != "Up":
        head.direction = "Down"

def go_left():
    if head.direction != "Right":
        head.direction = "Left"

def go_right():
    if head.direction != "Left":
        head.direction = "Right"

def move():
    if head.direction == "Up":
        y = head.ycor()
        head.sety(y + 20)

    elif head.direction == "Down":
        y = head.ycor()
        head.sety(y - 20)

    elif head.direction == "Left":
        x = head.xcor()
        head.setx(x - 20)

    elif head.direction == "Right":
        x = head.xcor()
        head.setx(x + 20)

def check_collision_with_border():
    return (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    )

def check_collision_with_food():
    return head.distance(food) < 20

def check_collision_with_bonus_food():
    return head.distance(bonus_food) < 20

def check_collision_with_body():
    for segment in segments:
        if head.distance(segment) < 20:
            return True
    return False

# Keyboard bindings
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")
wn.onkey(toggle_pause, "p")

while True:
    wn.update()

    if paused:
        continue  # Skip the rest of the loop if the game is paused

    if check_collision_with_border() or check_collision_with_body():
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Right"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        score = 0
        bonus_counter = 0
        delay = 0.1

        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    if check_collision_with_food():
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001  # Increase speed after eating food
        score += 10
        bonus_counter += 1

        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

        if bonus_counter == 5:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            bonus_food.goto(x, y)
            bonus_food.showturtle()

    if check_collision_with_bonus_food():
        bonus_food.hideturtle()
        bonus_counter = 0
        score += 5
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    time.sleep(delay)
