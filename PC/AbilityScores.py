
class AbilityScores:
    def __init__(self, scores = [9,9,9,9,9,9], modifiers = []):
        
        self.scores = {
            "Strength": scores[0],
            "Dexterity": scores[1],
            "Constitution": scores[2],
            "Intelligence": scores[3],
            "Wisdom": scores[4],
            "Charisma": scores[5]
        }
        
        self.mods = modifiers

    def GetRawScore(self, ability):
        return self.scores[ability]

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
    
    def GetRawMod(self, ability):
        return self.GetAbilityScoreMod(self.scores[ability])

    def GetMod(self, ability):
        mod = self.GetAbilityScoreMod(self.scores[ability])
        for x in self.mods:
            if x.abilityScore == "Strength":
                mod += x.modifier
        return mod

    def GetModDesc(self, ability):
        theMods = []
        for x in self.mods:
            if x.abilityScore == ability:
                theMods.append(x)
        return theMods

class AbilityScoreModifier:
    def __init__(self, abilityScore, mod, name="", desc=""):
        self.abilityScore = abilityScore
        self.mod = mod
        self.name = name
        self.desc = desc