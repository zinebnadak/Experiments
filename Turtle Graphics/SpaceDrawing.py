import turtle
import random

### Screen and background ###
screen = turtle.Screen()
screen.colormode(255) # Set color mode to accept 0–255 RGB values. HEX number do not need this!
screen.bgcolor((25, 24, 84)) #bg stands for background, HEX number (#191854)

### Moon ###
# Create turtle for the moon
moon = turtle.Turtle()
moon.hideturtle() #makes turtle invisible on screen
moon.speed(0)
moon.penup() #lifts the pen so it stops drawing when it moves

# Position moon in bottom-left corner
moon.goto(-280, -300)  # x=left(-), right(+). y =bottom(-), top(+)
moon.pendown()

# Draw the moon
moon.color("light gray")
moon.begin_fill() #Turtle starts remembering the shape so it can fill it in later
moon.circle(220)  # Big circle for the moon
moon.end_fill()


# === BOTTOM LEFT: ALIENS ===
num_aliens = int(input("How many One-eyed Aliens on the moon?: "))

#Create turtle for aliens
alien = turtle.Turtle()
alien.hideturtle()
alien.speed(0)
alien.pensize(2)
alien.color("green")

for i in range(num_aliens):     #runs "num_aliens" times, and each time it picks a random position for one alien.
    x = random.randint(-300, -50)
    y = random.randint(-300, -50)

    # Draw body (rectangle)
    alien.penup()
    alien.goto(x - 5, y)
    alien.pendown()
    alien.begin_fill()
    alien.goto(x + 5, y)
    alien.goto(x + 5, y + 30)
    alien.goto(x - 5, y + 30)
    alien.goto(x - 5, y)
    alien.end_fill()

    # Draw head (big circle) on top of body
    head_radius = 15
    alien.penup()
    alien.goto(x, y + 30)  # move to top of body
    alien.pendown()
    alien.begin_fill()
    alien.circle(head_radius)
    alien.end_fill()

    # Draw legs
    alien.penup()
    alien.goto(x - 3, y)
    alien.pendown()
    alien.goto(x - 3, y - 10)
    alien.penup()
    alien.goto(x + 3, y)
    alien.pendown()
    alien.goto(x + 3, y - 10)
    alien.penup()

    # Draw arms
    alien.penup()
    alien.goto(x - 5, y + 20)
    alien.pendown()
    alien.goto(x - 15, y + 25)
    alien.penup()
    alien.goto(x + 5, y + 20)
    alien.pendown()
    alien.goto(x + 15, y + 25)
    alien.penup()

    # Draw two angled lines on the head (same direction as arms)
    alien.pensize(2)
    # Left antenna
    alien.penup()
    alien.goto(x - 5, y + 30 + head_radius - 3)  # a bit below the top edge of head
    alien.setheading(140)  # angle similar to left arm
    alien.pendown()
    alien.forward(20)
    alien.penup()
    # Right antenna
    alien.goto(x + 5, y + 30 + head_radius - 3)  # a bit below the top edge of head
    alien.setheading(40)  # angle similar to right arm
    alien.pendown()
    alien.forward(20)
    alien.penup()
    alien.setheading(0)  # reset heading


    # Draw big white eye (circle)
    alien.penup()
    alien.goto(x, y + 30 + head_radius)  # center of head
    alien.pendown()
    alien.color("white")
    alien.begin_fill()
    alien.circle(7)  # big white eye radius
    alien.end_fill()
    # Draw small black pupil inside of white eye start from middle , go down
    alien.penup()
    alien.goto(x, y + 30 + head_radius)  # same center
    alien.pendown()
    alien.color("black")
    alien.begin_fill()
    alien.circle(3)  # smaller black pupil radius
    alien.end_fill()
    alien.color("green")  # Reset color for next drawing in loop

# === BOTTOM RIGHT: Colored swirls ===
swirl_num = int(input("How many colorful Swirls in space?: "))

#create turtle for swirls
swirl = turtle.Turtle()
swirl.pensize(3)
swirl.speed(0)
swirl.hideturtle()

for i in range(swirl_num):
    x = random.randint(50, 300)  # upper-right x range
    y = random.randint(-300, -50)  # upper-right y range

    # Move to random start position
    swirl.penup()
    swirl.goto(x, y)
    swirl.pendown()

    # Random color for each swirl
    r = random.randint(100, 255)
    g = random.randint(100, 255)
    b = random.randint(100, 255)
    swirl.color((r, g, b))

    # Draw a swirl
    length = 2      #how big start lenght
    angle = 50      #how tight turns will be
    for _ in range(30):     #how many turns
        swirl.forward(length)
        swirl.right(angle)
        length = length + 1  # amount of growth increase


# === TOP RIGHT: Stars ===
stars_num = int(input("How many yellow Stars in space!: "))

#create turtle for stars
star = turtle.Turtle()
star.pensize(8)
star.speed(0)
star.hideturtle()
turtle.colormode(255)  # Enable RGB colors

for i in range(stars_num):
    x = random.randint(50, 300)  # upper-right x range
    y = random.randint(50, 300)  # upper-right y range

    # Generate random yellow-ish color (R and G high, no Blue)
    r = random.randint(230, 255)
    g = random.randint(200, 255)
    b = random.randint(0, 0)

    # Set colors
    star.color((r, g, b))
    star.fillcolor((r, g, b))

    # Move and draw star
    star.penup()
    star.goto(x, y)
    star.setheading(0)
    star.pendown()

    # Draw 5-point star
    size = random.randint(30, 50)
    star.begin_fill()
    for i in range(5):
        star.forward(size)
        star.right(144)
    star.end_fill()

turtle.done()
screen.exitonclick()  # keep window open until close or run again

