from turtle import *
import time


def triangle(number: int, size: int, color: str):
    for number in range(number):
        begin_fill()
        fillcolor(color)
        forward(100)
        for _ in range(3):      
            forward(size)
            left(120)
        end_fill()
    input('press any Shift F5 for leave')
    
    
triangle(3 , 100 ,'blue')