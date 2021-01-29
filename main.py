import turtle as t
import random
t.colormode(255)
import colorgram

# def random_color():
#     r = random.randrange(0, 256, 10)
#     g = random.randrange(0, 256, 10)
#     b = random.randrange(0, 256, 10)
#     colors = (r, g, b)
#     return colors
# #
# def draw_circle():
#     turtle.color(random_color())
#     turtle.circle(100)
#
# angle = 0
# while angle <= 360:
#     draw_circle()
#     angle += 4
#     turtle.setheading(angle)
#
# extract_color = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     extract_color.append((color.rgb.r, color.rgb.b, color.rgb.b))
# print(extract_color)

color_list = [(144, 49, 49), (188, 120, 120), (166, 35, 35), (14, 83, 83), (45, 137, 137), (142, 175, 175), (146, 82, 82), (59, 100, 100), (141, 177, 177), (86, 29, 29), (63, 169, 169), (219, 94, 94), (112, 30, 30), (101, 111, 111), (166, 129, 129), (94, 170, 170), (169, 162, 162), (178, 83, 83), (206, 195, 195), (50, 90, 90), (71, 55, 55), (93, 63, 63), (172, 193, 193), (172, 204, 204), (14, 81, 81), (4, 119, 119)]
turtle = t.Turtle()
turtle.speed(0)
turtle.penup()
turtle.hideturtle()


def dot_line():
    for _ in range(0, 10):
        color = random.choice(color_list)
        turtle.color(color)
        turtle.dot(20)
        turtle.forward(50)


for _ in range(0, 10):
    position = turtle.position()
    dot_line()
    turtle.setpos(position)
    turtle.setheading(90)
    turtle.forward(50)
    turtle.right(90)


screen = t.Screen()
screen.exitonclick()
