#Copyright Jamie Westerhout, 2020
import tkinter as tk
import turtle
import random
import sqlite3
import sys
root = tk.Tk()
root.configure(bg="darkgrey")
frame = tk.Frame(root)
canvas = tk.Canvas(master = root, width = 900, height = 900, bg="black")
canvas.pack()
sys.stdout = open("log.txt", "+a")
screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)
root.title("Drawing Program - Copyright Jamie Westerhout, 2020")
root.iconbitmap('ICO.ico')
t.shape("circle")
t.shapesize(0.1)
t.pensize(2)
screen.bgcolor("white")
frame.pack()
t.speed(100000)
#screen = t.TurtleScreen()
loop2 = 1
test = 1
t.color("red")
def pen1():
    unbind()
    screen.onscreenclick(draw1)
def pen2():
    unbind()
    screen.onscreenclick(draw2)
def pen3():
    unbind()
    screen.onscreenclick(draw3)
#def pen4():
  #  t.penup()
  #  screen.onscreenclick(draw4)
def pen4():
    screen.onscreenclick(none2)
    canvasturtle=screen.getcanvas()
    t.penup()
    canvasturtle.bind("<B1-Motion>", draw42)
    canvasturtle.bind("<Button-1>", draw42)
    canvasturtle.bind("<ButtonRelease-1>", release)
def pen5():
    unbind()
    t.penup()
    screen.onscreenclick(none)
def pen7():
    unbind()
    t.penup()
    screen.onscreenclick(Record)
def none(x, y):
    unbind()
    t.penup()
    t.goto(x, y)
def unbind():
    canvasturtle=screen.getcanvas()
    canvasturtle.unbind("<B1-Motion>")
    canvasturtle.unbind("<Button-1>")
    canvasturtle.unbind("<ButtonRelease-1>")
def none2(x, y):
    print(x, y)
def BGBlack():
    screen.bgcolor("black")
def BGWhite():
    screen.bgcolor("white")
def PRed():
    t.pencolor("Red")
def PWhite():
    t.pencolor("white")
def PBlack():
    t.pencolor("black")
def PBlue():
    t.pencolor("Blue")
def Record(x, y):
    canvasturtle=screen.getcanvas()
    canvasturtle.unbind("<B1-Motion>")
    t.goto(x, y)
    t.pendown()
    f = open('CustomPen.pen','a+')
    f.write(str(float(t.xcor())))
    f.write(", ")
    f.write(str(float(t.ycor())))
    f.write("\n")
    f.close()
    print(str(t.pos()))
def CustomPen1():
    canvasturtle=screen.getcanvas()
    canvasturtle.unbind("<B1-Motion>")
    p = open('CustomPen.pen','r')
    t.penup()
    for x in p:
        x1, y1 = map(str , x.split())
        x1 = x1[:-1]
        t.goto(float(x1), float(y1))
        t.pendown()
    p.close
def draw1(x , y):
    t.penup()
    t.goto(x, y)
    Bac()
def draw2(x , y):
    t.penup()
    t.goto(x, y)
    star()
def draw3(x , y):
    t.penup()
    t.goto(x, y)
    other()
def draw4(x , y):
    t.goto(x, y)
    t.pendown()
def draw42(event):
    canvasturtle=screen.getcanvas()
    canvasturtle.unbind("<B1-Motion>")
    t.goto(event.x-455, 454-event.y)
    print(event.x-455 , 454-event.y)
    t.pendown()
    canvasturtle.bind("<B1-Motion>", draw42)
def release(event):
    canvasturtle=screen.getcanvas()
    unbind()
    t.penup()
    canvasturtle.bind("<Button-1>", reinziate)
def reinziate(event):
    t.penup()
    t.goto(event.x-455, 454-event.y)
    pen4()
