from copy import deepcopy as copy
from . import Skills
from . import MiscMod

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

        self.skillProf = skillProf
        
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

Dwarf.description = "Dwarves appear cold, distant, and avaricious to humans. By nature, they are clannish, wary of outsiders, and extremely vengeful, to the extent that they frequently seem xenophobic. Sarcastic jokes about ‘the generosity of dwarves’ are common in Archontos. Dwarves are reputed to be masters of stonecarving, metalworking and enchantment; still, as a rule they refuse to offer their goods for sale, so few are able to evaluate these claims. In keeping with their flinty, avaricious natures, dwarves are often teetotalers, as they fear that the effects of alcohol may render them open to being tricked or cheated. They prefer dour black clothes, sometimes embroidered with silver or gold thread. Some warrior clans favor beards, but most dwarven craftsmen do not.\n\nDwarven society is two-tiered. The upper tier is composed of the established clans, most named after a type of rock or similar substance (e.g. Malachite); members of these clans are the elites, and enjoy special privileges within dwarven holds. It is said that members of a clan will go to any end to rescue a clansman, or at least to recover his/her body and life-stone. The lower tier of dwarven society is composed of the clan-less. Some of the clanless were born that way, others were exiled from their clans for misdeeds, while still others are survivors of clans that imploded or were eliminated in factional politics. The clanless do much of the mining and shaping, usually under the supervision of a dwarf from an established clan. When dwarves die, they are said to ‘take to the stone’; whether this isliteral or figurative is an open question among human sages, for the dwarves are particularly tight-lipped about such intensely intimate practices.\n\nArchontean scholars have noted that there appears to be three types of dwarven societies: Mountain, Hill, and City. The mountain society are those closest to the dwarven homelands and dedicated to mining. The hill society are those who created forts or tradeposts to trade dwarven goods with the other races or provide their crafting expertise. Finally, the city society are those dwarves who live amongst humans and other demi-humans. These City Dwarves are typically clanless and shunned by their mountain kin. Dwarves who mix blood with humans give birth to a dwarf as normal but a moniker of 'Mul'. The muls are dwarven in every sense except for their heritage and even clanned muls is disowned and excommunicated. Therefore many muls keep their parentage to themselves and masquerade as clanless."

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

Elf.description = "Elves are rare in the human-dominated areas of Magae. The largest and best-known elven enclave is the realm of Lady Ellagel and Lord Gallador, located deep within the central forests of Irthuin. Those elves that travel in human society frequently do so for highly specific, temporary reasons (searching for a specific object or piece of knowledge); on occasion, they reside as advisors in the courts of human lords. Most humans have never seen an elf, and will treat elves with fear and caution.\n\nElven society is broadly collective, with younger elves associating themselves with seniors who have established reputations for great deeds, excellent craftsmanship, or particular wisdom. Elves prize core balance in all things. Those elves who are able to blend their emotions, magical sensibilities, knowledge, and connections with nature are held as paragons. Elves are curious and inquisitive, but do not care to reveal themselves before strangers (and especially non-elves). Most elves pursue a highly specific intellectual interest, as well as a specific interest in magic of some sort, whether as a practitioner, theorist, or amateur. Elves are particularly attracted by wisdom, by knowledge, by beauty, and by magical lore.\n\nElves have two names, one given name and one that describes one of their parents. Given names vary widely. The second name invariably is composed of a parent’s name with the suffix -son or -dottir. Which parental name an elf adopts as his/her second name is a personal choice, one marked by much symbolism (as the elf is thereby linking his/her future to that of the selected parent)."

#fae/true high elf
HighElf = copy(Elf)
HighElf.name = "High Elf"
HighElf.intAdj = 1
HighElf.strAdj = -1
HighElf.strMax = 17
HighElf.intMax = 19
HighElf.skillProf[1] = Skills.Skill("Language(High Elvish)", "Intelligence", Skills.languageDesc)
HighElf.description += "\n\nHigh Elves are the rarest and most powerful of their kind. They maintain their strong ties with the Fae with isolationist practices and are extremely rare outside of the Dolmenwood or their hidden elven enclaves."

#sylvan/wood elf
WoodElf = copy(Elf)
WoodElf.name = "Wood Elf"
WoodElf.miscMods[7] = MiscMod.MiscModifier("Spear Proficiency", "weapon prof", "Spear", 1)
WoodElf.miscMods[11] = MiscMod.MiscModifier("Spear Master", "weapon attack", "Spear", 1)
WoodElf.description += "\n\nWood Elves are those elves who abandoned the Fae in favor for the Sylvan. They embrace nature and eschew major cities, and are often confused with druids or rangers due to their reverence for nature."

