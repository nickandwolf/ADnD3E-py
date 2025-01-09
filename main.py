import tkinter as tk
from tkinter import ttk
from PC import Races
from PC import Classes
from PC import Skills
from PC import MiscMod
#from PC import PlayerCharacter

version = "0.0.1"
version_notes = """
8 January 2025
Added:
* All base races
TODO:
* Add human races

"""

'''
class CharacterSheet:
    def __init__(self, master):
        self.master = master
        master.title("My Tkinter App")

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Greet", command=self.greet)
        self.button.pack()

    def greet(self):
        name = self.entry.get()
        message = f"Hello, {name}!"
        tk.Label(self.master, text=message).pack()

class PlayerCharacter:
    def __init__(self):
        self.name
        self.player
        self.class
        self.level
        self.experience
        self.race
        self.alignment
        self.move
        self.vision
        
        self.strength
        self.dexterity
        self.constitution
        self.intelligence

        self.wisdom
        self.charisma

        self.strengthMod
        self.dexterityMod
        self.constitutionMod
        self.intelligenceMod
        self.wisdomMod
        self.charismaMod

        #dictated by race
        self.strengthMax
        self.dexterityMax
        self.constitutionMax
        self.intelligenceMax
        self.wisdomMax
        self.charismaMax
        
class Race:
    def __init__(self):
        self.name
        self.size
        self.move
        self.vision

        self.strengthAdjustment
        self.dexterityAdjustment
        self.constitutionAdjustment
        self.intelligenceAdjustment
        self.wisdomAdjustment
        self.charismaAdjustment
        
        self.strengthMax
        self.dexterityMax
        self.constitutionMax
        self.intelligenceMax
        self.wisdomMax
        self.charismaMax
        
        self.restrictedClasses
        
        #put proficiencies function in
        #also put other bonuses here

def GetProficiencyBonus(level):
    return max(math.floor((level) / 2),1)

def GetCommonBonus(level):
    return math.floor((level) / 4)

def GetAbilityScoreMod(value):
    match value:
        case 1:
             return -5
        case 2:
             return -4
        case 3:
             return -3
        case 4 | 5:
            return -2
        case 6 | 7 | 8:
            return -1
        case 9 | 10 | 11 | 12:
            return 0
        case 13 | 14 | 15:
            return 1
        case 16 | 17:
            return 2
        case 18:
            return 3
        case 19:
            return 4
        case 20:
            return 5
        case 21:
            return 6
        case 22:
            return 7
        case 23:
            return 8
        case 24:
            return 9
        case 25:
            return 10
        case _:
            -99

if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterSheet(root)
    root.mainloop()
'''