def Bac():
    t.setheading(90)
    t.penup()
    t.forward(90)
    t.setheading(180)
    t.pendown()
    loop = 1
    legnth = 1
    speed = 10000
    angle = 1
    while loop <= 200:
        t.forward(legnth)
        t.left(angle)
        t.speed(10000000)
        legnth += 1.5
        speed += 1.5
        angle += 1
        loop += 1
        txcord = t.xcor()
        tycord = t.ycor()
        print(txcord , tycord)
        #if txcord >= 250:
        #    t.color("green")
        #    if tycord >= 250:
        #      t.color("red")
        #elif txcord <= 250:
        #    t.color("blue")
        #    if tycord <= 250:
        #        t.color("black")
def star():
    t.penup()
    t.setheading(180)
    t.pendown()
    loop = 1
    legnth = 100
    speed = 10000
    angle = 200
    while loop <= 18:
        t.forward(legnth)
        t.left(angle)
        t.speed(10000000)
        legnth += 1.5
        speed += 1.5
        angle += 1
        loop += 1
        txcord = t.xcor()
        tycord = t.ycor()
        print(txcord , tycord)
def other():
    t.penup()
    t.setheading(180)
    t.pendown()
    loop = 1
    legnth = 50
    speed = 10000
    angle = 90
    while loop <= 50:
        t.forward(legnth)
        t.left(angle)
        t.speed(10000000)
        legnth += 1.5
        speed += 1.5
        angle += 1
        loop += 1
        txcord = t.xcor()
        tycord = t.ycor()
        print(txcord , tycord)
button = tk.Button(master = root, text="QUIT", fg="red", command=quit, highlightthickness=5, bd=0.5)
button.pack(side=tk.LEFT, padx=[10,20], pady=[5,5])
button = tk.Button(master = root, text="Shape 1", fg="black", command=pen1, highlightthickness=5, bd=0.5)
button.pack(side=tk.LEFT, padx=[10,20], pady=[5,5])
button = tk.Button(master = root, text="Shape 2", fg="black", command=pen2, highlightthickness=5, bd=0.5)
button.pack(side=tk.LEFT, padx=[10,20], pady=[5,5])
button = tk.Button(master = root, text="Shape 3", fg="black", command=pen3, highlightthickness=5, bd=0.5)
button.pack(side=tk.LEFT, padx=[10,20], pady=[5,5])
button = tk.Button(master = root, text="Pen", fg="black", command=pen4, highlightthickness=5, bd=0.5)
button.pack(side=tk.LEFT, padx=[10,20], pady=[5,5])
button = tk.Button(master = root, text="none", fg="black",command=pen5, highlightthickness=5, bd=0.5)
button.pack(side=tk.LEFT, padx=[10,20], pady=[5,5])
button = tk.Button(master = root, text="Play", fg="black",command=CustomPen1, highlightthickness=5, bd=0.5)
button.pack(side=tk.LEFT, padx=[10,20], pady=[5,5])
button = tk.Button(master = root, text="Record", fg="black",command=pen7, highlightthickness=5, bd=0.5)
button.pack(side=tk.RIGHT, padx=[10,20], pady=[5,5])
button = tk.Button(master = root, text="BG White", fg="black",command=BGWhite, highlightthickness=5, bd=0.5)
button.pack(side=tk.RIGHT, padx=[10,20], pady=[5,5])
button = tk.Button(master = root, text="BG Black", fg="black",command=BGBlack, highlightthickness=5, bd=0.5)
button.pack(side=tk.RIGHT, padx=[10,20], pady=[5,5])
button = tk.Button(master = root, text="Pen red", fg="black",command=PRed, highlightthickness=5, bd=0.5)
button.pack(side=tk.RIGHT, padx=[10,20], pady=[5,5])
button = tk.Button(master = root, text="Pen Black", fg="black",command=PBlack, highlightthickness=5, bd=0.5)
button.pack(side=tk.RIGHT, padx=[10,20], pady=[5,5])
button = tk.Button(master = root, text="Pen White", fg="black",command=PWhite, highlightthickness=5, bd=0.5)
button.pack(side=tk.RIGHT, padx=[10,20], pady=[0,0])
button = tk.Button(master = root, text="Pen Blue", fg="black",command=PBlue, highlightthickness=5, bd=0.5)
button.pack(side=tk.RIGHT, padx=[10,20], pady=[0,0])
button.pack()
screen.listen()
screen.mainloop()
t.mainloop()
root.mainloop()
