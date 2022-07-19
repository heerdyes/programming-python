import turtle

turtle.speed(0)

for i in range(180):
    turtle.fd(i)
    turtle.bk(i)
    turtle.lt(2)

turtle.exitonclick()

