import MiscMod, Skills
from copy import deepcopy as copy

class Race:
    def __init__(self, name, size, move, vision, skillProf, miscMods=[], strAdj=0, dexAdj=0, conAdj=0, intAdj=0, wisAdj=0, chaAdj=0, strMax=18, dexMax=18, conMax=18, intMax=18, wisMax=18, chaMax=18, restrictedClasses=[], desc = ""):
        self.name = name
        self.size = size
        self.move = move
        self.vision = vision

        self.strengthAdjustment = strAdj
        self.dexterityAdjustment = dexAdj
        self.constitutionAdjustment = conAdj
        self.intelligenceAdjustment = intAdj
        self.wisdomAdjustment = wisAdj
        self.charismaAdjustment = chaAdj

        self.strengthMax = strMax
        self.dexterityMax = dexMax
        self.constitutionMax = conMax
        self.intelligenceMax = intMax
        self.wisdomMax = wisMax
        self.charismaMax = chaMax

        self.restrictedClasses = restrictedClasses

        self.skillProficiencies = skillProf
        
        self.miscMods = miscMods

        self.description = desc

RaceList = []

Dwarf = Race("Dwarf", "Medium", 45, "Darkvision 60'",
             [Skills.Skill("Language(Archontean)", "Intelligence", Skills.languageDesc, True),
              Skills.Skill("Language(Dwarven)", "Intelligence", Skills.languageDesc, True),
              Skills.Skill("Profession(Miner)", "Wisdom", Skills.professionDesc)],
             
             [MiscMod.MiscModifier("Orc Hatred", "race attack", "Orc", 1),
              MiscMod.MiscModifier("Half-Orc Hatred", "race attack","Half-Orc", 1),
              MiscMod.MiscModifier("Goblin Hatred", "race attack", "Goblin", 1),
              MiscMod.MiscModifier("Hobgoblin Hatred", "race attack", "Hobgoblin", 1),
              MiscMod.MiscModifier("Bugbear Hatred", "race attack", "Bugbear", 1),
              
              MiscMod.MiscModifier("Giantkind Defence", "race AC", "Giant", 2),
              MiscMod.MiscModifier("Troll Defence", "race AC", "Troll", 2),
              MiscMod.MiscModifier("Ogre Defence", "race AC", "Ogre", 2),
              
              MiscMod.MiscModifier("Magic Resistance", "saving throw", "Magic", 4),
              MiscMod.MiscModifier("Spell Resistance", "saving throw", "Spell", 4),
              MiscMod.MiscModifier("Poison Resistance", "saving throw", "Poison", 4),
              
              MiscMod.MiscModifier("Stonework Professional", "skill", "Profession(Miner)", 2),
              MiscMod.MiscModifier("Stonework Scrutiny", "skill", "Perception(Mason)", 2),
              MiscMod.MiscModifier("Stonework Crafter", "skill", "Craft(Mason)", 2),
              MiscMod.MiscModifier("Master Smith", "skill", "Craft(Smith)", 2)],

              MiscMod.MiscModifier("Natural Miner", "special ability", "Automatically detect depth and direction when beneath the surface"),
             conAdj = 1, chaAdj = -1, conMax = 19, chaMax = 17, restrictedClasses = ["Magic-User", "Monk"])

