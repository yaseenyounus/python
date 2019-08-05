import turtle

window = turtle.Screen()
window.bgcolor("black")
window.screensize(600,600)
window.title("Space Invaders")

print(window.screensize())

# Draw a border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-300, -300)
border.pensize(3)
border.pendown()
for i in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()

# Draw my spaceship
ship = turtle.Turtle()
ship.speed(0)
ship.color("blue")
ship.shape("triangle")
ship.setheading(90)
ship.penup()
ship.setposition(0,-250)

# Make ship move
ship_speed = 15

def shipLeft():
    # Do not let ship pass border
    if ship.xcor() < -270:
        ship.setx(-270)
    x = ship.xcor() - ship_speed
    ship.setx(x)
def shipRight():
    # Do not let ship pass border
    if ship.xcor() > 270:
        ship.setx(270)
    x = ship.xcor() + ship_speed
    ship.setx(x)

# Draw bad guy ships
bad_guys = turtle.Turtle()
bad_guys.color("red")
bad_guys.shape("circle")
bad_guys.penup()
bad_guys.speed(0)
bad_guys.setposition(0, 250)

# Ships shoot
ship_fire = turtle.Turtle()
ship_fire.speed(0)
ship_fire.color("orange")
ship_fire.shape("triangle")
ship_fire.shapesize(.4,.4)
ship_fire.setheading(90)
ship_fire.penup()
ship_fire.setposition(ship.xcor(), ship.ycor() + 10)

fire_speed = 20
ship_fire.hideturtle()

def fire():
    ship_fire.setposition(ship.xcor(), ship.ycor() + 10)
    ship_fire.showturtle()

# Bad guys back and forth
bad_speed = 2

# Use keys to move ship
turtle.listen()
turtle.onkey(shipLeft, "Left")
turtle.onkey(shipRight, "Right")
turtle.onkey(fire, "space")


# Play loop
while True:
    x = bad_guys.xcor() + bad_speed
    bad_guys.setx(x) 
    
    if x > 280 or x < -280:
        bad_speed *= -1
        bad_guys.sety(bad_guys.ycor() - 30)

    ship_fire.sety(ship_fire.ycor() + fire_speed)





delay = input("Click enter to exit")
