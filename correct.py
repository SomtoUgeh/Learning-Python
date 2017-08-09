import turtle

 
def draw_shape():
    window = turtle.Screen()
    window.bgcolor('red')

    draw_square()
    draw_circle()
    draw_triangle()

    window.exitonclick() 

def draw_square():
    me = turtle.Turtle()
    me.shape('turtle')
    me.color('blue')
    one_side = 0
    side_square = 4
    while (one_side < side_square):
        me.forward(100)
        me.right(90)
        one_side = one_side + 1
    
        
def draw_circle():
    angie = turtle.Turtle()
    angie.circle(100)

def draw_triangle():
    main = turtle.Turtle()
    main.shape('arrow')
    main.color('yellow')
    side = 0
    all_side = 3
    while (side < all_side):
        main.forward(100)
        main.left(120)
        side = side + 1
        
draw_shape()
