from units import *



def test_basic_attack():
    weapon = Weapon(1,4,4,0,1)
    weapons = {"test_wep" : weapon}
    shooting = Unit("test_unit1",1,4,4,2,weapons)
    shot = Unit("test_unit0",1,4,4,2,weapons)
    tester = shooting.attack("test_wep",shot)
    assert round(tester,3) == Decimal(0.125)


def test_lethal_attack():
    weapon = Weapon(1,4,4,0,1,lethal=True)
    weapons = {"test_wep" : weapon}
    shooting = Unit("test_unit1",1,4,4,2,weapons)
    shot = Unit("test_unit0",1,4,4,2,weapons)
    tester = shooting.attack("test_wep",shot)
    assert round(tester,3) == round(Decimal(0.167),3)


def test_sustain_attack():
    weapon = Weapon(1,4,4,0,1,sustain=2)
    weapons = {"test_wep" : weapon}
    shooting = Unit("test_unit1",1,4,4,2,weapons)
    shot = Unit("test_unit0",1,4,4,2,weapons)
    tester = shooting.attack("test_wep",shot)
    assert round(tester,3) == round(Decimal(0.208),3)


def test_lethal_sustained_attack():
    weapon = Weapon(1,4,4,0,1,lethal=True,sustain=2)
    weapons = {"test_wep" : weapon}
    shooting = Unit("test_unit1",1,4,4,2,weapons)
    shot = Unit("test_unit0",1,4,4,2,weapons)
    tester = shooting.attack("test_wep",shot)
    assert round(tester,3) == round(Decimal(0.25),3)


def test_dev_attack():
    weapon = Weapon(1,4,4,0,1,dev=6)
    weapons = {"test_wep" : weapon}
    shooting = Unit("test_unit1",1,4,4,2,weapons)
    shot = Unit("test_unit0",1,4,4,2,weapons)
    tester = shooting.attack("test_wep",shot)
    assert round(tester,3) == round(Decimal(0.167),3)

def test_ap_attack():
    weapon = Weapon(1,4,4,-3,1)
    weapons = {"test_wep" : weapon}
    shooting = Unit("test_unit1",1,4,4,2,weapons)
    shot = Unit("test_unit0",1,4,4,2,weapons)
    tester = shooting.attack("test_wep",shot)
    assert round(tester,3) == Decimal(0.250)


def test_dmg_attack():
    weapon1 = Weapon(1,4,4,1,1)
    weapon2 = Weapon(1,4,4,1,10)
    weapons = {"test_wep1" : weapon1,"test_wep2" : weapon2}
    shooting = Unit("test_unit1",1,4,4,2,weapons)
    shot = Unit("test_unit0",1,4,4,1,weapons)
    test1 = shooting.attack("test_wep1",shot)
    test10 = shooting.attack("test_wep2",shot)
    test2 = shot.attack("test_wep1",shooting)
    test20 = shot.attack("test_wep2",shooting)
    assert round(test1,3) == round(test10,3)
    assert test2 * 2 == test20