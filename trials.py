rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
while True:
    options = [rock,paper,scissors]
    print("Welcome to Rock,Paper,Scissors!")
    print("Select a number for the respective options:\nRock = 1,Paper = 2,Scissors = 3")
    user_choice = int(input("Select a number:"))
    computer_choice = random.choice(options)
    print("You chose:")
    if user_choice == 1:
        print(rock)
    elif user_choice == 2:
        print(paper)
    elif user_choice == 3:
        print(scissors)
    else:
        print("Try again")
    print("Computer Chooses:")
    print(computer_choice)
    if user_choice == 1:
        if computer_choice == rock:
            print("Its  a draw!")
        elif computer_choice == paper:
            print("You Lose!")
        elif computer_choice == scissors:
            print("You win")
    elif user_choice == 2:
        if computer_choice == rock:
            print("You win!")
        elif computer_choice == paper:
            print("Its a draw!")
        elif computer_choice == scissors:
            print("You Lose!")
    elif user_choice == 3:
        if computer_choice == rock:
            print("You Lose!")
        elif computer_choice == paper:
            print("You Win!")
        elif computer_choice == scissors:
            print("Its a Draw!")
    play_again = input("Do you want to play again?Y/N: ").upper()
    if play_again != "Y":
        print("Thank you for playing!")
        break

