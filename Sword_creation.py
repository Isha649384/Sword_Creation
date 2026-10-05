import turtle

paper = turtle.Screen()
paper.setup(400,400)
paper.bgcolor("white")

pen = turtle.Turtle()
pen.color("black")
pen.speed(10)

pen.penup()
pen.right(90)
pen.forward(450)
pen.right(180)
pen.pendown()

# The Grip
pen.fillcolor("brown")
pen.begin_fill()
pen.forward(250)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(250)
pen.right(90)
pen.forward(25)
pen.end_fill()

# The Pommel
pen.dot(75)

pen.penup()
pen.right(90)
pen.forward(250)
pen.left(90)
pen.forward(25)
pen.pendown()

# The guard
pen.fillcolor("black")
pen.begin_fill()
pen.forward(50)
pen.right(90)
pen.forward(30)
pen.right(90)
pen.forward(150)
pen.right(90)
pen.forward(30)
pen.right(90)
pen.forward(100)
pen.end_fill()

pen.penup()
pen.forward(25)
pen.right(90)
pen.forward(30)
pen.pendown()

# The Blade
pen.fillcolor("grey")
pen.begin_fill()
pen.forward(350)
pen.right(45)
pen.forward(75)
pen.right(90)
pen.forward(75)
pen.right(45)
pen.forward(350)

# The Fuller
pen.right(90)
pen.forward(100)
pen.right(180)
pen.forward(47)
pen.end_fill()
pen.begin_fill()
pen.left(90)
pen.forward(410)
pen.end_fill()
turtle.done()