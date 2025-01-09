
class Skill:
    def __init__(self, name, ability, description, profReq=False, isProf=False):
        self.name = name
        self.ability = ability
        self.profRequired = profReq
        self.description = description
        self.isProf = isProf

SkillList = []

#Strength
SkillList.append(Skill("Athletics", "Strength", "Your Athletics check covers difficult situations you encounter while climbing, jumping, or swimming.\n\n• Climb: Athletics checks may be made to climb a sheer or slippery cliff, or cling to a surface while fighting.  Characters trying to climb move at ½ of their usual Movement Rate, rounded down to the nearest 5’ increment.\n\n• High-Jump: Characters may high-jump a number of inches equal to their Movement Rate by making a DC 10 Athletics (Strength) check. For every point higher (or lower) than 10 on the Athletics check, the high-jumper adds (or subtracts) 1 inch.\n\n• Long-Jump: Generally, a character can long-jump a number of feet equal to their Movement Rate divided by 4, by making a DC 10 Athletics (Strength) check. Without a running start of at least 20’ that base distance jumped is halved.  For every point higher (or lower) than 10 on the Athletics check, the long-jumper adds (or subtracts) half of a foot.\n\n• Swim: Athletics checks are made to swim or stay afloat in treacherous currents, storm-tossed waves, or areas of thick seaweed, or when another creature tries to push or pull you underwater or otherwise interfere with your swimming. Characters trying to swim move at ½ of their usual Movement Rate, rounding down to the nearest 5’ increment."))

#Dexterity
SkillList.append(Skill("Acrobatics", "Dexterity", "Your Acrobatics check covers your attempt to stay on your feet in a tricky situation, such as when you’re trying to run across a sheet of ice, balance on a tightrope, or stay upright on a rocking ship’s deck. The DM might also call for an Acrobatics check to see if you can perform acrobatic stunts, including dives, rolls, somersaults, and flips. Characters using Acrobatics to balance upon a narrow, uneven, or slippery surface move at ½ of their usual Movement Rate."))
SkillList.append(Skill("Disable Device", "Dexterity", "This skill is used to open mechanical locks and disable traps, including magical traps. Generally, it takes 1d4 rounds to disarm a device, depending on its complexity. This ability requires the use of a set of Thieves’ Tools, including picks, blank keys, wires, or other appropriate tools.\n\nA successful skill check indicates that the lock has been opened or the trap has been disabled.  If a Disable Device attempt fails when opening a lock, the character cannot try to open the same lock again until the next level of experience is gained, as it is beyond that character’s current ability.  Failure to disarm a trap indicates that the character has set off the trap and suffers the trap’s effect. The DC for checks made to find mundane traps and for Saving Throws against mundane traps is equal to 10 + the Proficiency Bonus + the Dexterity modifier of the character setting the trap.\n\nTo set a trap, or to reset a previously disabled trap, the character must make a successful Disable Device check.    If a character is resetting a trap that he previously disabled, he gains a +5 bonus to this check. Failure to set a trap does not trigger it.  For magical traps (such as a Glyph of Warding) the DC for the Perception and Disable Device checks is equal to the spell’s Saving Throw DC. ", True))
SkillList.append(Skill("Sleight of Hand", "Dexterity", " Whenever you attempt an act of legerdemain or manual trickery, such as planting something on someone else or concealing an object on your person, make a Sleight of Hand check.\n\nThe DM might also call for a Sleight of Hand check to determine whether you can lift a coin purse off another person or slip something out of another person’s pocket.\n\nFinally, Sleight of Hand checks may be made to slip free from bonds or shackles."))
SkillList.append(Skill("Stealth", "Dexterity", "Make a Stealth check when you attempt to conceal yourself from enemies, slink past guards, slip away without being noticed, or sneak up on someone without being seen or heard.\n\nAll characters may attempt Stealth checks to hide from others or move silently.  These checks are always opposed by the target’s Perception check.  Characters using Stealth to move silently move at ½ of their usual Movement Rate.\n\n• Hiding: When you try to hide, make a Stealth check. Until you are discovered or you stop hiding, that check’s total is contested by the Wisdom (Perception) check of any creature that actively searches for signs of your presence.\n\nIf you are being observed, even casually, you can’t hide. If observers are momentarily distracted, though, you can attempt to hide. While the observer averts its attention from your character, you can attempt to get to a hiding place. This check, however, is made with a -5 penalty because your character has to move quickly to the hiding place.\n\nYou cannot hide if there is nothing to hide behind or conceal oneself with. Deep shadows can count as concealment at the Dungeon Master’s discretion.  If you make noise (such as shouting a warning or knocking over a vase), you give away your position. An invisible creature can’t be seen, so it can always try to hide. Signs of its passage might still be noticed, however, and it still has to stay quiet.\n\nIn combat, most creatures stay alert for signs of danger all around, so if you come out of hiding and approach a creature, it usually sees or hears you. However, under certain circumstances, the Dungeon Master might allow you to stay hidden as you approach a creature that is distracted or looking in the opposite direction, allowing you to make a surprise attack before you are seen.\n\n• Stealth versus Passive Perception: When you hide, there’s a chance someone will notice you even if they aren't searching. To determine whether such a creature notices you, the DM compares your Dexterity (Stealth) check with that creature’s passive Wisdom (Perception) score, which equals 10 + the creature’s Wisdom modifier + its Proficiency or Common Ability bonus."))

