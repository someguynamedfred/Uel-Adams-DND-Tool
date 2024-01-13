import random

import os

#update this to go by a                                                                                                                         relative file
os.chdir (r'C:\Users\tahda\OneDrive\Desktop\Mega\Portfolio\py\DNDScript')

variable_list = []
with open ("UelAdams.txt") as myfile:
    for myline in myfile:
        variable_list.append(myline.rstrip("\n"))

level = (variable_list[0])
max_hp = (variable_list[2])
curr_hp = (variable_list[1])

#print (variable_list)

stre = (variable_list[3])
strer = (variable_list[4])
dex = (variable_list[5])
dexr = (variable_list[6])
con = (variable_list[7])
conr = (variable_list[8])
inte = (variable_list[9])
intr = (variable_list[10])
wis = (variable_list[11])
wisr = (variable_list[12])
cha = (variable_list[13])
char = (variable_list[14])
init = (variable_list[15])

abilsc = [stre, dex, con, inte, wis, cha]

while True:
    #let's have the name and the class come from the text document as well
    print ("Samuel - Uel - Adams.\nLevel " + (level) + " Warlock - Fiend Diety\n") 
    print ("Current Health = " + (max_hp) + "/" + (curr_hp))
    n1 = input ("\nWhat would you like to do? ")

#exit
    if n1 == "exit":
        exit()

#this is for general dice rolls (now with multi-dice support!)
#it should go here as well for saving throws
    elif n1 == "roll" or n1 == "r":
        number_rolls, dice_faces = input ("How many dice and how many faces? ") .split ()
        modifier = input ("What is the modifier? ")
        results = []
        while int(number_rolls) > 0:
            r1 = random.randint (1, int(dice_faces))
            results.append (r1)
            number_rolls = (int(number_rolls) - 1)
        print ("\nYou rolled a " + (str(results)))
        print ("The sum total of the dice is " + str(sum(results)) + " and your modifier is " + str(modifier))
        results.append (int(modifier))
        print ("Your total is " + str(sum(results)) + "\n\n")
        input ()

#saving throws
    elif n1 == "save" or n1 == "saving throw":
        save = input ("What save? ")
        if save == "str":
            modifier = (strer)      
        if save == "dex":
            modifier = (dexr)
        if save == "con":
            modifier = (conr)
        if save == "int":
            modifier = (intr)
        if save == "wis":
            modifier = (wisr)
        if save == "cha":
            modifier = (char)
        r1 = random.randint (1, 20)
        r2 = (int(r1) + int(modifier))
        print ("\nYou rolled the following: \n" + (str(r1)))
        print ("You rolled a " + str(r1) + " and your modifier is " + str(modifier))        
        input ("Your saving throw is a " + str(r2) + "\n\n")
        n1 = "unknown"

#d20
    elif n1 == "d20":
        n2 = random.randint (1, 20)
        n3 = input ("\nWhat is the modifier? ")
        n4 = (int(n2) + int(n3))
        print ("You rolled a " + str(n2) + " + " + str(n3) + " = " + str(n4)) 
        input ("Your total is " + str(n4) + "\n\n")
        n1 = "unknown"
 
#initiative tracker
#init -                                                                                                                                             add this to the text document
    elif n1 == "Initiative" or n1 == "initiative" or n1 == "init":
        print ("Your initiative modifier is +" + (str(init)))
        n3 = random.randint (1, 20)
        n4 = (int(init) + int(n3))
        print ("You rolled a " + str(n3) + " + " + str(init) + " = " + str(n4)) 
        input ("Your total is " + str(n4) + " and your Dex is 14.\n\n")
        n1 = "unknown"

#abilities

    elif n1 == "ability scores" or n1 == "abs":
        print ("\nStr " + str(stre) + " +" + str(strer) + "\nDex " + str(dex) + " +" + str(dexr) + "\nCon " + str(con) + " +" + str(conr) + "\nInt " + str(inte) + " +" + str(intr) + "\nWis " + str(wis) + " +" + str(wisr) + "\nCha " + str(cha) + " +" + str(char) + "\n\n")
