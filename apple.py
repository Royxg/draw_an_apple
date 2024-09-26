import turtle

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.pensize(3)
pen.speed(5)


pen.color("red")
pen.begin_fill()
pen.circle(100)  
pen.end_fill()


pen.penup()
pen.goto(-30, 120)
pen.pendown()


pen.color("brown")
pen.pensize(5)
pen.right(45)
pen.forward(50)


pen.penup()
pen.goto(-30, 120)
pen.pendown()
pen.color("green")
pen.pensize(2)
pen.begin_fill()
pen.circle(30, 90)  
pen.left(90)
pen.circle(30, 90)  
pen.end_fill()


pen.hideturtle()
turtle.done()

