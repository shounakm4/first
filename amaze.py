print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
while True:
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    first = input("You just enter the island and reach a crossroads,do you go left(L) or right(R)?: ").upper()

    if first == "L":
        print("Good job!You survive")
        swim = input("You reach a river bank and need to get across;\nyou also see a boat in the distance that is rowing towards you but is too far away.\nYou can either swim across the bank(1) or wait for the boat(2),what do you do 1 or 2? ")
        if swim == "2":
            print("good job u alive!")
            door = input("You have now reached a building with 3 doors,Red,Green and Blue colours respectively.\nNow, you have a key to open all doors but \nonly one can be opened so you need to select a door to find where the treasure is hidden.\nWhich door do you choose?Red(R),Green(G) or Blue(B)").upper()
            if door == "G":
                print("YOU FOUND THE TREASURE!YOU WIN!")
            elif door == "R":
                print("You got burnt by fire and died in hell :),Game over.")
            elif door == "B":
                print("You got eaten by cookie monster and he made your organs into a stew :),Game over.")
            else:
                print("You lose!")


        else:
            print("You got eaten by an alligator while swimming ;).Game over")
    else:
        print("You fell off a cliff and died :),Game over.")

    play_again = input("Do you want to play again,Y or N? ").upper()
    if play_again != "Y":
        break
