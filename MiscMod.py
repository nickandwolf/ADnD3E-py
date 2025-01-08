#a class to support misc bonuses and process them

class MiscModifier:
    def __init__(self, name, type, trigger, modifier=0):
        self.name = name
        self.type = type
        self.trigger = trigger
        self.modifier = modifier

'''
modTypes = 
        ["weapon attack", "weapon damage", "race attack", "race damage",
        "race AC", "saving throw", "skill", "weapon prof", "special ability",
        "ability modifier"]
'''

#dude, gotta find a realworld version of saving throws making stuff. like magic vs spells, charm shit, etc.