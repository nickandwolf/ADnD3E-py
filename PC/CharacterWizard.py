import tkinter as tk
from tkinter import ttk
from . import AbilityScores

class CharacterWizard:
    def __init__(self, master):
        self.master = master
        master.title("Character Wizard - AD&D 3E")

        self.abilityScores = AbilityScoreFrame(self.master)

        tk.Button(self.master, text="<<", command=self.StatePlus).grid(column=0, row=1)
        tk.Button(self.master, text=">>", command=self.StateMinus).grid(column=1, row=1)
        
        self.state = 0
        
    def StatePlus(self):
        if self.state != 99:#make this the end
            self.state += 1

        self.RefreshState()

    def StateMinus(self):
        if self.state != 0:
            self.state -= 1

        self.RefreshState()

    def RefreshState(self):
        if self.state == 0:#ABILITY
            self.abilityScores.grid()
            
        elif self.state == 1:#RACE
            pass

class AbilityScoreFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.master = master

        self.Intro()

    def Intro(self):
        introVar = tk.StringVar(self.master, "0")

        # Dictionary to create multiple buttons
        values = {"Manual Input" : "1",
                  "Roll It" : "2"
                 }
        
        tk.Label(self.master, text="How would you like to generate Ability Scores?").grid(column=0,row=0)

        tk.Radiobutton(self.master, text="Manual Input", variable=introVar, value="1", command=self.ManualInput).grid(column=0,row=1)
        
        tk.Radiobutton(self.master, text="Roll It", variable=introVar, value="2", command=self.RollIt).grid(column=0,row=2)

    def ManualInput(self):
        pass

    def RollIt(self):
        pass
        

if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterSheet(root)
    root.mainloop()