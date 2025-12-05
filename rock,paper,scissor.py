import random
choies= ["rock","paper","scissor"]

while True:
    print("welcome to the game")
    print("1.rock")
    print("2.paper")

    print("3.scissor")
    print("4.exit the game")
    choice = int(input("enter your choice: "))
    if choice == 4 :
        print("thanks for playing")
        print("bye")
        break
    if choice not in [1,2,3]:
        print("invalid choice")
        continue

    #logical part
    user_choice = choies[ choice - 1 ]
    computer_choice = random.choice(choies)
    print(f"your choice is:{user_choice}")
    print(f"computer choice is:{computer_choice}")

    if computer_choice == user_choice :
        print("its a tie")

    elif (computer_choice == "rock" and user_choice == "scissor") or \
          (computer_choice == "paper" and user_choice == "rock") or \
            (computer_choice == "scissor" and user_choice == "paper"):
        print("you lose")
    else:
        print("you win")