#Intelligence
SkillList.append(Skill("Arcana", "Intelligence", "Your Arcana check measures your ability to recall lore about spells, magic items, eldritch symbols, magical traditions, the planes of existence, and the inhabitants of those planes.", True))
SkillList.append(Skill("Ciphers", "Intelligence", "This skill may be used to decipher writing in an unfamiliar language, a message written in an incomplete or archaic font, or a message written in code. If the check succeeds, the character understands the general content of a piece of writing. It takes 10 minutes to decipher each page of a script.  The attempt may be made only once per writing.\n\nYou can use this skill to create written ciphers. Others can’t decipher a code you create unless you teach them, they succeed on an Intelligence (Ciphers) check (the DC is equal to your Ciphers skill check result), or they use magic to decipher it. "))
SkillList.append(Skill("History", "Intelligence", "Your History check measures your ability to recall lore about historical events, legendary people, ancient kingdoms, past disputes, recent wars, and lost civilizations."))
SkillList.append(Skill("Perception(Investigation)", "Intelligence", " When you look around for clues and make deductions based on those clues, you may make a Perception check using Intelligence in place of Wisdom. Poring through ancient scrolls in search of a hidden fragment of knowledge might also call for a Perception check based on Intelligence."))
SkillList.append(Skill("Nature", "Intelligence", "Your Nature skill check measures your ability to recall lore about terrain, plants and animals, the weather, and natural cycles."))
SkillList.append(Skill("Poison", "Intelligence", "Proficiency with this skill lets you add your Proficiency Bonus to any Ability Checks you make to craft, identify, or use poisons.", True))
SkillList.append(Skill("Religion", "Intelligence", "Your Religion check measures your ability to recall lore about deities, rites and prayers, religious hierarchies, holy symbols, celestial, fiendish, and undead creatures, and the practices of secret cults."))
#language and craft
languageDesc = "Language checks are typically made to parse the meaning of challenging or semi-legible written passages, to understand idioms and dialects of that tongue, and to gain insight into the culture of speakers of that language. A character fluent in Orcish, for example, would know a bit about Orcish culture and about their social norms."
craftDesc = "Use of this skill allows the character to appraise the craftsmanship and value of items directly related to their Craft with their Proficiency Bonus.  In addition, given time and adequate materials, the character can repair or create such items.  Craft skill checks are usually Intelligence checks, though other abilities (such as Dexterity) may come to bear when crafting items."

