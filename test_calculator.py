from calculator import *

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

def test_svt():
    test_out = strenVsTough(1,1)
    woundon=3
    assert test_out == woundon
    test_out = strenVsTough(2,1)
    woundon=5
    assert test_out == woundon
    test_out = strenVsTough(3,2)
    woundon=4
    assert test_out == woundon
    test_out = strenVsTough(1,2)
    woundon=1
    assert test_out == woundon
    test_out = strenVsTough(2,3)
    woundon=2
    assert test_out == woundon

def test_wound():
    test_out = wounds(3)
    woundon= dice_roll*3
    assert test_out == {"wounds":woundon, "devs":0}

def test_wound_reroll():
    test_out = wounds(3,reroll=3)
    woundon= dice_roll*3 + dice_roll*3*dice_roll*3 
    assert test_out == {"wounds":woundon, "devs":0}

def test_wound_devs():
    test_out = wounds(3,devs=6)
    woundon= dice_roll*3-dice_roll
    devon = dice_roll*1
    assert test_out == {"wounds":woundon, "devs":devon}

def test_saves():
    test_out = saves(3,0)
    saved= dice_roll*4
    assert test_out == saved

def test_saves_reroll():
    test_out = saves(4,0,reroll=3)
    saved= dice_roll*3 + dice_roll*3*dice_roll*3 
    assert test_out == saved

def test_saves_ap():
    test_out = saves(2,1)
    saved= dice_roll*4
    assert test_out == saved

def test_saves_inv():
    test_out = saves(3,6,inv=3)
    saved= dice_roll*4
    assert test_out == saved

def test_saves_no_save():
    test_out = saves(3,6)
    saved = 0
    assert test_out == saved