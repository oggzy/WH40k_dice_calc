from units import *
import pytest

def test_basic_attack():
    weapon = Weapon(1,4,4,0,1)
    weapons = {"test_wep" : weapon}
    shooting = Unit("test_unit1",1,4,4,4,2,weapons)
    shot = Unit("test_unit0",1,4,4,4,2,weapons)
    tester = shooting.attack("test_wep",shot)
    assert round(tester,3) == Decimal(0.125)

def test_lethal_attack():
    weapon = Weapon(1,4,4,1,1,lethal=True)
    weapons = {"test_wep" : weapon}
    shooting = Unit("test_unit1",1,4,4,4,2,weapons)
    shot = Unit("test_unit0",1,4,4,4,2,weapons)
    tester = shooting.attack("test_wep",shot)
    assert round(tester,3) == round(Decimal(0.167),3)

@pytest.mark.skip()
def test_sustain_attack():
    weapon = Weapon(10,4,4,1,1,sustain=2)
    weapons = {"test_wep" : weapon}
    shooting = Unit("test_unit1",1,4,4,4,2,weapons)
    shot = Unit("test_unit0",1,4,4,4,2,weapons)
    tester = shooting.attack("test_wep",shot)
    assert round(tester,3) == round(Decimal(0.208),3)

@pytest.mark.skip()
def test_lethal_sustained_attack():
    weapon = Weapon(1,4,4,1,1,lethal=True,sustain=2)
    weapons = {"test_wep" : weapon}
    shooting = Unit("test_unit1",1,4,4,4,2,weapons)
    shot = Unit("test_unit0",1,4,4,4,2,weapons)
    tester = shooting.attack("test_wep",shot)
    assert round(tester,3) == round(Decimal(0.25),3)

@pytest.mark.skip()
def test_dev_attack():
    pass