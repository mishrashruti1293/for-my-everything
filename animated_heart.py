import turtle
import math

# ---------------- Screen ---------------- #
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Rotating Red Heart")
screen.tracer(0)

# ---------------- Heart Turtle ---------------- #
heart_t = turtle.Turtle()
heart_t.hideturtle()
heart_t.speed(0)

# ---------------- Text Turtle ---------------- #
text_t = turtle.Turtle()
text_t.hideturtle()
text_t.penup()
text_t.color("#0b1f3a")  # navy blue

# ---------------- Message ---------------- #
message = (
    "Because at the end of the day you're the person I want\n"
    "to come home to. You're the person I want to tell\n"
    "how my day went. You're the person I want to\n"
    "share my happiness, sadness, frustration,\n"
    "and success with.\n\n"
    "please don't give up on me ever ♡\n"
    "love you so much and I want to be with you forever."
)

text_t.goto(0, -35)
text_t.write(message, align="center", font=("Arial", 9, "normal"))

# ---------------- Heart Formula ---------------- #
def heart(t, scale):
    x = 16 * math.sin(t) ** 3
    y = (13 * math.cos(t)
         - 5 * math.cos(2 * t)
         - 2 * math.cos(3 * t)
         - math.cos(4 * t))
    return x * scale, y * scale

# ---------------- Animation ---------------- #
angle = 0

while True:
    heart_t.clear()
    heart_t.pensize(2)
    heart_t.pencolor("#cc0000")

    points = []

    for i in range(200):
        theta = 2 * math.pi * i / 200
        x, y = heart(theta + angle, 18)
        points.append((x, y))

    # Draw outer rotating frame only (protect text center)
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 25) % len(points)]

        # Skip center area so text stays clear
        if abs(x1) < 85 and abs(y1) < 85:
            continue

        heart_t.penup()
        heart_t.goto(x1, y1)
        heart_t.pendown()
        heart_t.goto(x2, y2)

    angle += 0.03
    screen.update()