#spells

#eldritch blast
    elif n1 == "spells" or n1 == "spell":
        spell = input ("\nWhat spell will you be casting? ")
        if spell == "Eldritch blast" or spell == "eldritch blast" or spell == "eb":
            print ("\n\n--Eldritch Blast--\nA beam of crackling energy streaks toward a creature within range. Make a ranged spell attack against the target. \nOn a hit, the target takes 1d10 force damage. \nThe spell creates more than one beam when you reach higher levels: two beams at 5th level, three beams at 11th level, and four beams at 17th level. \nYou can direct the beams at the same target or at different ones. Make a separate attack roll for each beam.")
            c1 = input ("\n\nWould you like to cast this spell? ")
            if c1 == "yes" or c1 == "Yes" or c1 == "y":
                n2 = random.randint (1, 20)
                n3 = 7
                n4 = (int(n2) + int(n3))
                print ("\nYou rolled a " + str(n2) + " + " + str(n3) + " = " + str(n4)) 
                print ("You rolled " + str(n4) + " to hit.")
                hr2 = input ("Did you hit? ")     
                if hr2 == "yes" or hr2 == "y":
                    dr2 = 4
                    print ("\nYour spell modifier is " + str(dr2) + ".")
                    n3 = random.randint (1, 10)
                    n4 = (int(dr2) + int(n3))
                    print ("You rolled a " + str(n3) + " + " + str(dr2) + " = " + str(n4)) 
                    print ("You deal " + str(n4) + " necrotic damage." )
                    c2 = input ("\nDo you roll again? ")
                    if c2 == "y" or c2 == "yes":
                        n2 = random.randint (1, 20)
                        n3 = 7
                        n4 = (int(n2) + int(n3))
                        print ("\nYou rolled a " + str(n2) + " + " + str(n3) + " = " + str(n4)) 
                        print ("You rolled " + str(n4) + " to hit.")
                        hr2 = input ("Did you hit? ")     
                        if hr2 == "yes" or hr2 == "y":
                            dr2 = 4
                            print ("\nYour spell modifier is " + str(dr2) + ".")
                            n3 = random.randint (1, 10)
                            n5 = (int(dr2) + int(n3))
                            print ("You rolled a " + str(n3) + " + " + str(dr2) + " = " + str(n5)) 
                            n6 = (n5 + n4)
                            input ("You deal " + str(n5) + " necrotic damage. For a total of " + str(n6) + " damage this turn.\n\n")     
#fireball 
        elif spell == "fireball" or spell == "fb": 
            print ("\n\n--Fireball--\nA bright streak flashes from your pointing finger to a point you choose within range and then blossoms with a low roar into an explosion of flame. \nEach creature in a 20-foot-radius sphere centered on that point must make a Dexterity saving throw. \nA target takes 8d6 fire damage on a failed save, or half as much damage on a successful one.\nYou have a range of 150ft.")
            c1 = input ("\n\nWould you like to cast this spell? ")
            if c1 == "yes" or c1 == "Yes" or c1 == "y":
                target_dex_save = 15
                print ("\nAll targets must pass a DC" + str(target_dex_save) + " Dexterity Saving Throw." )
                n3 = random.randint (1, 10)

#attack
    elif n1 == "attack" or n1 == "hellscythe":
        print ("\nYou attack with your hellscythe.")
        n3 = 3
        n2 = random.randint (1, 20)
        n4 = (int(n2) + int(n3))
        print ("You rolled a " + str(n2) + " + " + str(n3) + " = " + str(n4)) 
        print ("You rolled " + str(n4) + " to hit.")
        hr2 = input ("\nDid you hit? ")     
        if hr2 == "yes" or hr2 == "y":
            dr2 = 3
            print ("\nYour damage modifier is " + str(dr2) + ".")
            n3 = random.randint (1, 10)
            n4 = (int(dr2) + int(n3))
            print ("You rolled a " + str(n3) + " + " + str(dr2) + " = " + str(n4)) 
            print ("You deal " + str(n4) + " slashing damage.\n\n" )

#damage dealt