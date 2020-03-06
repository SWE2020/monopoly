import pygame
from tkinter import *
from PIL import ImageTk,Image
import random

root = Tk()
canvas = Canvas(root, width = 1000, height = 1000)
canvas.pack()
root.title("Monopoly")
root.grid()
value = 0
value2 = 0


# side1 = ImageTk.PhotoImage(Image.open("Cooper Drive.png"))
# side2 = ImageTk.PhotoImage(Image.open("Crapper Street.png"))
# side3 = ImageTk.PhotoImage(Image.open("Crusher Creek.png"))
# side4 = ImageTk.PhotoImage(Image.open("Gangsters Paradise.png"))
# side5 = ImageTk.PhotoImage(Image.open("Ghengis Crescent.png"))
# side6 = ImageTk.PhotoImage(Image.open("Han Xin Gardens.png"))

side1 = Image.open("Cooper Drive.png")
side1 = side1.resize((100,100),Image.ANTIALIAS)
side1 = ImageTk.PhotoImage(side1)

side2 = Image.open("Crapper Street.png")
side2 = side2.resize((100,100),Image.ANTIALIAS)
side2 = ImageTk.PhotoImage(side2)

side3 = Image.open("Gangsters Paradise.png")
side3 = side3.resize((100,100),Image.ANTIALIAS)
side3 = ImageTk.PhotoImage(side3)

side4 = Image.open("Crusher Creek.png")
side4 = side4.resize((100,100),Image.ANTIALIAS)
side4 = ImageTk.PhotoImage(side4)

side5 = Image.open("Ghengis Crescent.png")
side5 = side5.resize((100,100),Image.ANTIALIAS)
side5 = ImageTk.PhotoImage(side5)

side6 = Image.open("Han Xin Gardens.png")
side6 = side6.resize((100,100),Image.ANTIALIAS)
side6 = ImageTk.PhotoImage(side6)

side7 = Image.open("Han Xin Gardens.png")
side7 = side7.resize((100,100),Image.ANTIALIAS)
side7 = side7.rotate(270)
side7 = ImageTk.PhotoImage(side7)

array = []
array.append(side1)
array.append(side2)
array.append(side3)
array.append(side4)
array.append(side5)
array.append(side6)

print(array)

def createBoard():
    canvas.create_image(20, 20, anchor=NW, image=side1)
    canvas.create_image(120, 20, anchor=NW, image=side2)
    canvas.create_image(220, 20, anchor=NW, image=side3)
    canvas.create_image(320, 20, anchor=NW, image=side4)
    canvas.create_image(420, 20, anchor=NW, image=side5)
    canvas.create_image(520, 20, anchor=NW, image=side6)
    canvas.create_image(620, 120, anchor=NW, image=side7)


def randnum(event):
    createBoard()


def updateDisplay(myString):
	displayVariable.set(myString)

def updateDisplay2(myString):
    displayVariable1.set(myString)

#
# def showDice1(roll):
#     if roll == 1:
#         canvas.create_image(20, 20, anchor=NW, image=side1)
#     if roll == 2:
#         canvas.create_image(20, 20, anchor=NW, image=side2)
#     if roll == 3:
#         canvas.create_image(20, 20, anchor=NW, image=side3)
#     if roll == 4:
#         canvas.create_image(20, 20, anchor=NW, image=side4)
#     if roll == 5:
#         canvas.create_image(20, 20, anchor=NW, image=side5)
#     if roll == 6:
#         canvas.create_image(20, 20, anchor=NW, image=side6)


#
# #def showDice2(roll):
#     if roll == 1:
#         canvas.create_image(250, 20, anchor=NW, image=side1)
#     if roll == 2:
#         canvas.create_image(250, 20, anchor=NW, image=side2)
#     if roll == 3:
#         canvas.create_image(250, 20, anchor=NW, image=side3)
#     if roll == 4:
#         canvas.create_image(250, 20, anchor=NW, image=side4)
#     if roll == 5:
#         canvas.create_image(250, 20, anchor=NW, image=side5)
#     if roll == 6:
#         canvas.create_image(250, 20, anchor=NW, image=side6)



button_1 = Button(root, text="Create The Board")
button_1.bind("<Button-1>",randnum)
button_1.pack()
displayVariable = StringVar()
displayVariable1 = StringVar()
displayLabel = Label(root, textvariable=displayVariable)
displayLabel1 = Label(root, textvariable=displayVariable1)
displayLabel.pack()
displayLabel1.pack()


root.mainloop()