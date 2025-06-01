from calculator import hits, wounds
from decimal import Decimal

dice_roll= Decimal(1/6)

def test_hits():
    test_out = hits(4)
    hit =dice_roll*2
    crit = dice_roll*1
    assert test_out == {"hits":hit, "crits":crit}

def test_hits_reroll():
    test_out = hits(4,reroll=1)
    hit = dice_roll*2+dice_roll*dice_roll*2
    crit = dice_roll*1+dice_roll*dice_roll
    assert test_out == {"hits":hit, "crits":crit}
    test_out = hits(4,reroll=3)
    hit = dice_roll*2+dice_roll*3*dice_roll*2
    crit = dice_roll*1+dice_roll*3*dice_roll
    assert test_out == {"hits":hit, "crits":crit}


def test_hits_crit():
    pass
    test_out = hits(4,crit=5)
    hit = dice_roll*1
    crit = dice_roll*2
    assert test_out == {"hits":hit, "crits":crit}

def test_wound():
    test_out = wounds(1,1)
    woundon=dice_roll*3
    assert test_out == {"wounds":woundon, "devs":0}
    test_out = wounds(2,1)
    woundon=dice_roll*5
    assert test_out == {"wounds":woundon, "devs":0}
    test_out = wounds(3,2)
    woundon=dice_roll*4
    assert test_out == {"wounds":woundon, "devs":0}
    test_out = wounds(1,2)
    woundon=dice_roll*1
    assert test_out == {"wounds":woundon, "devs":0}
    test_out = wounds(2,3)
    woundon=dice_roll*2
    assert test_out == {"wounds":woundon, "devs":0}

def test_wound_reroll():
    test_out = wounds(1,1,reroll=3)
    woundon= dice_roll*3 + dice_roll*3*dice_roll*3 
    assert test_out == {"wounds":woundon, "devs":0}

def test_wound_devs():
    test_out = wounds(1,1,devs=6)
    woundon= dice_roll*3-dice_roll
    devon = dice_roll*1
    assert test_out == {"wounds":woundon, "devs":devon}


