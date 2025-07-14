##shots, hit rolls, wound roll, crit, devistating, AP, save, invuln, Damage, fnp, wound
from decimal import Decimal

dice_roll = Decimal(1/6)

def hits(ws,crit=6,reroll=0):
    hit_perc = dice_roll*(7-ws-(7-crit))
    hit_perc+= dice_roll * reroll * hit_perc
    crit_perc = dice_roll*(7-crit)
    crit_perc+= dice_roll * reroll * crit_perc
    return {"hits":hit_perc, "crits":crit_perc}

def wounds(svt,devs=7,reroll=0):
    wound = dice_roll*svt
    wound+= dice_roll * reroll * wound
    dev=0
    if devs != 7:
        dev = dice_roll*(7-devs)
        dev+= dice_roll*reroll*dev
        wound -= dev
    return {"wounds":wound, "devs":dev}

def strenVsTough(stren,tough):
    if stren/2 >= tough:
        svt = 5
    elif stren > tough:
        svt = 4
    elif stren <= tough/2:
        svt = 1
    elif stren < tough:
        svt = 2
    else:
        svt = 3
    return svt

def saves(sv,ap,inv=7,reroll=0):
    save = 7-sv-ap
    if 7-inv > save:
        save = 7-inv
    saved = dice_roll*save
    saved+= dice_roll * reroll * saved
    return saved

def deal_damage(dmg,saved,fnp):
    fnp_roll = 7-fnp
    damaged = fnp_roll*dice_roll*(1-saved)*dmg
