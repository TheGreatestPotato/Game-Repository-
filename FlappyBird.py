












import turtle
import time

wn = turtle.Screen()
wn.title("Flappy Bird by TheGreatestPotato")
wn.bgcolor("lightblue")
wn.setup(width=500, height=800)
wn.tracer(0)

player = turtle.Turtle()
player.speed(0)
player.penup()
player.color("Orange", "yellow")
player.shape("turtle")
player.shapesize(stretch_wid=1.5, stretch_len=1.5, outline=4)
player.goto(-200, 0)
player.dx = 0
player.dy = 1

pipe1_top = turtle.Turtle()
pipe1_top.speed(0)
pipe1_top.penup()
pipe1_top.color("green")
pipe1_top.shape("square")
pipe1_top.shapesize(stretch_wid=25, stretch_len=3, outline=8)
pipe1_top.goto(300, 300)
pipe1_top.dx = -2
pipe1_top.dy = 0
pipe1_top.value = 1

pipe1_bot = turtle.Turtle()
pipe1_bot.speed(0)
pipe1_bot.penup()
pipe1_bot.color("green")
pipe1_bot.shape("square")
pipe1_bot.shapesize(stretch_wid=25, stretch_len=3, outline=8)
pipe1_bot.goto(300, -300)
pipe1_bot.dx = -2
pipe1_bot.dy = 0

pipe2_top = turtle.Turtle()
pipe2_top.speed(0)
pipe2_top.penup()
pipe2_top.color("grey")
pipe2_top.shape("square")
pipe2_top.shapesize(stretch_wid=25, stretch_len=3, outline=8)
pipe2_top.goto(600, 350)
pipe2_top.dx = -2
pipe2_top.dy = 0
pipe2_top.value = 1

pipe2_bot = turtle.Turtle()
pipe2_bot.speed(0)
pipe2_bot.penup()
pipe2_bot.color("grey")
pipe2_bot.shape("square")
pipe2_bot.shapesize(stretch_wid=25, stretch_len=3, outline=8)
pipe2_bot.goto(600, -250)
pipe2_bot.dx = -2
pipe2_bot.dy = 0

pipe3_top = turtle.Turtle()
pipe3_top.speed(0)
pipe3_top.penup()
pipe3_top.color("orange")
pipe3_top.shape("square")
pipe3_top.shapesize(stretch_wid=25, stretch_len=3, outline=8)
pipe3_top.goto(900, 200)
pipe3_top.dx = -2
pipe3_top.dy = 0
pipe3_top.value = 1

pipe3_bot = turtle.Turtle()
pipe3_bot.speed(0)
pipe3_bot.penup()
pipe3_bot.color("orange")
pipe3_bot.shape("square")
pipe3_bot.shapesize(stretch_wid=25, stretch_len=3, outline=8)
pipe3_bot.goto(900, -400)
pipe3_bot.dx = -2
pipe3_bot.dy = 0

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.color("black")
pen.goto(0,350)
pen.write("0", move=False, align="left", font=("Arial", 32, "normal"))

gravity = -0.3

# Define function / method
def go_up():
    player.dy += 8

    if player.dy > 8:
        player.dy = 8

# Keyboard binding
wn.listen()
wn.onkeypress(go_up, "space")

# Initialize game variables
player.score = 0



