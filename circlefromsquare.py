import turtle

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')
    #for a square name 'me'
    me = turtle.Turtle()
    draw_square(me)
   

    for i in range (1,37):
        draw_square(me)
        me.right(10)

    
    

    window.exitonclick()
draw_art()
