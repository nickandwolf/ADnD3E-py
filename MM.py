from lib.display import Display
from lib.userinput import UserInput
import json

#Monster class to hold JSON data
class Monster:
    def __init__(self, name="", climate="", frequency="", organization="", activity_cycle="", diet="",
             intelligence="", treasure="", alignment="", num_appearing="", AC="", movement="", HD="",
             num_attacks="", damage_attack="", special_attack="", special_def="", magic_res="",
             size="", morale="", xp="", page="", desc="", combat="", habitat_society="", ecology=""):
        self.name = name
        self.climate = climate
        self.frequency = frequency
        self.organization = organization
        self.activity_cycle = activity_cycle
        self.diet = diet
        self.intelligence = intelligence
        self.treasure = treasure
        self.alignment = alignment
        self.num_appearing = num_appearing
        self.AC = AC
        self.movement = movement
        self.HD = HD
        self.num_attacks = num_attacks
        self.damage_attack = damage_attack
        self.special_attack = special_attack
        self.special_def = special_def
        self.magic_res = magic_res
        self.size = size
        self.morale = morale
        self.xp = xp
        self.page = page
        self.description = desc
        self.combat = combat
        self.habitat_society = habitat_society
        self.ecology = ecology

    #Let's us sort alphabetically
    def __lt__(self,other):
        return self.name < other.name

monsterList = []

f = open("apps/MM/MM.json", 'r')
jsonData = json.load(f)
f.close()

searchString = ""

display = Display()

def MakeMonsterList():
    monsterList.clear()

    for x in jsonData:
        if searchString in x or searchString == "":
            monsterList.append(Monster(jsonData[x]["name"], jsonData[x]["climate"], jsonData[x]["frequency"], jsonData[x]["organization"], jsonData[x]["activity_cycle"], jsonData[x]["diet"],
                 jsonData[x]["intelligence"], jsonData[x]["treasure"], jsonData[x]["alignment"], jsonData[x]["num_appearing"], jsonData[x]["AC"], jsonData[x]["movement"], jsonData[x]["HD"],
                 jsonData[x]["num_attacks"], jsonData[x]["damage_attack"], jsonData[x]["special_attack"], jsonData[x]["special_def"], jsonData[x]["magic_res"],
                 jsonData[x]["size"], jsonData[x]["morale"], jsonData[x]["xp"], jsonData[x]["page"], jsonData[x]["description"], jsonData[x]["combat"], jsonData[x]["habitat_society"], jsonData[x]["ecology"]))

    monsterList.sort()

def ShowMonsterList(dx, dy):
    yDisp = 0
    for x in monsterList:
        if dy + yDisp == 16: display.text(x.name, x=dx, y=dy+yDisp, color=display.palette[8])
        else: display.text(x.name, x=dx, y=dy+yDisp, color=display.palette[7])
        yDisp += 8

