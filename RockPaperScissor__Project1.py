import random
your_name=input("Your name->>")
print("Welcome to Rock_Paper_Scissors",your_name)
while True:
    user_choice=int(input("Game Rules:-\n 1) 0 for Rock\n 2) 1 for Paper\n 3) 2 for Scissors\nYour_Choice\n"))
    if user_choice >=3 or user_choice < 0:
        print("SORRY YOU INTERED WRONG NUMBER")
    else:
        computer_choice=random.randint(0,2)
        print("Computer Choice")
        print(computer_choice)
        if computer_choice==user_choice:
            print("DRAW??")
        elif user_choice == 0 and computer_choice == 2:
            print("YOU WIN.\nCongrats!!")
        elif user_choice == 2 and computer_choice==0:
            print("YOU LOSE.\nBetter Luck Try Next Time!")
        elif computer_choice > user_choice:
            print("YOU LOSE.\nBetter Luck Try Next Time!")
        elif user_choice > computer_choice:
            print("YOU WIN.\nCongrats!!")
    play_again = input("\nDo you want to play again? (YES/NO): ").strip().lower()
    if play_again != 'yes':
        print("Thank you for playing! Goodbye!")
        break


    

