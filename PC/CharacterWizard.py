import tkinter as tk
from tkinter import ttk
from random import randint as r
import tkinter.messagebox
from . import AbilityScores
from . import Races

version = "0.0.1"

class CharacterWizard(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Character Creation Wizard v" + version)
        self.geometry("250x300")

        self.AbilityScores = AbilityScores.AbilityScores()

        # Create a container to hold wizard frames
        self.container = ttk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Define wizard steps
        steps = [AbilityScoreFrame, RaceFrame, Step3]

        for Step in steps:
            frame = Step(self.container, self)
            self.frames[Step] = frame
            frame.grid(row=0, column=0, sticky="nsew")

            #where do we start?! HERE!
        self.show_frame(RaceFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class AbilityScoreFrame(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        ttk.Label(self, text="  Ability Scores", font=('Helvetica', 18, 'bold')).grid(column=0,row=0,columnspan=5)

        self.totals = ["ass"]
        

        #put this at the end
        self.abNext = ttk.Button(self, text="Select Race", command=lambda: controller.show_frame(RaceFrame))
        self.abNext.grid(column=2,row=9,columnspan=3)
        self.abNext["state"] = tk.DISABLED
        
        self.Intro()

    def Intro(self):
        self.abNext["state"] = tk.DISABLED
        self.controller.geometry("200x165")
        self.introVar = tk.StringVar(self.master, "0")

        # Dictionary to create multiple buttons
        values = {"Manual Input" : "1",
                        "Roll It" : "2"
                     }
          
        self.introL = ttk.Label(self, text="  How would you like to\n  generate Ability Scores?")
        self.introL.grid(column=0,row=1,columnspan=5)

        self.introR1 = ttk.Radiobutton(self, text="Manual Input", variable=self.introVar, value="1", command=None)
        self.introR1.grid(column=0,row=2,columnspan=5)

        self.introR2 = ttk.Radiobutton(self, text="Roll It", variable=self.introVar, value="2", command=None)
        self.introR2.grid(column=0,row=3,columnspan=5)

        self.introB = ttk.Button(self, text="Next", command=self.handler)
        self.introB.grid(column=2, row=4,columnspan=3)

    def handler(self):
        if self.introVar.get() > "0":
            self.introL.destroy()
            self.introR1.destroy()
            self.introR2.destroy()
            self.introB.destroy()

            if self.introVar.get() == "1":
                self.ManualInput()

            elif self.introVar.get() == "2":
                self.RollIt()

    def manualReset(self):
        self.abNext["state"] = tk.DISABLED
        self.abmiStrL.destroy()
        self.abmiIntL.destroy()
        self.abmiWisL.destroy()
        self.abmiDexL.destroy()
        self.abmiConL.destroy()
        self.abmiChaL.destroy()
        self.abmiStrE.destroy()
        self.abmiIntE.destroy()
        self.abmiWisE.destroy()
        self.abmiDexE.destroy()
        self.abmiConE.destroy()
        self.abmiChaE.destroy()
        self.abmiStrModL.destroy()
        self.abmiIntModL.destroy()
        self.abmiWisModL.destroy()
        self.abmiDexModL.destroy()
        self.abmiConModL.destroy()
        self.abmiChaModL.destroy()
        self.abmiB1.destroy()
        self.abmiB2.destroy()

        self.Intro()

    def RollItValidate(self):
        playerTotals = []
        playerTotals.append(int(self.abmiStrV.get()))
        playerTotals.append(int(self.abmiIntV.get()))
        playerTotals.append(int(self.abmiWisV.get()))
        playerTotals.append(int(self.abmiDexV.get()))
        playerTotals.append(int(self.abmiConV.get()))
        playerTotals.append(int(self.abmiChaV.get()))

        playerTotals.sort()
        self.totals.sort()

        if playerTotals == self.totals or "ass" in self.totals:
            self.SetMod("str")
            self.SetMod("int")
            self.SetMod("wis")
            self.SetMod("dex")
            self.SetMod("con")
            self.SetMod("cha")

            self.controller.AbilityScore = AbilityScores.AbilityScores(playerTotals)

            self.abNext["state"] = tk.ACTIVE

        else:
            tkinter.messagebox.showerror("Warning!", "Your stats don't match the dice!")
            self.abNext["state"] = tk.DISABLED
            

    def DisableButton(self,n):
        self.abNext["state"] = tk.DISABLED

    def ManualInput(self):
        self.abNext["state"] = tk.DISABLED
        self.totals = ["ass"]
        self.controller.geometry("200x215")

        self.abmiStrL = ttk.Label(self, text="[Strength]", font=('Helvetica', 10, 'bold'))
        self.abmiStrL.grid(column=0,row=1,sticky="E")
        self.abmiStrV = tk.StringVar(self)

        self.abmiIntL = ttk.Label(self, text="[Intelligence]", font=('Helvetica', 10, 'bold'))
        self.abmiIntL.grid(column=0,row=2,sticky="E")
        self.abmiIntV = tk.StringVar(self)

        self.abmiWisL = ttk.Label(self, text="[Wisdom]", font=('Helvetica', 10, 'bold'))
        self.abmiWisL.grid(column=0,row=3,sticky="E")
        self.abmiWisV = tk.StringVar(self)

        self.abmiDexL = ttk.Label(self, text="[Dexterity]", font=('Helvetica', 10, 'bold'))
        self.abmiDexL.grid(column=0,row=4,sticky="E")
        self.abmiDexV = tk.StringVar(self)

        self.abmiConL = ttk.Label(self, text="[Constitution]", font=('Helvetica', 10, 'bold'))
        self.abmiConL.grid(column=0,row=5,sticky="E")
        self.abmiConV = tk.StringVar(self)

        self.abmiChaL = ttk.Label(self, text="[Charisma]", font=('Helvetica', 10, 'bold'))
        self.abmiChaL.grid(column=0,row=6,sticky="E")
        self.abmiChaV = tk.StringVar(self)

        self.abmiStrE = ttk.Spinbox(self, from_=1, to=25, textvariable=self.abmiStrV, command=lambda: self.SetMod("str"), width=3)
        self.abmiStrE.grid(column=1, row=1,sticky="W")

        self.abmiIntE = ttk.Spinbox(self, from_=1, to=25, textvariable=self.abmiIntV, command=lambda: self.SetMod("int"), width=3)
        self.abmiIntE.grid(column=1, row=2,sticky="W")

        self.abmiWisE = ttk.Spinbox(self, from_=1, to=25, textvariable=self.abmiWisV, command=lambda: self.SetMod("wis"), width=3)
        self.abmiWisE.grid(column=1, row=3,sticky="W")

        self.abmiDexE = ttk.Spinbox(self, from_=1, to=25, textvariable=self.abmiDexV, command=lambda: self.SetMod("dex"), width=3)
        self.abmiDexE.grid(column=1, row=4,sticky="W")

        self.abmiConE = ttk.Spinbox(self, from_=1, to=25, textvariable=self.abmiConV, command=lambda: self.SetMod("con"), width=3)
        self.abmiConE.grid(column=1, row=5,sticky="W")

        self.abmiChaE = ttk.Spinbox(self, from_=1, to=25, textvariable=self.abmiChaV, command=lambda: self.SetMod("cha"), width=3)
        self.abmiChaE.grid(column=1, row=6,sticky="W")

        self.abmiStrModL = ttk.Label(self, text="", font=('Helvetica', 10))
        self.abmiStrModL.grid(column=2, row=1)

        self.abmiIntModL = ttk.Label(self, text="", font=('Helvetica', 10))
        self.abmiIntModL.grid(column=2, row=2)

        self.abmiWisModL = ttk.Label(self, text="", font=('Helvetica', 10))
        self.abmiWisModL.grid(column=2, row=3)

        self.abmiDexModL = ttk.Label(self, text="", font=('Helvetica', 10))
        self.abmiDexModL.grid(column=2, row=4)

        self.abmiConModL = ttk.Label(self, text="", font=('Helvetica', 10))
        self.abmiConModL.grid(column=2, row=5)

        self.abmiChaModL = ttk.Label(self, text="", font=('Helvetica', 10))
        self.abmiChaModL.grid(column=2, row=6)

        self.abmiB1 = ttk.Button(self, text="Back", command=self.manualReset)
        self.abmiB1.grid(column=0, row=7,columnspan=2)

        self.abmiB2 = ttk.Button(self, text="Next", command=self.RollItValidate)
        self.abmiB2.grid(column=2, row=7,columnspan=2)

    def SetMod(self,score):
        val = ""
        newVal = ""

        if score == "str":
            val = self.abmiStrV.get()
        elif score == "int":
            val = self.abmiIntV.get()
        elif score == "wis":
            val = self.abmiWisV.get()
        elif score == "dex":
            val = self.abmiDexV.get()
        elif score == "con":
            val = self.abmiConV.get()
        elif score == "cha":
            val = self.abmiChaV.get()

        match val:
            case "1":
                newVal = "-5"
            case "2":
                newVal = "-4"
            case "3":
                newVal = "-3"
            case "4" | "5":
                newVal = "-2"
            case "6" | "7" | "8":
                newVal = "-1"
            case "9" | "10" | "11" | "12":
                newVal = "+0"
            case "13" | "14" | "15":
                newVal = "+1"
            case "16" | "17":
                newVal = "+2"
            case "18":
                newVal = "+3"
            case "19":
                newVal = "+4"
            case "20":
                newVal = "+5"
            case "21":
                newVal = "+6"
            case "22":
                newVal = "+7"
            case "23":
                newVal = "+8"
            case "24":
                newVal = "+9"
            case "25":
                newVal = "+10"
            case _:
                pass
            
        if score == "str":
            self.abmiStrModL["text"] = newVal
        elif score == "int":
            val = self.abmiIntModL["text"] = newVal
        elif score == "wis":
            val = self.abmiWisModL["text"] = newVal
        elif score == "dex":
            val = self.abmiDexModL["text"] = newVal
        elif score == "con":
            val = self.abmiConModL["text"] = newVal
        elif score == "cha":
            val = self.abmiChaModL["text"] = newVal

    def rollItReset(self):
        self.abNext["state"] = tk.DISABLED
        self.abmiStrL.destroy()
        self.abmiIntL.destroy()
        self.abmiWisL.destroy()
        self.abmiDexL.destroy()
        self.abmiConL.destroy()
        self.abmiChaL.destroy()
        self.abmiStrModL.destroy()
        self.abmiIntModL.destroy()
        self.abmiWisModL.destroy()
        self.abmiDexModL.destroy()
        self.abmiConModL.destroy()
        self.abmiChaModL.destroy()
        self.abmiB1.destroy()
        self.abmiB2.destroy()
        self.abmiStrLB.destroy()
        self.abmiIntLB.destroy()
        self.abmiWisLB.destroy()
        self.abmiDexLB.destroy()
        self.abmiConLB.destroy()
        self.abmiChaLB.destroy()

        self.Intro()

    def RollIt(self):
        self.abNext["state"] = tk.DISABLED
        self.controller.geometry("230x275")
        self.totals = []

        while len(self.totals) < 6:
            roll1 = r(1,6)+r(1,6)+r(1,6)
            roll2 = r(1,6)+r(1,6)+r(1,6)

            if roll1 > roll2:
                self.totals.append(roll1)
            else:
                self.totals.append(roll2)

        self.abmiStrModL = ttk.Label(self, text="--", font=('Helvetica', 10))
        self.abmiStrModL.grid(column=2, row=1)

        self.abmiIntModL = ttk.Label(self, text="--", font=('Helvetica', 10))
        self.abmiIntModL.grid(column=2, row=2)

        self.abmiWisModL = ttk.Label(self, text="--", font=('Helvetica', 10))
        self.abmiWisModL.grid(column=2, row=3)

        self.abmiDexModL = ttk.Label(self, text="--", font=('Helvetica', 10))
        self.abmiDexModL.grid(column=2, row=4)

        self.abmiConModL = ttk.Label(self, text="--", font=('Helvetica', 10))
        self.abmiConModL.grid(column=2, row=5)

        self.abmiChaModL = ttk.Label(self, text="--", font=('Helvetica', 10))
        self.abmiChaModL.grid(column=2, row=6)

        self.abmiStrL = ttk.Label(self, text="[Strength]", font=('Helvetica', 10, 'bold'))
        self.abmiStrL.grid(column=0,row=1,sticky="E")
        self.abmiStrV = tk.StringVar(self,0)

        self.abmiIntL = ttk.Label(self, text="[Intelligence]", font=('Helvetica', 10, 'bold'))
        self.abmiIntL.grid(column=0,row=2,sticky="E")
        self.abmiIntV = tk.StringVar(self,0)

        self.abmiWisL = ttk.Label(self, text="[Wisdom]", font=('Helvetica', 10, 'bold'))
        self.abmiWisL.grid(column=0,row=3,sticky="E")
        self.abmiWisV = tk.StringVar(self,0)

        self.abmiDexL = ttk.Label(self, text="[Dexterity]", font=('Helvetica', 10, 'bold'))
        self.abmiDexL.grid(column=0,row=4,sticky="E")
        self.abmiDexV = tk.StringVar(self,0)

        self.abmiConL = ttk.Label(self, text="[Constitution]", font=('Helvetica', 10, 'bold'))
        self.abmiConL.grid(column=0,row=5,sticky="E")
        self.abmiConV = tk.StringVar(self,0)

        self.abmiChaL = ttk.Label(self, text="[Charisma]", font=('Helvetica', 10, 'bold'))
        self.abmiChaL.grid(column=0,row=6,sticky="E")
        self.abmiChaV = tk.StringVar(self,0)

        self.abmiStrLB = tk.OptionMenu(self, self.abmiStrV, *self.totals)
        self.abmiStrLB.config(width=2)
        self.abmiStrLB.grid(column=1,row=1)

        self.abmiIntLB = tk.OptionMenu(self, self.abmiIntV, *self.totals)
        self.abmiIntLB.config(width=2)
        self.abmiIntLB.grid(column=1,row=2)

        self.abmiWisLB = tk.OptionMenu(self, self.abmiWisV, *self.totals)
        self.abmiWisLB.config(width=2)
        self.abmiWisLB.grid(column=1,row=3)

        self.abmiDexLB = tk.OptionMenu(self, self.abmiDexV, *self.totals)
        self.abmiDexLB.config(width=2)
        self.abmiDexLB.grid(column=1,row=4)

        self.abmiConLB = tk.OptionMenu(self, self.abmiConV, *self.totals)
        self.abmiConLB.config(width=2)
        self.abmiConLB.grid(column=1,row=5)

        self.abmiChaLB = tk.OptionMenu(self, self.abmiChaV, *self.totals, command=self.DisableButton)
        self.abmiChaLB.config(width=2)
        self.abmiChaLB.grid(column=1,row=6)

        self.abmiB1 = ttk.Button(self, text="Back", command=self.rollItReset)
        self.abmiB1.grid(column=0, row=7,columnspan=2)

        self.abmiB2 = ttk.Button(self, text="Next", command=self.RollItValidate)
        self.abmiB2.grid(column=2, row=7,columnspan=2)

class RaceFrame(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        ttk.Label(self, text="          Race", font=('Helvetica', 18, 'bold')).grid(column=0,row=0,columnspan=5)
        self.PrevB = ttk.Button(self, text="Ability Scores", command=lambda: controller.show_frame(AbilityScoreFrame))
        self.PrevB.grid(column=0,row=4,columnspan=3)

        self.NextB = ttk.Button(self, text="Select Class", command=lambda: controller.show_frame(Step3))
        self.NextB.grid(column=3,row=4,columnspan=3)
        self.NextB["state"] = tk.DISABLED
        
        Races.InitRaces()
        self.raceList = []
        for x in Races.RaceList:
            self.raceList.append(x.name)

        self.raceVar = tk.Variable(self.raceList)

        self.raceLB = tk.Listbox(self, listvariable=self.raceVar, selectmode=tk.SINGLE)
        self.raceLB.grid(column=0,row=1,columnspan=5)



class Step3(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Step 3")
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back", command=lambda: controller.show_frame(RaceFrame))


if __name__ == "__main__":
    #root = tk.Tk()
    #app = CharacterWizard(root)
    #root.mainloop()
    app = CharacterWizard()
    app.mainloop()