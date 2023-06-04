import turtle

def draw_origami_star():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Origami Star")

    pen = turtle.Turtle()
    pen.speed(2)

    colors = ["red", "orange", "yellow", "green", "blue", "purple"] #color for blades

    #drawing the blades
    for i in range(12):
        pen.color(colors[i % len(colors)])
        pen.begin_fill()
        for _ in range(2):
            pen.forward(100)
            pen.left(45)
            pen.forward(100)
            pen.left(135)
        pen.end_fill()
        pen.left(30)

    #hiding the turtle
    pen.hideturtle()

    #exit on when cilck
    screen.exitonclick()

#call the function to draw the origami star
draw_origami_star()

