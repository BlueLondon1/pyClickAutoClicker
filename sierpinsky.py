from turtle import *

right(30)
pu()
ht()
speed(200)

shape('triangle')
speed(10)

def sierpinski(size, order):
    if order == 0:
        stamp()
    else:
        for i in range(0,3):
            forward(size)
            sierpinski(size/2, order-1)
            backward(size)
            left(120)

sierpinski(300, 6)

input('type shift F5 for leave')