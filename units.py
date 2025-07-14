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
        #get weapon
        shooter = self.weapons[weapon]
        #get target
        #calculate chance of hit
        hit = hits(shooter.skill,crit=shooter.crits,reroll=shooter.hreroll)
        totalhits = hit["hits"]
        wound = 0
        if shooter.lethal:
            wound = hit["crits"]
        if shooter.sustain:
            totalhits+= (shooter.sustain+1)*hit["crits"]
        if not (shooter.lethal or shooter.sustain):
            totalhits+=hit["crits"]
        print(totalhits)
        #calculate chance of wound
        stvto = strenVsTough(shooter.strength,target.toughness)
        wound += wounds(stvto,devs = shooter.dev,reroll=shooter.wreroll)["wounds"]*totalhits
        print(wound)
        #calculate chance of save
        unsaved = saves(target.save , shooter.ap, inv = target.invl) * wound
        print(unsaved)
        #times by shots
        shots = shooter.attacks * self.models
        total_wounding = shots*unsaved
        #times by damage
        damage_done=total_wounding*shooter.damage
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
