import turtle
import math

# Lab 04 Part C - American Flag using Turtle Graphics


def get_colour(colour):
    colour = colour.lower()
    if colour == "red":
        return 191, 10, 48
    elif colour == "white":
        return 255, 255, 255
    elif colour == "blue":
        return 0, 40, 104
    elif colour == "black":
        return 0, 0, 0
    else:
        return 128, 128, 128


def draw_rectangle(length, height, colour):
    r, g, b = get_colour(colour)
    turtle.color(r, g, b)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()


def draw_star(size, colour):
    r, g, b = get_colour(colour)
    turtle.color(r, g, b)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()


def draw_row_of_stars(count, start_x, y, spacing, star_size):
    for col in range(count):
        x = start_x + col * spacing
        turtle.penup()
        turtle.goto(x - star_size / 2, y + star_size * 0.3)
        turtle.setheading(0)
        draw_star(star_size, "white")


def draw_flag(height):
    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor("lightgrey")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(0)

    # Official US flag proportions from Wikipedia
    length = 1.9 * height               # B = 1.9 * A
    stripe_height = height / 13          # L = A / 13
    canton_height = 7 * stripe_height    # C = 7/13 * A
    canton_length = 0.76 * height        # D = 0.76 * A

    start_x = -length / 2
    start_y = height / 2

    # Draw 13 stripes (7 red, 6 white)
    for i in range(13):
        turtle.penup()
        turtle.goto(start_x, start_y - i * stripe_height)
        turtle.setheading(0)
        if i % 2 == 0:
            draw_rectangle(length, stripe_height, "red")
        else:
            draw_rectangle(length, stripe_height, "white")

    # Draw blue canton
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.setheading(0)
    draw_rectangle(canton_length, canton_height, "blue")

    # Draw 50 stars: 5 rows of 6 and 4 rows of 5
    row_spacing = canton_height / 10
    col_spacing = canton_length / 12
    star_size = min(row_spacing, col_spacing) * 0.55

    for row in range(9):
        y = start_y - row_spacing * (row + 1)

        if row % 2 == 0:
            # Even rows: 6 stars
            row_start_x = start_x + col_spacing
            draw_row_of_stars(6, row_start_x, y, 2 * col_spacing, star_size)
        else:
            # Odd rows: 5 stars
            row_start_x = start_x + 2 * col_spacing
            draw_row_of_stars(5, row_start_x, y, 2 * col_spacing, star_size)

    turtle.update()


def main():
    turtle.setup(1000, 700)
    draw_flag(260)
    turtle.done()


main()
