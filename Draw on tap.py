#Copyright Jamie Westerhout
import tkinter as tk
import turtle
import random
import sqlite3
print("copyright Jamie Westerhout, 2019")
root = tk.Tk()
root.geometry('{}x{}'.format(10, 500))
frame = tk.Frame(root)
frame.pack()
turtle.bgcolor("black")
screen = turtle.Screen()
loop2 = 1
test = 1
turtle.color("red")
def pen1():
    screen.onscreenclick(draw1)
def pen2():
    screen.onscreenclick(draw2)
def pen3():
    screen.onscreenclick(draw3)
def pen4():
    turtle.penup()
    screen.onscreenclick(draw4)
def pen5():
    turtle.penup()
    screen.onscreenclick(none)
def pen7():
    turtle.penup()
    screen.onscreenclick(Record)
def none(x, y):
    turtle.penup()
    turtle.goto(x, y)
    print("nothing")
def BGBlack():
    turtle.bgcolor("black")
def BGWhite():
    turtle.bgcolor("white")
def PRed():
    turtle.pencolor("Red")
def PWhite():
    turtle.pencolor("white")
def PBlack():
    turtle.pencolor("black")
def PBlue():
    turtle.pencolor("Blue")
def Record(x, y):
    turtle.goto(x, y)
    turtle.pendown()
    f = open('CustomPen.pen','a+')
    f.write(str(float(turtle.xcor())))
    f.write(", ")
    f.write(str(float(turtle.ycor())))
    f.write("\n")
    f.close()
    print(str(turtle.pos()))
def CustomPen1():
    p = open('CustomPen.pen','r')
    turtle.penup()
    for x in p:
        x1, y1 = map(str , x.split())
        x1 = x1[:-1]
        turtle.goto(float(x1), float(y1))
        turtle.pendown()
    p.close
def draw1(x , y):
    turtle.penup()
    turtle.goto(x, y)
    Bac()
def draw2(x , y):
    turtle.penup()
    turtle.goto(x, y)
    star()
def draw3(x , y):
    turtle.penup()
    turtle.goto(x, y)
    other()
def draw4(x , y):
    turtle.goto(x, y)
    turtle.pendown()
def Bac():
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(90)
    turtle.setheading(180)
    turtle.pendown()
    loop = 1
    legnth = 1
    speed = 10000
    angle = 1
    while loop <= 200:
        turtle.forward(legnth)
        turtle.left(angle)
        turtle.speed(10000000)
        legnth += 1.5
        speed += 1.5
        angle += 1
        loop += 1
        turtlexcord = turtle.xcor()
        turtleycord = turtle.ycor()
        print(turtlexcord , turtleycord)
        #if turtlexcord >= 250:
        #    turtle.color("green")
        #    if turtleycord >= 250:
        #      turtle.color("red")
        #elif turtlexcord <= 250:
        #    turtle.color("blue")
        #    if turtleycord <= 250:
        #        turtle.color("black")
def star():
    turtle.penup()
    turtle.setheading(180)
    turtle.pendown()
    loop = 1
    legnth = 100
    speed = 10000
    angle = 200
    while loop <= 18:
        turtle.forward(legnth)
        turtle.left(angle)
        turtle.speed(10000000)
        legnth += 1.5
        speed += 1.5
        angle += 1
        loop += 1
        turtlexcord = turtle.xcor()
        turtleycord = turtle.ycor()
        print(turtlexcord , turtleycord)
def other():
    turtle.penup()
    turtle.setheading(180)
    turtle.pendown()
    loop = 1
    legnth = 50
    speed = 10000
    angle = 90
    while loop <= 50:
        turtle.forward(legnth)
        turtle.left(angle)
        turtle.speed(10000000)
        legnth += 1.5
        speed += 1.5
        angle += 1
        loop += 1
        turtlexcord = turtle.xcor()
        turtleycord = turtle.ycor()
        print(turtlexcord , turtleycord)
button = tk.Button(frame, text="QUIT", fg="red", command=quit)
button.pack(side=tk.BOTTOM, padx=[10,20])
button = tk.Button(frame, text="Shape 1", fg="black", command=pen1)
button.pack(side=tk.BOTTOM, padx=[10,20])
button = tk.Button(frame, text="Shape 2", fg="black", command=pen2)
button.pack(side=tk.BOTTOM, padx=[10,20])
button = tk.Button(frame, text="Shape 3", fg="black", command=pen3)
button.pack(side=tk.BOTTOM, padx=[10,20])
button = tk.Button(frame, text="Pen", fg="black", command=pen4)
button.pack(side=tk.BOTTOM, padx=[10,20])
button = tk.Button(frame, text="none", fg="black",command=pen5)
button.pack(side=tk.BOTTOM, padx=[10,20])
button = tk.Button(frame, text="Play", fg="black",command=CustomPen1)
button.pack(side=tk.BOTTOM, padx=[10,20])
button = tk.Button(frame, text="Record", fg="black",command=pen7)
button.pack(side=tk.BOTTOM, padx=[10,20])
button = tk.Button(frame, text="BG White", fg="black",command=BGWhite)
button.pack(side=tk.BOTTOM, padx=[20,20])
button = tk.Button(frame, text="BG Black", fg="black",command=BGBlack)
button.pack(side=tk.BOTTOM, padx=[20,20])
button = tk.Button(frame, text="Pen red", fg="black",command=PRed)
button.pack(side=tk.BOTTOM, padx=[20,20])
button = tk.Button(frame, text="Pen Black", fg="black",command=PBlack)
button.pack(side=tk.BOTTOM, padx=[20,20])
button = tk.Button(frame, text="Pen White", fg="black",command=PWhite)
button.pack(side=tk.BOTTOM, padx=[20,20])
button = tk.Button(frame, text="Pen Blue", fg="black",command=PBlue)
button.pack()
screen.listen()
screen.mainloop()
root.mainloop()