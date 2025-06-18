from calculator import *

class Unit:
    def __init__(self,name,models,toughness,save,invl,wounds,weapons,fnp=7):
        self.name = name
        self.models = models
        self.toughness = toughness
        self.save = save
        self.invl = invl
        self.wounds = wounds
        self.weapons = weapons
        self.fnp = fnp
    
    def attack(self,weapon,target):
        shooter = self.weapons[weapon]
        totalshots = shooter.attacks * self.models
        hit = hits(shooter.skill,crit=shooter.crits,reroll=shooter.hreroll)
        totalhits = 1-(1-hit["hits"])**totalshots
        if shooter.lethal:
            wound = hit["crits"] * totalshots     
        else:
            totalhits += hit["crits"] * totalshots
            wound = 0
        if shooter.sustain:
            totalhits+= (shooter.sustain)*hit["crits"] 
        stvto = strenVsTough(shooter.strength,target.toughness)
        wounded = wounds(stvto,devs = shooter.dev,reroll=shooter.wreroll)
        wound += 1-(1-wounded["wounds"])**totalhits
        unsaved = saves(target.save , shooter.ap, inv = target.invl) * wound
        return unsaved      


class Weapon:
    def __init__(self,attacks,skill,strength,ap,damage,crits=6,lethal=False,sustain=False,hreroll=0,dev=7,wreroll=0):
        self.attacks = attacks
        self.skill = skill
        self.strength = strength
        self.ap = ap
        self.damage = damage
        self.crits = crits
        self.lethal = lethal
        self.sustain = sustain
        self.hreroll = hreroll
        self.dev = dev
        self.wreroll = wreroll