# Main Game Loop
while True:
    #Pause
    time.sleep(0.02)
    # Update the screen
    wn.update()

    # Add gravity
    player.dy += gravity

    # Move player
    y = player.ycor()
    y += player.dy
    player.sety(y)

    # Bottom Border
    if player.ycor() < -390:
        player.dy = 0
        player.sety(-390)

    # Move the pipes
    x = pipe1_top.xcor()
    x += pipe1_top.dx
    pipe1_top.setx(x) 

    x = pipe1_bot.xcor()
    x += pipe1_bot.dx
    pipe1_bot.setx(x)

    x = pipe2_top.xcor()
    x += pipe2_top.dx
    pipe2_top.setx(x)

    x = pipe2_bot.xcor()
    x += pipe2_bot.dx
    pipe2_bot.setx(x)

    x = pipe3_top.xcor()
    x += pipe3_top.dx
    pipe3_top.setx(x)

    x = pipe3_bot.xcor()
    x += pipe3_bot.dx
    pipe3_bot.setx(x)

    #Return pipes to start
    if pipe1_top.xcor() < -350:
        pipe1_top.setx(600)
        pipe1_bot.setx(600)
        pipe1_top.value = 1

    if pipe2_top.xcor() < -350:
        pipe2_top.setx(600)
        pipe2_bot.setx(600)
        pipe2_top.value = 1

    if pipe3_top.xcor() < -350:
        pipe3_top.setx(600)
        pipe3_bot.setx(600)
        pipe3_top.value = 1


    # Check for collisions with pipes
    # Pipe 1
    if (player.xcor() + 30 > pipe1_top.xcor() - 30) and (player.xcor() - 30 < pipe1_top.xcor() + 30):
        if (player.ycor() + 30 > pipe1_top.ycor() - 180) or (player.ycor() - 30 < pipe1_bot.ycor() + 180):
            print("Game Over")
            wn.update()
            time.sleep(3)
            # Reset score
            player.score = 0
            pen.clear()
            pen.write(player.score, move=False, align="left", font=("Arial", 32, "normal"))
            # Move Pipes Back
            pipe1_top.setx(300)
            pipe1_bot.setx(300)
            pipe2_top.setx(600)
            pipe2_bot.setx(600)
            pipe3_top.setx(900)
            pipe3_bot.setx(900)
            # Move Player back
            player.goto(-200, 0)
            player.dy = 0


    # Check for score
    if pipe1_top.xcor() + 30 < player.xcor() - 10:
        player.score += pipe1_top.value
        pipe1_top.value = 0
        pen.clear()
        pen.write(player.score, move=False, align="left", font=("Arial", 32, "normal"))

    if pipe2_top.xcor() + 30 < player.xcor() - 10:
        player.score += pipe2_top.value
        pipe2_top.value = 0
        pen.clear()
        pen.write(player.score, move=False, align="left", font=("Arial", 32, "normal"))

    # Check for collisions with pipes
    # Pipe 2

    if (player.xcor() + 30 > pipe2_top.xcor() - 30) and (player.xcor() - 30 < pipe2_top.xcor() + 30):
        if (player.ycor() + 30 > pipe2_top.ycor() - 180) or (player.ycor() - 30 < pipe2_bot.ycor() + 180):
            print("Game Over")
            wn.update()
            time.sleep(3)
            # Reset score
            player.score = 0
            pen.clear()
            pen.write(player.score, move=False, align="left", font=("Arial", 32, "normal"))
            # Move Pipes Back
            pipe1_top.setx(300)
            pipe1_bot.setx(300)
            pipe2_top.setx(600)
            pipe2_bot.setx(600)
            pipe3_top.setx(900)
            pipe3_bot.setx(900)
            # Move Player back
            player.goto(-200, 0)
            player.dy = 0

        # Check for collisions with pipes
        # Pipe 3
    if (player.xcor() + 30 > pipe3_top.xcor() - 30) and (player.xcor() - 30 < pipe3_top.xcor() + 30):
        if (player.ycor() + 30 > pipe3_top.ycor() - 180) or (player.ycor() - 30 < pipe3_bot.ycor() + 180):
            print("Game Over")
            wn.update()
            time.sleep(3)
            # Reset score
            player.score = 0
            pen.clear()
            pen.write(player.score, move=False, align="left", font=("Arial", 32, "normal"))
            # Move Pipes Back
            pipe1_top.setx(300)
            pipe1_bot.setx(300)
            pipe2_top.setx(600)
            pipe2_bot.setx(600)
            pipe3_top.setx(900)
            pipe3_bot.setx(900)
            # Move Player back
            player.goto(-200, 0)
            player.dy = 0


    if pipe2_top.xcor() + 30 < player.xcor() - 10:
        player.score += pipe2_top.value
        pipe2_top.value = 0
        print("Score: {}".format(player.score))




























wn.mainloop()
