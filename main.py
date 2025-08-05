from units import *
from calculator import * 

print("""
****************************
 Welcome to WH40K dice calc
****************************
""")

def main():
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
                add_unit()
            case "2":
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
    print ("1")
    

### Add weapon
def add_weapon():
    print ("2")

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