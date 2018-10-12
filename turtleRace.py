from turtle import *
from random import randint

speed(20)
penup()
goto(-140,140)
for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color("red")
ada.shape("turtle")

ada.penup()
ada.goto(-160,100)
ada.pendown()

bob = Turtle()
bob.color("blue")
bob.shape("turtle")

bob.penup()
bob.goto(-160,70)
bob.pendown()

turtle1 = Turtle()
turtle1.color("green")
turtle1.shape("turtle")

turtle1.penup()
turtle1.goto(-160,40)
turtle1.pendown()

turtle2 = Turtle()
turtle2.color("orange")
turtle2.shape("turtle")

turtle2.penup()
turtle2.goto(-160,10)
turtle2.pendown()

for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    turtle1.forward(randint(1, 5))
    turtle2.forward(randint(1, 5))
for turn in range(10):
    ada.right(36)


