from . import Skills
from . import MiscMod


ExperienceLevels = {1:0, 2:2500, 3:5000, 4:10000, 5:20000,
                    6:37500, 7:75000, 8:150000, 9:250000, 10:500000,
                    11:750000, 12:1000000, 13:1250000, 14:1500000, 15:1750000,
                    16:2000000, 17:2250000, 18:2500000, 19:2750000, 20:3000000}

class Class:
    def __init__(self):
        pass

    def LevelCheck(self,xp):
        for level, xpReq in sorted(ExperienceLevels.items(), reverse=True):
            if xp >= xpReq:
                return level

class Assassin(Class):
    def __init__(self, level=1, hp=3):
        self.name = "Assassin"
        self.level = level
        self.hitDie = 4
        self.hitPoints = hp
        self.abilityReq = ["Dexterity 13", "Intelligence 13"]
        self.alignmentReq = "Non-Good"

        self.attackBonus = 0
        
        self.savingThrowProf = ["Dexterity", "Intelligence"]
        
        self.skillProf = [Skills.GetSkill("Athletics")]#, Skills.GetSkill("Disable Device"), Skills.GetSkill("Disguise"),
                          #Skills.GetSkill("Poison"), Skills.GetSkill("Stealth"),
                          #Skills.Skill("Extra Skill", "", ""), Skills.Skill("Extra Skill", "", "")]
        
        self.miscMod = [MiscMod.MiscModifier("Assassin Armor Proficiency", "armor prof", "Light Armor"),
                        MiscMod.MiscModifier("Assassin Shield Proficiency", "armor prof", "Small Shields"),
                        MiscMod.MiscModifier("Assassin Weapon Proficiency", "weapon prof", "All"),
                        MiscMod.MiscModifier("Backstab", "special attack/damage", "Flanked Foe, Blinded Foe", 2),
                        MiscMod.MiscModifier("Burglar", "skill",
                                             "Athletics(Climb), Disable Device(Traps), Disable Device(Locks), Stealth", 2),
                        MiscMod.MiscModifier("Find Traps", "skill", "Perception(Traps)"),
                        MiscMod.MiscModifier("Killing Strike", "special ability", "Surprised Foe",
                                             "Foe ► CON Saving Throw vs 10 + ½ Assassin Level (min. 1) + Assassin INT mod = HP reduced to 0 - ½ Assassin Level (round down)")]
                        
    def LevelUp(self):
        checkLevel = self.LevelCheck()
        if checkLevel == self.level:
            return
        
ass = Assassin()
#ass.LevelUp()