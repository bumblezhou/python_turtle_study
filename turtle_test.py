import turtle

turtle.title("My Turtle Program")
turtle.bgcolor("green")

t = turtle.Turtle()

#Change tutle size
t.shapesize(1,5,10)
t.shapesize(10,5,1)
t.shapesize(1,10,5)
t.shapesize(10,1,5)

#Change pen size
t.pensize(5)
t.forward(100)

#Change turtle size and color
t.shapesize(3,3,3)
t.fillcolor("red")
t.pencolor("green")

#Change turtle pen color and fill color
t.color("blue", "red")

#Go anywhere on screen
t.right(90)
t.forward(100)
t.left(90)
t.backward(100)
t.goto(100,100)

t.home()

#Drawing a Shape
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)

#Drawing circle
t.circle(60)

#Drawing dot
t.dot(20)

#Fill area with special color
t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()

#Change turtle shapesize: square, arrow, circle, turtle, triangle, classic
t.shape("turtle")
t.shape("arrow")
t.shape("circle")

#Change the pen speed
t.speed(1)
t.forward(100)
t.speed(10)
t.forward(100)

#One line to draw a circle
t.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
t.begin_fill()
t.circle(90)
t.end_fill()

#Picking the pen up and down
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.rt(90)
t.pendown()
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.pendown()

#Undoing changes
t.undo()

#Clear the screen
t.clear()

#Clone the turtle
c = t.clone()
t.color("magenta")
c.color("red")
t.circle(100)
c.circle(60)

turtle.mainloop()