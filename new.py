import turtle

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_triangle):
    for i in range (1,4):
        some_triangle.forward(100)
        some_triangle.left(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')
    #for a square name 'me'
    me = turtle.Turtle()
    draw_square(me)
    #for a triangle called angie
    angie = turtle.Turtle()
    draw_triangle(angie)
    #for a circle
    circle1 = turtle.Turtle()
    circle1.circle(150)

    for i in range (1,37):
        draw_square(me)
        me.right(10)

    
    

    window.exitonclick()
draw_art()
