import random
import tkinter
from tkinter import ttk

#Graphic Interface class
class GraphicInterface:

    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")

        self.frame = ttk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.labelTitle = ttk.Label(self.frame, text="Password Generator length:")
        self.labelTitle.grid(row=0, column=0, pady=10)

        self.passwordLength = ttk.Entry(self.frame)
        self.passwordLength.grid(row=1, column=0, pady=5)

        self.generateButton = ttk.Button(self.frame, text="Generate a password", command=self.GeneratePassword)
        self.generateButton.grid(row=2, column=0, pady=10)

        self.passwordGenerated = ttk.Label(self.frame, text="Password Generated:")
        self.passwordGenerated.grid(row=3, column=0, pady=5)

        self.finalPassword = ttk.Entry(self.frame, state="readonly")
        self.finalPassword.grid(row=4, column=0, pady=10)

        root.mainloop()

    #Function to obtein the length from the Entry
    def obtainLenght(self):
        try:
            passwordLenght = int(self.passwordLength.get())
            if passwordLenght > 0:
                return passwordLenght
            else: raise ValueError("Longitud incorrecta")
        except ValueError:
            print("Introduce un número")
            return 0

    #Function to generate the password using an array of characters
    def GeneratePassword(self):
        passwordLenght = self.obtainLenght()
        Password = ""

        validCharacters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                   "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "_"]
        for i in range (passwordLenght):
            Password = Password + validCharacters[random.randint(0, (len(validCharacters)-1))]
        self.finalPassword.config(state="normal")
        self.finalPassword.delete(0, "end")
        self.finalPassword.insert(0, Password)
        self.finalPassword.config(state="readonly")


root = tkinter.Tk()
app = GraphicInterface(root)