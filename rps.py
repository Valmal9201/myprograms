import random
guess = input("Rock, Paper, or Scissors?: ")
comp = random.randrange(0, 3) # 0: Rock, 1: Paper, 2: Scissors
while True:
    print(f"User thrown: {guess} and the CPU thrown: {comp} (0: Rock, 1: Paper, 2: Scissors)")
    if guess == "Rock" and comp == 1:
        print("You Lose!")
    elif guess == "Rock" and comp == 0:
        print("You Tied!")
    elif guess == "Paper" and coin == 2:
        print("You Lose!")
    elif guess == "Paper" and comp == 1:
        print("You Tied!")
    elif guess == "Scissors" and coin == 0:
        print("You Lose!")
    elif guess == "Scissors" and comp == 2:
        print("You Tied!")
    else:
        print("You Win!")
    exit_status = input("End the game (Y/N): ")
    if exit_status == "Y":
        break