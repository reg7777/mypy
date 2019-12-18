from cgear import cgear
import sys


def print_gear(gear):
    prnt1 = gear.ret_data()
    sprnt0 = "{:0.2f}".format(cp)
    sprnt1 = "{:0.2f}".format(prnt1[0])
    sprnt2 = "{:0.2f}".format(prnt1[1])
    sprnt3 = "{:0.2f}".format(prnt1[2])
    sprnt4 = "{:0.2f}".format(prnt1[3])
    sprnt5 = "{:0.2f}".format(prnt1[4])
    sprnt6 = "{:0.2f}".format(prnt1[5])
    sprnt7 = "{:0.2f}".format(prnt1[6])
    sprnt8 = "{:0.2f}".format(prnt1[7])
    prnt9 = int(prnt1[8])  # gear number of teeth
    sprnt9 = str(prnt9)
    sprnt10 = "{:0.2f}".format(prnt1[9])


    print("\n Gear circular diameter = " + sprnt10 + " with " + sprnt9 + " teeth")
    print("Mod = " + sprnt1)
    print("Gear outside diameter = " + sprnt2)
    print("Gear root  diameter = " + sprnt3)
    print("Gear tooth angle = " + sprnt4)
    print("Gear circular pitch = " + sprnt5)
    print("Gear tooth depth = " + sprnt6)
    print("Gear pitch(Num. teeth/unit) = " + sprnt7)
    print("Gear tooth thickness = " + sprnt8)
    print("Done \n")


print("\nFor gear given circular diameter and number of teeth, input 'n'")
print("For gear given circular diameter and mod to match a gear, input 'm'")
print("""For two gears with a given ratio to one gear with diameter,
           and number of teeth, imput 'r'""")
choice = input("Your choice ")

#choice = input("Using mod to match a gear (y/n) ")
if choice == "n":
    cp = float(input("Input circular diameter of gear in mm "))
    n = int(input("Input number of teeth  "))
    gear1 = cgear(cp, n, 't')
    print_gear(gear1)

if choice == "m":
    cp = float(input("Input circular diameter of gear in mm "))
    mod = float(input("Input the mod to be used for a matching gear "))
    gear1 = cgear(cp,mod, 'm')
    print_gear(gear1)

if choice == "r":
    cp = float(input("Input the circular diameter for gear one "))
    n = int(input("Imput number of teeth for gear one "))
    ratio = float(input("Input the power ratio relative to gear one "))
    ratio = 1/ratio  # Change power ratio to gear ratio

    gear1 = cgear(cp,n,'t')
    glist = gear1.ret_data()
    mod = glist[0]
    
    gear2_cp  = cp / ratio
    gear2 = cgear(gear2_cp,mod,'m')
    print_gear(gear1)
    print_gear(gear2)


