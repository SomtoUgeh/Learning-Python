import turtle

def shape():
    window = turtle.Screen()
    window.bgcolor("white")
    abc = turtle.Turtle()
    abc.shape("classic")
    abc.color("blue")
    abc.speed(10)

    abc.pu()
    abc.setpos(-200,0)
    abc.pd()

    for i in range(1,37):  
        abc.left(35)
        abc.forward(50)
        abc.right(35)
        abc.forward(50)
        abc.right(145)
        abc.forward(50)
        abc.right(35)
        abc.forward(50)
        abc.right(10)
    abc.seth(270)
    abc.forward(200)
            
shape()
