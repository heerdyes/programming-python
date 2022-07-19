import turtle

turtle.speed(0)

for i in range(4):
    for j in range(3):
        # square
        for z in range(4):
            turtle.fd(30)
            turtle.lt(90)
        turtle.pu()
        turtle.fd(40)
        turtle.pd()
    turtle.pu()
    turtle.bk(3*40)
    turtle.rt(90)
    turtle.fd(40)
    turtle.lt(90)
    turtle.pd()

turtle.exitonclick()
