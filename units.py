from calculator import *

class Unit:
    def __init__(self,name,models,toughness,save,wounds,weapons,invl=7,fnp=7):
        self.name = name
        self.models = models
        self.toughness = toughness
        self.save = save
        self.invl = invl
        self.wounds = wounds
        self.weapons = weapons
        self.fnp = fnp
    
    def attack(self,weapon,target):
        #get weapon
        shooter = self.weapons[weapon]
        #get target
        #calculate chance of hit
        hit = hits(shooter.skill,crit=shooter.crits,reroll=shooter.hreroll)
        totalhits = hit["hits"]
        wound = 0
        if shooter.lethal:
            wound = hit["crits"]
        else:
            totalhits+=hit["crits"]
        if shooter.sustain:
            totalhits+= (shooter.sustain)*hit["crits"]
        #calculate chance of wound
        stvto = strenVsTough(shooter.strength,target.toughness)
        wounding=wounds(stvto,devs = shooter.dev,reroll=shooter.wreroll)
        wound += wounding["wounds"]*totalhits
        #calculate chance of save
        unsaved = saves(target.save , shooter.ap, inv = target.invl) * wound + wounding["devs"]*totalhits
        #times by shots
        shots = shooter.attacks * self.models
        total_wounding = shots*unsaved
        #times by damage (min of damage and wounds)
        damage_done=total_wounding*min(shooter.damage, target.wounds)
        #calculate chance of fnp
        ##deal_damage()
        #return average number of models killed
        return damage_done


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
