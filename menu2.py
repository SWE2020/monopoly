from tkinter import *
from tkinter.ttk import Combobox

class Windows():

    def __init__(self):
        pass

    def selectPlayerNumWin(self, root):
        root.title('Property Tycoon - Setup Menu')
        root.geometry("400x150+600+300")

        #'Pick # Players' label
        lbl=Label(root, text="Pick the number of players", fg='blue', font=("Helvetica", 16))
        lbl.place(x=100, y=10)

        #radio button variable
        self.playerNum = IntVar()

        #creating radio buttons
        r2=Radiobutton(root, text="2", variable=self.playerNum, value=2)
        r3=Radiobutton(root, text="3", variable=self.playerNum, value=3)
        r4=Radiobutton(root, text="4", variable=self.playerNum, value=4)
        r5=Radiobutton(root, text="5", variable=self.playerNum, value=5)
        r6=Radiobutton(root, text="6", variable=self.playerNum, value=6)
        r2.place(x=60,y=50)
        r3.place(x=120, y=50)
        r4.place(x=180, y=50)
        r5.place(x=240, y=50)
        r6.place(x=300, y=50)

        btn=Button(root, text="Next", fg='blue', command=self.definePlayerWin)
        btn.place(x=180, y=100)


    def definePlayerWin(self):
        definePlayer=Toplevel()
        TotPlayers = str(self.playerNum.get())
        numTotPlayers = self.playerNum.get()

        lbl=Label(definePlayer, text="Define Player States for " + TotPlayers + " players", fg='blue', font=("Helvetica", 22))
        lbl.place(x=100, y=10)

        status = StringVar()
        status.set("Computer")
        data=("Person", "Computer")

        #need to add token selection --> need to randomize if Computer
        #create lists to hold each players info
        for x in range(numTotPlayers):
            lbl=Label(definePlayer, text="Player " + str(x+1) + " ", fg='black', font=("Helvetica", 16))
            lbl.place(x=70, y=(40+(x*30)))
            cb=Combobox(definePlayer, values=data)
            cb.place(x=150, y=(40+(x*30)))
            print(x)

        definePlayer.title('Define Players')
        definePlayer.geometry("400x200+600+300")

root = Tk()
windows = Windows()
windows.selectPlayerNumWin(root)
root.mainloop()