Gnome = copy(Dwarf)
Gnome.name = "Gnome"
Gnome.size = "Small"
Gnome.skillProf[1] = Skills.Skill("Language(Ave Vox)", "Intelligence", Skills.languageDesc, True)
Gnome.skillProf.append(Skills.Skill("Language(Burrowing Mammals)", "Intelligence", "Gnomes may communicate with burrowing mammals at a rudimentary level.", True))
Gnome.miscMods = Gnome.miscMods[2:]
del Gnome.miscMods[8]
Gnome.miscMods.append(MiscMod.MiscModifier("Kobold Hatred", "race attack","Kobold", 1))
Gnome.chaAdj = 0
Gnome.chaMax = 18
Gnome.strAdj = -1
Gnome.strMax = 17
Gnome.restrictedClasses = ["Barbarian", "Monk"]
Gnome.description = "Unknown to a majority of the Archontean Empire, Gnomes are native to Ostralios and sometimes mistaken for dwarves by those who do not know better. Gnomes have lively and sly senses of humor, especially for practical jokes. They have a great love of living things and finely wrought items, particularly gems and jewelry. Gnomes love all sorts of precious stones and are masters of gem polishing and cutting.\n\nGnomes prefer to live in areas of rolling, rocky hills, well wooded and uninhabited by humans. Their typical isolation has made them suspicious of the other race, although they are not hostile and always hope for jolly cooperation. They are sly and furtive with those they do not know or trust, and somewhat reserved even under the best of circumstances. Gnomes tend to live in burrows or homes built into the side of natural features."

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
       
       MiscMod.MiscModifier("Ability Check Bonus", "check modifier", "", 1),
       MiscMod.MiscModifier("Ability Check Bonus", "check modifier", "", 1),
       MiscMod.MiscModifier("Ability Check Bonus", "check modifier", "", 1)])
HalfElf.description = "Half-elves are usually much like their elven parent in appearance. They are handsome folk, with the good features of each of their races. They mingle freely with either race, being only slightly taller than the average elf (5½’ on average) and weighing about 150 pounds. They typically live about 250 years. They do not have all the abilities of the elf and do not have the natural aptitude of humankind.\n\nIn general, a half-elf has the curiosity, inventiveness, and ambition of his human ancestors, and the refined senses, love of nature and artistic tastes of his elven ancestors. Half-elves do not form communities among themselves; rather, they can be found living in both elven and human communities. The reactions of humans and elves to half-elves range from intrigued fascination to outright bigotry."


Halfling = Race("Hairfoot Halfling", "Small", 45, "Twilight Vision",
                [Skills.Skill("Language(Archontean)", "Intelligence", Skills.languageDesc, True),
                 Skills.Skill("Language(Halfling Pidgin)", "Intelligence", Skills.languageDesc, True)],
                
                [MiscMod.MiscModifier("Sling Proficiency", "weapon prof", "Sling"),
                 MiscMod.MiscModifier("Dart Proficiency", "weapon prof", "Dart"),
                 MiscMod.MiscModifier("Throw Mastery", "weapon attack", "Throw", 1),
                 MiscMod.MiscModifier("Sling Mastery", "weapon attack", "Sling", 1),

                 MiscMod.MiscModifier("Magic Resistance", "saving throw", "Magic", 4),
                 MiscMod.MiscModifier("Spell Resistance", "saving throw", "Spell", 4),
                 MiscMod.MiscModifier("Poison Resistance", "saving throw", "Poison", 4),

                 MiscMod.MiscModifier("Halfling Stealth", "skill", "Stealth", 2),
                 MiscMod.MiscModifier("Halfling Perception", "skill", "Perception", 2)],

                strAdj = -1, dexAdj = 1, strMax = 17, dexMax = 19, restrictedClasses = ["Barbarian", "Magic-User", "Monk"])
Halfling.description = "Halflings are uncommon, and largely found in segregated agricultural communities. Most halflings known to the Empire live on the Grain Islands to the east of Archontea, where their agricultural prowess provides important food supplies to Archontos itself. These halfling communities are largely self-regulating, although they are under the loose supervision of the imperial strategos and his legion. Local halfling lore does not fully account for their existence on the Grain Islands, being content to distantly recall the Great Voyage on the Big Ships.\n\nAlthough most halflings are content with their rural lives, a few bold sorts attach themselves to the staff of the Strategos and end up traveling ‘across the water’ to Archontos. These halflings are seen as exotic and rustic, and they tend to suffer some general paternalistic patronizing from Imperial citizens.\n\nHalflings are sturdy and industrious, generally quiet and peaceful. Overall, they prefer the comforts of home to dangerous adventuring. They enjoy good living, rough humor, and homespun stories. In fact, they can be a trifle boring at times. Halflings are not forward, but they are observant and conversational if in friendly company.\n\nHalflings see wealth only as a means of gaining creature comforts, which they love. Though they are not overly brave or ambitious, they are generally honest and hard-working when there is need."