Elf = Race("Elf", "Medium", 60, "Twilight Vision",
           [Skills.Skill("Language(Archontean)", "Intelligence", Skills.languageDesc, True),
            Skills.Skill("Language(Irthuin Elvish)", "Intelligence", Skills.languageDesc, True)],
           
           [MiscMod.MiscModifier("Ghoul Paralysis Immunity", "saving throw", "Ghoul Paralysis", 99),
            MiscMod.MiscModifier("Magical Sleep Immunity", "saving throw", "Magic Sleep", 99),
            MiscMod.MiscModifier("Spell Sleep Immunity", "saving throw", "Spell Sleep", 99),
            MiscMod.MiscModifier("Magical Charm Immunity", "saving throw", "Magic Charm", 99),
            MiscMod.MiscModifier("Spell Charm Immunity", "saving throw", "Spell Charm", 99),
            
            MiscMod.MiscModifier("Longbow Proficiency", "weapon prof", "Longbow"),
            MiscMod.MiscModifier("Shortbow Proficiency", "weapon prof", "Shortbow"),
            MiscMod.MiscModifier("Longsword Proficiency", "weapon prof", "Longsword"),
            MiscMod.MiscModifier("Shortsword Proficiency", "weapon prof", "Shortsword"),
           
            MiscMod.MiscModifier("Longbow Mastery", "weapon attack", "Longbow", 1),
            MiscMod.MiscModifier("Shortbow Mastery", "weapon attack", "Shortbow", 1),
            MiscMod.MiscModifier("Longsword Mastery", "weapon attack", "Longsword", 1),
            MiscMod.MiscModifier("Shortsword Mastery", "weapon attack", "Shortsword", 1),
           
            MiscMod.MiscModifier("Elven Stealth", "skill", "Stealth", 2),
            MiscMod.MiscModifier("Secret Door Perception", "skill", "Perception(Secret Doors)", 2),
            MiscMod.MiscModifier("Concealed Door Perception", "skill", "Perception(Concealed Doors)", 2),
            MiscMod.MiscModifier("Passive Secret Door Perception", "skill", "Passive Perception(Secret Doors)"),
            MiscMod.MiscModifier("Passive Concealed Door Perception", "skill", "Passive Perception(Concealed Doors)")],
           dexAdj = 1, conAdj = -1, dexMax = 19, conMax = 17, restrictedClasses = ["Barbarian", "Monk"])

#fae/true high elf
HighElf = copy(Elf)
HighElf.name = "High Elf"
HighElf.intAdj = 1
HighElf.strAdj = -1
HighElf.strMax = 17
HighElf.intMax = 19
HighElf.skillProficiencies[1] = Skills.Skill("Language(High Elvish)", "Intelligence", Skills.languageDesc)

#sylvan/wood elf
WoodElf = copy(Elf)
WoodElf.name = "Wood Elf"

WoodElf.miscMods[7] = MiscMod.MiscModifier("Spear Proficiency", "weapon prof", "Spear", 1)
WoodElf.miscMods[11] = MiscMod.MiscModifier("Spear Master", "weapon attack", "Spear", 1)

Gnome = copy(Dwarf)
Gnome.name = "Gnome"
Gnome.size = "Small"
Gnome.skillProficiencies[1] = Skills.Skill("Language(Ave Vox)", "Intelligence", Skills.languageDesc, True)
Gnome.skillProficiencies.append(Skills.Skill("Language(Burrowing Mammals)", "Intelligence", "Gnomes may communicate with burrowing mammals at a rudimentary level.", True))
Gnome.miscMods = Gnome.miscMods[2:]
del Gnome.miscMods[8]
Gnome.miscMods.append(MiscMod.MiscModifier("Kobold Hatred", "race attack","Kobold", 1))
Gnome.chaAdj = 0
Gnome.chaMax = 18
Gnome.strAdj = -1
Gnome.strMax = 17
Gnome.restrictedClasses = ["Barbarian", "Monk"]

HalfElf = Race("Half-Elf", "Mediun", 60, "Twilight Vision",
       [Skills.Skill("Language(Archontean)", "Intelligence", Skills.languageDesc, True),
        Skills.Skill("Language(Irthuin Elvish)", "Intelligence", Skills.languageDesc, True)],

       [MiscMod.MiscModifier("Magical Sleep Resistance", "saving throw", "Magic Sleep", 4),
        MiscMod.MiscModifier("Spell Sleep Resistance", "saving throw", "Spell Sleep", 4),
        MiscMod.MiscModifier("Magical Charm Resistance", "saving throw", "Magic Charm", 4),
        MiscMod.MiscModifier("Spell Charm Resistance", "saving throw", "Spell Charm", 4),

       MiscMod.MiscModifier("Secret Door Perception", "skill", "Perception(Secret Doors)", 2),
       MiscMod.MiscModifier("Concealed Door Perception", "skill", "Perception(Concealed Doors)", 2),
       MiscMod.MiscModifier("Passive Secret Door Perception", "skill", "Passive Perception(Secret Doors)"),
       MiscMod.MiscModifier("Passive Concealed Door Perception", "skill", "Passive Perception(Concealed Doors)"),
       
       MiscMod.MiscModifier("Ability Check Bonus", "ability modifier", "", 1),
       MiscMod.MiscModifier("Ability Check Bonus", "ability modifier", "", 1),
       MiscMod.MiscModifier("Ability Check Bonus", "ability modifier", "", 1)])

RaceList.append(Dwarf)
RaceList.append(Elf)
RaceList.append(HighElf)
RaceList.append(WoodElf)