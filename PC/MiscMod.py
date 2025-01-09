#a class to support misc bonuses and process them

class MiscModifier:
    def __init__(self, name, type, trigger, modifier=0, desc=""):
        self.name = name
        self.type = type
        self.trigger = trigger
        self.modifier = modifier
        self.description = desc

'''
#ability modifier is only to skill checks and saving throws
modTypes = 
        ["weapon attack", "weapon damage", "race attack", "race damage",
        "race AC", "saving throw", "skill", "weapon prof", "armor prof",
        "special ability", "check modifier", "special attack",
        "special damage", "special attack/damage"]
'''

class Language:
    def __init__(self, name, alphabet, description=[]):
        self.name = name
        self.alphabet = alphabet
        self.description = description

class Alphabet:
    def __init__(self, name, description=[]):
        self.name = name
        self.description = description

MithricAlpha = Alphabet("Mithric", "Mithric was the original writing system of the Archontean Empire. In expressing the spoken form of Mithric, the early Archonteans employed a set of angular letters (30) alongside a relatively small corpus of symbols (50); the symbols were mostly those used for public expressions of power and might. In the past 1,000 years, spoken Mithric has largely died, having been replaced by its linguistic daughter, Archontean. While Archontean uses the same Mithric alphabet, four letters and all the symbols have largely fallen away; this means that modern written Archontean uses only twenty-six letters of the old Mithric alphabet. As citizens of the empire, both the halflings of the Grain Islands and the imperial goblins speak Archontean like their masters and use the exact same version of Mithric for writing. The Thorcinga adopted the Mithric alphabet to their own distinct spoken language; in so doing, they retained two of the now-lost original Mithric letters and have added three others (for a total of 31 letters). Finally, the beastmen of Arden Vul have unsurprisingly retained Mithric as their writing system; their version of the Mithric alphabet is simpler, as it uses only 22 letters.")

DwarvishRunic = Alphabet("Dwarvish Runic", "As a runic system comprising some 350+ images, Dwarven Runic expresses concepts, nouns, and adjectives symbolically. Differences in time, number, and gender can be indicated by adding small flourishes to the base rune. Dwarven Runic is famous for devoting 63 characters to various descriptions of the shape, smell, taste, hardness, and color of rock.")

WiskinRunic = Alphabet("Wiskin Runic", "Wiskin Runic is a simple runic system modeled on Dwarven Runic. It is able to convey numbers from 1-10 and in groups of 10, 50, and 100. It also includes a set of 200 or so angular runes used to describe concepts, temperatures, time, and nouns.")

SylvanRunic = Alphabet("Sylvan Runic", "In the distant past the elves contented themselves with a set of 275 runes that were used primarily for aesthetic and simple descriptive purposes (e.g., in smithing). Their system was adopted and modified by the intelligent Fey. While the elves eventually adopted a true alphabet (see Sylvan, below), they still employ Sylvan Runic for artistic, decorative, and symbolic purposes.")

SylvanAlpha = Alphabet("Sylvan Alphabet", "In response to the growth of human culture and writing, the elven lords commissioned a true alphabet to complement Sylvan Runic. This system, begun 4,500 years ago, was intended to represent spoken Elvish in both aesthetic and functional ways. Sylvan appears as a cursive, semi-continuous script of 31 letters, in which new thoughts are represented by elaborate geometric patterns which themselves carry hints of meaning (that is, each symbol, including symbols denoting pauses, connotes a different intention, emotion, or expectation).")

KhumicAlpha = Alphabet("Khumic Characters", "Khumic developed without any influence from Mithric. It contains 19 letters and 200+ symbols, all of which are typically joined together in an elegant, cursive hand.")

DraconicAlpha = Alphabet("Draconic Alphabet", "Draconic is one of the oldest languages native to Magae. Spoken draconic sounds like long wheezes of sound, varying in intensity of expelled breath, in timbre, in volume, and very occasionally in the presence of glottal interjections. Written draconic is a continuous and elaborate cursive script, without distinct words or punctuation; it is thus very difficult to get a sense for the meaning of a text without reading the entire thing, as context and shades of meaning can be modified by the expressions found later in a manuscript.")

VoxScript = Alphabet("Vox Script", "A Mithric adjacent language akin to how Greek is to Latin.")

NeoMithricAlpha = Alphabet("Neo Mithric", "Appears as Mithric except it has six more characters and is missing a few others.")

#LanguageList = []
Mithric = Language("Mithric", MithricAlpha, "Mithric is a dead language. It is still employed as the language of arcane theory and practice.")

Archontean = Language("Archontean", MithricAlpha, "The common language of wherever the Archontean Empire has or had influence.")

Thorcin = Language("Thorcin", MithricAlpha, "The native tongue of the Thorcinga, the nataives who live on Irthuin.")

Wiskin = Language("Wiskin", WiskinRunic, "The native language of the Wiskinga, the natives who reside on Borealios.")
                  
Khumus = Language("Khumus", KhumicAlpha, "The native language of the Khumus, the horse riding natives of the Khumus Khorates.")

Woldish = Language("Woldish", NeoMithricAlpha, "The common language of those who reside in the Dolmenwood.")
                  
OldWoldish = Language("Old Woldish", MithricAlpha, "A dead language of the humans who came to Dolmenwood. A mixture of Mithric and Thorcin.")
                  
Liturgic = Language("Liturgic", MithricAlpha, "The Pluritine Church's language. An archaic version of Archontean.")

AveVox = Language("Ave Vox", VoxScript, "The native language of those who reside in Ostalios.")

HighElvish = Language("High Elvish", SylvanAlpha, "The language used by the immortal fey Elves in Dolmenwood.")
                  
Sylvan = Language("Sylvan", SylvanRunic, "The language of the Fey and Immortals of Dolmenwood.")
                  
IrthuinElvish = Language("Irthuin Elvish", SylvanAlpha, "The language used by Elves in Irthuin.")

Dwarvish = Language("Dwarvish", DwarvishRunic, "The language of the Dwarves.")
                  
Fey = Language("Fey", SylvanRunic, "Also known as the Immortal Fairy Tongue")
                  
Draconic = Language("Draconic", DraconicAlpha, "The language of the Dragons.")
                  
Orcish = Language("Orcish", MithricAlpha, "A primitive language proliferated among other primitive demi-humans through violence. Has no actual alphabet so is commonly transcribed using Mithric.")
                  
OrcishKobold = Language("Orcish(Kobold)", MithricAlpha, "A combination of Orcish and some Draconic spoken by the reptile like Kobolds. Incorporates some Draconic characters.")
                           
OrcishGoblin = Language("Orcish(Goblin)", MithricAlpha, "A pidgin based on Goblin culture and the Orcish language.")
                           
OrcishBugbear = Language("Orcish(Bugbear)", MithricAlpha, "A dialect of Orcish.")
                            
OrcishGnoll = Language("Orcish(Gnoll)", MithricAlpha, "A dialect of Orcish with some Abyssal.")


#dude, gotta find a realworld version of saving throws making stuff. like magic vs spells, charm shit, etc.