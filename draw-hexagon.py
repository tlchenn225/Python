# use turtle module to draw a hexagon
import turtle

# declare colors that will be used in each line direction
colors = ["gold", "green", "maroon", "orange", "purple", "turquoise"]

# turtle settings
screen.title("Rainbow Hexagon")
screen.setup(width=200, height=200)
t = turtle.Pen()

# set background color to black for contrast
turtle.bgcolor('black')

# draw hexagon
for i in range(360):
    t.pencolor(colors[i % 6])
    t.width(i//200 + 1)
    t.forward(i)
    t.left(58)