StoutHalfling = copy(Halfling)
StoutHalfling.name = "Stout Halfling"
StoutHalfling.vision = "Darkvision 60'"
StoutHalfling.description += "This kind of halfling is a bit smaller and stockier than the typical (hairfoot) halfling. It is commonly believed that stout halflings have traces of dwarven blood within their veins.  When forced into battle, they tend to wear more armor than their hairfoot brethren and employ morningstars in addition to the usual halflingish arms."

TallfellowHalfling = copy(Halfling)
TallfellowHalfling.name = "Tallfellow Halfling"
TallfellowHalfling.description += "A taller, slimmer halfling, with fairer skin and hair. Tallfellows are very rare. Like stouts they tend to use heavier armor than hairfoots. Tallfellows are able to ride ponies and tend to use spears in addition to the to the usual halflingish arms.  Tallfellows share the racial abilities of hairfoots, though they often speak Elven, in addition to Common and Halfling, and are friendly with elvenkind.  It is rumored that tallfellows have a bit of elven blood in them."

HalfOrc = Race("Half-Orc (Borean)", "Medium", 60, "Darkvision 60'",
               [Skills.Skill("Language(Archontean)", "Intelligence", Skills.languageDesc, True),
                Skills.Skill("Language(Orcish)", "Intelligence", Skills.languageDesc, True)],

               [MiscMod.MiscModifier("Ability Check Bonus", "check modifier", "", 1),
                MiscMod.MiscModifier("Ability Check Bonus", "check modifier", "", 1),
                MiscMod.MiscModifier("Ability Check Bonus", "check modifier", "", 1)],
              
              strAdj = 1, conAdj = 1, chaAdj = -2, strMax = 19, conMax = 19, chaMax = 16)
HalfOrc.description = "Half-orcs are boors. They are rude, crude, crass, and generally obnoxious. Because most are cowardly they tend to be bullies and cruel to the weak, but they will quickly knuckle under to the stronger. This does not mean that all half-orcs are horrid, only most of them.  It neither means that they are necessarily stupid nor incapable.  They will always seek to gain the upper hand and dominate those around them so as to be able to exercise their natural tendencies; half-orcs are greedy too. They can, of course, favor their human parent more than their orcish one.\n\nOrcs are fecund and create many crossbreeds, most of the offspring of such being typically orcish. However, some one-tenth of orc-human mongrels are sufficiently non-orcish to pass for human. It is assumed that player characters that are of the half-orc race are within the superior 10%, though there is something disquieting about their appearance that reveals the cruel nature of their orcish heritage.\n\nHalf-orcs tend to be slightly taller than humans, longer of limb and with broader shoulders. Their facial features have an orcish caste to them, with thin-slit eyes and nostrils, broad, jutting jaw lines and slightly pointed ears being common. Their canine teeth are somewhat larger than those of humans and their coloration tends to be ruddier than usual for men of their lands."

Human = Race("Human", "Medium", 60, "",
            [Skills.Skill("Language(Archontean)", "Intelligence", Skills.languageDesc, True),
             Skills.Skill("Extra Skill", "", ""),
             Skills.Skill("Extra Skill", "", "")],

            [MiscMod.MiscModifier("Strength Check Bonus", "check modifier", "Strength", 1),
             MiscMod.MiscModifier("Dexterity Check Bonus", "check modifier", "Dexterity", 1),
             MiscMod.MiscModifier("Constitution Check Bonus", "check modifier", "Constitution", 1),
             MiscMod.MiscModifier("Intelligence Check Bonus", "check modifier", "Intelligence", 1),
             MiscMod.MiscModifier("Wisdom Check Bonus", "check modifier", "Wisdom", 1),
             MiscMod.MiscModifier("Charisma Check Bonus", "check modifier", "Charisma", 1)])
Human.description = "Humans are the most diverse of all the races, with skin and hair varying in color from black to the lightest shades.  Their men may or may not wear beards and their eyes can be of various hues, tending towards shades of blue or brown."
ArchonteanHuman = copy(Human)
ArchonteanHuman.name = "Human (Archontean)"

KhumusHuman = copy(Human)
KhumusHuman.name = "Human (Khumus)"

ThorcingaHuman = copy(Human)
ThorcingaHuman.name = "Human (Thorcinga)"

WiskingaHuman = copy(Human)
WiskingaHuman.name = "Human (Wiskinga)"

OstraliosHuman = copy(Human)
OstraliosHuman.name = "Human (Ostralios)"

RaceList.append(Dwarf)
RaceList.append(Elf)
RaceList.append(HighElf)
RaceList.append(WoodElf)
RaceList.append(Gnome)
RaceList.append(HalfElf)
RaceList.append(Halfling)
RaceList.append(StoutHalfling)
RaceList.append(TallfellowHalfling)
RaceList.append(HalfOrc)
RaceList.append(ArchonteanHuman)
RaceList.append(KhumusHuman)
RaceList.append(ThorcingaHuman)
RaceList.append(WiskingaHuman)
RaceList.append(OstraliosHuman)