#Wisdom
SkillList.append(Skill("Animal Handling", "Wisdom", "When there is any question whether you can calm down a domesticated beast, keep a mount from getting spooked, or intuit an animal’s intentions, the DM might call for an Animal Handling check. You also make an Animal Handling check as a free action in combat or as when you attempt a risky maneuver.\n\nSee Mounted Combat on page 69 for more information on the benefits and limitations on fighting while mounted."))
SkillList.append(Skill("Insight", "Wisdom", "Your Insight check decides whether you can determine the true intentions of a creature, such as when searching out a lie or predicting someone’s next move. Doing so involves gleaning clues from body language, speech habits, and changes in mannerisms."))
SkillList.append(Skill("Medicine", "Wisdom", "A Medicine check lets you try to stabilize a dying companion, diagnose an illness, and help others recover from wounds and ability damage (see page 72)."))
SkillList.append(Skill("Perception", "Wisdom", "Your Perception check lets you spot, hear, or otherwise detect the presence of something. It measures your general awareness of your surroundings and the keenness of your senses.\n\nYou might deduce the location of a hidden object, discern from the appearance of a wound what kind of weapon dealt it, or determine the weakest point in a tunnel that could cause it to collapse.\n\nPerception skill checks usually take an action to perform.  Examining an object takes anywhere from 1 action to 1 minute, depending upon its size and complexity.  Searching a 5’ x 5’ area takes at least 1 minute."))
SkillList.append(Skill("Survival", "Wisdom", "The DM might ask you to make a Survival check to follow tracks, hunt wild game, guide your group through frozen wastelands, identify signs that owlbears live nearby, predict the weather, or avoid quicksand and other natural hazards. Characters using Survival to track another creature move at ½ of their usual Movement Rate"))
#profession too
professionDesc = "Profession skills would allow the character to bring their professional knowledge to bear, where appropriate, or even ply their trade once they have settled down or during their downtime between adventures.  Profession skill checks are usually Wisdom checks but, at times, may involve other ability scores (as the situation warrants)."

#Charisma
SkillList.append(Skill("Deception", "Charisma", "Your Deception check determines whether you can convincingly hide the truth, either verbally or through your actions. This deception can encompass everything from misleading others through ambiguity to telling outright lies. Typical situations include trying to fast-talk a guard, con a merchant, pass yourself off in a disguise, dull someone’s suspicions with false assurances, or maintain a straight face while telling a blatant lie. See page 61 for more information on Social Interaction."))
SkillList.append(Skill("Disguise", "Charisma", "With a successful check, the character can alter his appearance or attempt to impersonate others. The difficulty of the check depends upon the extent of alterations needed to affect the disguise.  When impersonating individuals, the difficulty may be compounded by others’ familiarity with the impersonated person.", True))
SkillList.append(Skill("Intimidate", "Charisma", "When you attempt to influence someone through overt threats, hostile actions, and physical violence, the DM might ask you to make an Intimidation check. Examples include trying to pry information out of a prisoner, convincing street thugs to back down from a confrontation, or using the edge of a broken bottle to convince a sneering vizier to reconsider a decision. See page 61 for more information on Social Interaction."))
SkillList.append(Skill("Persuasion", "Charisma", "When you attempt to influence someone or a group of people with tact, social graces, or good nature, the DM might ask you to make a Persuasion check. Typically, you use Persuasion when acting in good faith, to foster friendships, make cordial requests, or exhibit proper etiquette. Examples of persuading others include convincing a chamberlain to let your party see the king, negotiating peace between warring tribes, or inspiring a crowd of townsfolk.  See page 61 for more information on Social Interaction."))
#performance too
performanceDesc = "audience through your art. When proficiency is taken in the Performance skill the character must choose a type of performance art in which they are proficient: acting, buffoonery, dancing, stringed instruments, percussion instruments, woodwind instruments, singing, etc.  A character who wishes to master more than one mode of Performance must gain proficiency in other Performance skills separately.\n\nUnskilled Performance checks are typically made without a musical instrument, as most musical instruments require some degree of proficiency to use with any degree of aptitude."

def GetSkill(skillz):
    for x in SkillList:
        if x.name == skillz:
            return x
    return None