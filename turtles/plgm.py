import turtle

turtle.speed(0)

def sqr(side):
    for i in range(4):
        turtle.fd(side)
        turtle.lt(90)
        
def llgm(side,angle):
    for i in range(2):
        turtle.fd(side)
        turtle.lt(angle)
        turtle.fd(side)
        turtle.lt(180-angle)
        
def grid(rows,cols):
    for i in range(rows):
        row(cols)
        turtle.pu()
        turtle.bk(cols*40)
        turtle.rt(90)
        turtle.fd(40)
        turtle.lt(90)
        turtle.pd()

def row(n):
    for i in range(n):
        llgm(30,120)
        turtle.pu()
        turtle.fd(40)
        turtle.pd()

grid(4,4)
turtle.exitonclick()
