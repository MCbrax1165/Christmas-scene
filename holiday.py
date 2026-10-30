import turtle
import random

#This is a chrstmas sceene with a redwood pine and chrstmas lights everywhere

t = turtle.Turtle()
t.speed(0)

def treetop(x, y):
    t.teleport(x - 50, y - 50)
    t.begin_fill()
    t.color("green")
    t.forward(100)
    t.left(135)
    t.forward(70.71)
    t.left(90)
    t.forward(70.71)
    t.left(135)
    t.end_fill()
def stump(x, y):
    t.color("brown")
    t.begin_fill()
    t.teleport(x - 20, y - 50)
    t.forward(40)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.end_fill()
def lights(x, y, color):
    t.color(color)
    t.teleport(x - 10, y - 10)
    t.begin_fill()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.end_fill()
if __name__ == "__main__":
    treetop(0, 200)
    treetop(0, 225)
    treetop(0, 250)
    stump(0, 100)
    for i in range(50):
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        lights(x, y, "red")
        lights(x - 50, y + 50, "blue")
        lights(x + 50, y - 50, "orange")

turtle.done()
