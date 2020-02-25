import pygame
from tkinter import *
from PIL import ImageTk,Image
import random

root = Tk()
canvas = Canvas(root, width = 500, height = 500)
canvas.pack()
root.title("Dice Roller")
root.grid()
value = 0
value2 = 0
side1 = ImageTk.PhotoImage(Image.open("1.png"))
side2 = ImageTk.PhotoImage(Image.open("2.png"))
side3 = ImageTk.PhotoImage(Image.open("3.png"))
side4 = ImageTk.PhotoImage(Image.open("4.png"))
side5 = ImageTk.PhotoImage(Image.open("5.png"))
side6 = ImageTk.PhotoImage(Image.open("6.png"))

def randnum(event):
    value1 = random.randint(1,6)
    value2 = random.randint(1, 6)
    showDice1(value1)
    showDice2(value2)
    print(value1)
    print(value2)
    updateDisplay(value1)
    updateDisplay2(value2)


def updateDisplay(myString):
	displayVariable.set(myString)

def updateDisplay2(myString):
    displayVariable1.set(myString)


def showDice1(roll):
    if roll == 1:
        canvas.create_image(20, 20, anchor=NW, image=side1)
    if roll == 2:
        canvas.create_image(20, 20, anchor=NW, image=side2)
    if roll == 3:
        canvas.create_image(20, 20, anchor=NW, image=side3)
    if roll == 4:
        canvas.create_image(20, 20, anchor=NW, image=side4)
    if roll == 5:
        canvas.create_image(20, 20, anchor=NW, image=side5)
    if roll == 6:
        canvas.create_image(20, 20, anchor=NW, image=side6)



def showDice2(roll):
    if roll == 1:
        canvas.create_image(250, 20, anchor=NW, image=side1)
    if roll == 2:
        canvas.create_image(250, 20, anchor=NW, image=side2)
    if roll == 3:
        canvas.create_image(250, 20, anchor=NW, image=side3)
    if roll == 4:
        canvas.create_image(250, 20, anchor=NW, image=side4)
    if roll == 5:
        canvas.create_image(250, 20, anchor=NW, image=side5)
    if roll == 6:
        canvas.create_image(250, 20, anchor=NW, image=side6)



button_1 = Button(root, text="Roll the Dice")
button_1.bind("<Button-1>",randnum)
button_1.pack()
displayVariable = StringVar()
displayVariable1 = StringVar()
displayLabel = Label(root, textvariable=displayVariable)
displayLabel1 = Label(root, textvariable=displayVariable1)
displayLabel.pack()
displayLabel1.pack()


root.mainloop()