def ShowMonsterInfo(dx, dy):
    monster = monsterList[pointer]

    display.text(monster.page, x=240-len(monster.page)*8-5, y=dy+2, color=display.palette[7])
    display.text(monster.name, x=1, y=dy+2, color=display.palette[7])
    display.hline(x=1, y=dy+10, length=len(monster.name)*8, color=display.palette[7])
    display.hline(x=1, y=dy+0, length=len(monster.name)*8, color=display.palette[7])
    display.text(monster.frequency, x=(len(monster.name)*8)+2, y=dy+2, color=display.palette[15])

    display.text(monster.climate, x=1, y=dy+12, color=display.palette[12])

    display.text("Org:", x=1, y=dy+21, color=display.palette[23])
    display.text(monster.organization, x=4*8, y=dy+21, color=display.palette[17])

    display.text("Acty:", x=1, y=dy+30, color=display.palette[23])
    display.text(monster.activity_cycle, x=5*8, y=dy+30, color=display.palette[17])
    display.text("Diet:", x=6*8 + len(monster.activity_cycle)*8, y=dy+30, color=display.palette[23])
    display.text(monster.diet, x=11*8 + len(monster.activity_cycle)*8, y=dy+30, color=display.palette[17])

    display.text("Int:", x=1, y=dy+39, color=display.palette[23])
    display.text(monster.intelligence, x=8*4, y=dy+39, color=display.palette[17])

    display.text("Treasure:", x=1, y=dy+48, color=display.palette[7])
    display.text(monster.treasure, x=8*9, y=dy+48, color=display.palette[6])

    display.text("Alignment:", x=1, y=dy+57, color=display.palette[23])
    display.text(monster.alignment, x=10*8, y=dy+57, color=display.palette[17])

    display.text("# Appr:", x=1, y=dy+66, color=display.palette[23])
    display.text(monster.num_appearing,  x=7*8, y=dy+66, color=display.palette[17])

    display.text("AC:", x=1, y=dy+75, color=display.palette[7])
    display.text(monster.AC, x=3*8, y=dy+75, color=display.palette[6])

    display.text("MV:", x=1, y=dy+84, color=display.palette[7])
    display.text(monster.movement, x=3*8, y=dy+84, color=display.palette[6])

    display.text("HD:", x=1, y=dy+93, color=display.palette[7])
    display.text(monster.HD, x=3*8, y=dy+93, color=display.palette[6])

    display.text("# Attk:", x=1, y=dy+102, color=display.palette[7])
    display.text(monster.num_attacks, x=7*8, y=dy+102, color=display.palette[6])

    display.text("Dmg:", x=1, y=dy+111, color=display.palette[7])
    atks = monster.damage_attack.split("/")
    for l in atks:
        display.text(l, x=4*8, y=dy+111, color=display.palette[6])
        dy+=9

    display.text("S.Atk:", x=1, y=dy+111, color=display.palette[23])
    atks = monster.special_attack.split(", ")
    for l in atks:
        display.text(l, x=6*8, y=dy+111, color=display.palette[17])
        dy+=9

    display.text("S.Def:", x=1, y=dy+111, color=display.palette[23])
    atks = monster.special_def.split("; ")
    for l in atks:
        display.text(l, x=6*8, y=dy+111, color=display.palette[17])
        dy+=9

    display.text("M.Res:", x=1, y=dy+111, color=display.palette[23])
    display.text(monster.magic_res, x=6*8, y=dy+111, color=display.palette[17])

    display.text("Size:", x=1, y=dy+120, color=display.palette[23])
    display.text(monster.size, x=5*8, y=dy+120, color=display.palette[17])

    display.text("ML:", x=1, y=dy+129, color=display.palette[23])
    display.text(monster.morale, x=3*8, y=dy+129, color=display.palette[17])

    display.text("XP:", x=1, y=dy+138, color=display.palette[7])
    display.text(monster.xp, x=8*3, y=dy+138, color=display.palette[6])

#● common
#◆ uncommon
#★ rare
#✷ very rare

input = UserInput()

alpha = ["a","b","c","d","e","f","g","h","i","j","l","k","m","n","o",
         "p","q","r","s","t","u","v","w","x","y","z","BSPC","ENT"]

upArrow = ";"
downArrow = "."
leftArrow = ","
rightArrow = "/"

enter = "ENT"
escape = "`"

dispX = 8
dispY = 0

scrollY = 0

status = 1 
pointer = 2
MakeMonsterList()
ShowMonsterList(dispX,dispY)
display.show()

while 1:
    action = False
    keyList = input.get_new_keys()
    if status == 1:
        if downArrow in keyList:
            if dispY - 8 < (len(monsterList)-1)*-8+16:
                pointer = len(monsterList)-1
                dispY = (len(monsterList)-1)*-8+16
            else:
                dispY -= 8
                pointer += 1
            action = True

        elif leftArrow in keyList:
            if dispY + 80 > 16:
                dispY = 16
                pointer = 0
            else:
                dispY += 80
                pointer -= 10
            action = True

        elif upArrow in keyList:
            if dispY + 8 > 16:
                dispY = 16
                pointer = 0
            else:
                dispY += 8
                pointer -= 1
            action = True

        elif rightArrow in keyList:
            if dispY -80 < (len(monsterList)-1)*-8+16:
                dispY = len(monsterList)-1
                pointer = len(monsterList)-1
            else:
                dispY -= 80
                pointer += 10
            action = True

        elif "`" in keyList:
            break

        elif "ENT" in keyList:
            if status == 1:
                status = 0
            else:
                status = 1

            action = True

        else:
            for x in keyList:
                if x in alpha:
                    if x == "ENT":
                        searchString = ""
                    elif x == "BSPC":
                            searchString = searchString[:-1]
                    else:
                        searchString += x
                    dispY = 0
                    MakeMonsterList()
                    action = True

    elif status == 0:
        if downArrow in keyList:
            scrollY -= 16
            action = True

        elif upArrow in keyList:
            if scrollY + 16 > 0:
                scrollY = 0
            else:
                scrollY += 16
                action = True

        elif "`" in keyList:
            break

        elif "ENT" in keyList:
            scrollY = 0
            if status == 0:
                status = 1
            else:
                status = 0

            action = True

    if action:
        display.fill(0)
        if status:
            ShowMonsterList(dispX, dispY)
            display.text(searchString, x=100, y=125, color=display.palette[10])
        else:
            ShowMonsterInfo(dispX, scrollY)
        display.show()
        action = False
