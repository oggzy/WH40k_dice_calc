from units import *
from calculator import * 

print("""
****************************
 Welcome to WH40K dice calc
****************************
""")



def main():

    global units
    units = []

    while(True):
        print("""1 : Add unit
2 : Add Weapon
3 : Calculate Average Attack
4 : Remove unit
5 : Remove weapon
Q : quit""")
        x = input("\nPlease Select an option : ")
        match x:
            case "1":
                new_U = add_unit()
                units.append(new_U)

                
            case "2":
                if not units:
                    print ("No units availiable. Please add a unit before adding a weapon.")
                else:
                    add_weapon()
                
            case "3":
                attack()
                
            case "4":
                rm_unit()
                
            case "5":
                rm_weapon()
                
            case x if x in "qQ":
                break
            case _:
                print ("\nSorry I didnt understand that input. please try again.\n")

    print("\nThank you for using the WH40k dice calc\n")


### Add unit
def add_unit():
    print("\nplease input the value for each of your units following attributes (for saves please input the dice roll required eg. 4+ = 4)")
    attributes = ['Number of Mobels',"toughness","save","wounds","invulnerable save (if none enter 0)","feel no pain (if none enter 0)"]
    name = input("Name :")
    input_att = [name]
    for x in attributes:
        y = input(f"{x} :")
        if int(y):
            input_att.append(int(y))
    weapons = {}
    while(True):
        print("please input the weapons availiable to this unit one by one.\n(please add weapons to a unit before attempting an attack calculation)")
        q = input("add weapon (y/n):")
        match q:
            case q if q in "Nn":
                break
            case q if q in "Yy":
                wep = add_weapon(weapons)
                weapons.update(wep)
            case _:
                print ("\nSorry I didnt understand that input. please try again.\n")
    
    
    input_att.insert(5, weapons)

    new_unit = Unit(*input_att)

    print("\nNew unit created :" + str(new_unit)+"\n")

    return new_unit
    
    

            

### Add weapon
def add_weapon(weapons="n"):
    return_wep = False
    if weapons == "n":
        print("\nplease select an availiable unit to assign this weapon to. (eg. for 1 : necron warriors please input 1)\n")
        for x in range(len(units)): 
            print(f"{x} : {str(units[x].name)}\n")
        while(True):
            unit_input = input("Selection : ")
            if unit_input in str(range(len(units))):
                wep_unit = units[int(unit_input)]
                weapons = wep_unit.weapons
                break
            else:
                print ("\nSorry I didnt understand that input. please try again.\n")
    else:
        return_wep = True
    print("\nplease input the value for each of your weapons following  (for skill / ap please input the value from datasheet without a sign eg. 4+ = 4 / -1 = 1)")
    attributes = ["attacks","weapon skill","strength","armour penetration","damage"]
    while(True):
        wep_name = input("Name :")
        if wep_name not in weapons:
            break
        else:
            print("a weapon of this name already exists. please give weapons unique names.\n")
    input_att = []
    for x in attributes:
        y = input(f"{x} :")
        if int(y):
            input_att.append(abs(int(y)))
    if return_wep:
        return {wep_name : Weapon(*input_att)}
    else:
        wep_unit.weaponise(wep_name,input_att)
        print("success")
        

### Calculate Average Attack
def attack():
    print("3")

### remove unit
def rm_unit():
    if not units:
        print("\nNo units availiable\n")
        return
    print("\nplease select a unit to remove. (eg. for 1 : necron warriors please input 1)\n")
    for x in range(len(units)): 
        print(f"{x} : {units[x].name}\n")
    print("B : back\n")
    while(True):
        unit_input = input("Selection : ")
        if unit_input in str(range(len(units))):
            units.pop(int(unit_input))
            print("Success")
            break
        elif unit_input in "Bb":
            print("")
            break
        else:
            print ("\nSorry I didnt understand that input. please try again.\n")



### remove weapon
def rm_weapon():
    if not units:
        print("\nNo units availiable\n")
        return
    print("\nplease select an availiable unit to remove this weapon from. (eg. for 1 : necron warriors please input 1)\n")
    for x in range(len(units)): 
        print(f"{x} : {str(units[x])}\n")
    unit_input = input("Selection :")
    unit = units[int(unit_input)]
    print("\nplease select an availiable weapon to remove (eg. for 1 : gauss flayer please input 1)\n")
    weps = list(unit.weapons.keys())
    for x in range(len(weps)): 
        print(f"{x} : {str(weps[x])}\n")
    wep_input = input("Selection :")
    unit.weapons.pop(str(weps[int(wep_input)]))


main()