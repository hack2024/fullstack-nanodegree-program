import turtle

def draw_art():

    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.color("green")
    brad.speed(1)
    brad.shape("turtle")
        
    #draw_circle(brad)
    draw_name(brad)
    #draw_sierpinski(brad,100,2)

    window.exitonclick()

def draw_square(some_turtle):

    for _ in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle(some_turtle):

    for _ in range(1,37):
        draw_square(some_turtle)
        some_turtle.right(10)

def draw_name(some_turtle):
    
    #F
    some_turtle.left(90)
    some_turtle.forward(100)
    some_turtle.right(90)
    some_turtle.forward(40)
    some_turtle.up()
    some_turtle.setpos(0,50)
    some_turtle.down()
    some_turtle.forward(40)
    #B
    some_turtle.up()
    some_turtle.setpos(60,0)
    some_turtle.down()
    some_turtle.left(90)
    some_turtle.forward(100)
    some_turtle.right(90)
    some_turtle.circle(-25,180)
    some_turtle.left(180)
    some_turtle.circle(-25,180)

def draw_sierpinski(some_turtle,length,depth):
    if depth==0:
        for i in range(0,3):
            some_turtle.fd(length)
            some_turtle.left(120)
    else:
        draw_sierpinski(some_turtle,length/2,depth-1)
        some_turtle.fd(length/2)
        draw_sierpinski(some_turtle,length/2,depth-1)
        some_turtle.bk(length/2)
        some_turtle.left(60)
        some_turtle.fd(length/2)
        some_turtle.right(60)
        draw_sierpinski(some_turtle,length/2,depth-1)
        some_turtle.left(60)
        some_turtle.bk(length/2)
        some_turtle.right(60)

draw_art()