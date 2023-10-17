from tkinter import *
class calculator:

    def getInput(self):
        self.userInput = self.entry.get()

    def clearInput(self):
        self.entry.delete(0, END)

    def buttonPress(self, argv):
        self.entry.insert(END, argv)

    def evaluate(self):
        self.getInput()
        try:
            self.result = eval(self.userInput)
        except ZeroDivisionError:
            self.entry.delete(0, END)
            self.entry.insert(0, "Undefined")
        except SyntaxError:
            self.entry.delete(0, END)
            self.entry.insert(0, "Enter Value")
        else:
            self.entry.delete(0, END)
            self.entry.insert(0, self.result)

    def __init__(self, gui):

        gui.title("Calculator")
        gui.iconbitmap('Cal.ico')
        gui.geometry()

        self.entry = Entry(gui, fg = "gray5")
        self.entry.grid(row = 0, column = 0, columnspan = 4)

        bAC = Button(gui, text = "AC", width = 17, height = 2, bg= "crimson", fg = "white",
        command = lambda: self.clearInput())
        bAC.grid(row = 1, column = 0, columnspan = 3)

        bDiv = Button(gui, text = "÷", width = 5, height = 3, bg= "gray25", fg = "white",
        command = lambda: self.buttonPress("/"))
        bDiv.grid(row = 1, column = 3)

        b7 = Button(gui, text = "7", width = 5, height = 3, bg= "cornsilk3", fg = "gray5",
        command = lambda: self.buttonPress("7"))
        b7.grid(row = 2, column = 0)

        b8 = Button(gui, text = "8", width = 5, height = 3, bg= "cornsilk3", fg = "gray5",
        command = lambda: self.buttonPress("8"))
        b8.grid(row = 2, column = 1)

        b9 = Button(gui, text = "9", width = 5, height = 3, bg= "cornsilk3", fg = "gray5",
        command = lambda: self.buttonPress("9"))
        b9.grid(row = 2, column = 2)

        bMult = Button(gui, text = "*", width = 5, height = 3, bg= "gray25", fg = "white",
        command = lambda: self.buttonPress("*"))
        bMult.grid(row = 2, column = 3)

        b4 = Button(gui, text = "4", width = 5, height = 3, bg= "cornsilk3", fg = "gray5",
        command = lambda: self.buttonPress("4"))
        b4.grid(row = 3, column = 0)

        b5 = Button(gui, text = "5", width = 5, height = 3, bg= "cornsilk3", fg = "gray5",
        command = lambda: self.buttonPress("5"))
        b5.grid(row = 3, column = 1)

        b6 = Button(gui, text = "6", width = 5, height = 3, bg= "cornsilk3", fg = "gray5",
        command = lambda: self.buttonPress("6"))
        b6.grid(row = 3, column = 2)

        bSub = Button(gui, text = "-", width = 5, height = 3, bg= "gray25", fg = "white",
        command = lambda: self.buttonPress("-"))
        bSub.grid(row = 3, column = 3)

        b1 = Button(gui, text = "1", width = 5, height = 3, bg= "cornsilk3", fg = "gray5",
        command = lambda: self.buttonPress("1"))
        b1.grid(row = 4, column = 0)

        b2 = Button(gui, text = "2", width = 5, height = 3, bg= "cornsilk3", fg = "gray5",
        command = lambda: self.buttonPress("2"))
        b2.grid(row = 4, column = 1)

        b3 = Button(gui, text = "3", width = 5, height = 3, bg= "cornsilk3", fg = "gray5",
        command = lambda: self.buttonPress("3"))
        b3.grid(row = 4, column = 2)

        bAdd = Button(gui, text = "+", width = 5, height = 3, bg= "gray25", fg = "white",
        command = lambda: self.buttonPress("+"))
        bAdd.grid(row = 4, column = 3)

        b0 = Button(gui, text = "0", width = 12, height = 3, bg= "cornsilk3", fg = "gray5",
        command = lambda: self.buttonPress("0"))
        b0.grid(row = 5, column = 0, columnspan = 2)

        bDot = Button(gui, text = ".", width = 5, height = 3, bg= "cornsilk3", fg = "gray5",
        command = lambda: self.buttonPress("."))
        bDot.grid(row = 5, column = 2)

        bEquals = Button(gui, text = "=", width = 5, height = 3, bg= "gray25", fg = "white",
        command = lambda: self.evaluate())
        bEquals.grid(row = 5, column = 3)

root = Tk()
calculator(root)
root.mainloop()
