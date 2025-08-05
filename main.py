from units import *
from calculator import * 

print("""
****************************
 Welcome to WH40K dice calc
****************************
""")

def main():
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
        print("please input the weapons availiable to this unit one by one. Press f when done.\n(please add weapons to a unit before attempting an attack calculation)")
        w = input("weapon name:")
        match w:
            case q if q in "Ff":
                break
            case _:
                wep = add_weapon(w)
                weapons.update({w:wep})
    
    input_att.insert(5, weapons)

    new_unit = Unit(*input_att)
    
    print("\nNew unit created :" + str(new_unit)+"\n")

            

### Add weapon
def add_weapon(name=0):
    print ("2")
    return "pass"

### Calculate Average Attack
def attack():
    print("3")

### remove unit
def rm_unit():
    print("4")

### remove weapon
def rm_weapon():
    print("5")


main()