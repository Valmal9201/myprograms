
#random.randrange(a, b) = returns randon in from [a, b)
# a < b

# My Solution
import random
user = input("Enter heads or tails: ")
program = random.randrange(1,3) # 1 = head, 2 = tail
again = True
head = 0
tail = 0

while again:
    if user == "heads":
        if (program == 1):
            head += 1
            print("You Win!")
        else:
            tail += 1
            print("You Lose!")
    else:
        if (program == 1):
            head += 1
            print("You Lose!")
        else:
            tail += 1
            print("You Win!")
    end = input("Would you like to play again? Yes or No: ")
    if (end == "No"):
        break
    else:
        print("Enjoy your next game.")

print(f"heads: {head}\ntails: {tail}")

# In Class Solution
import random
heads = 0 # variable initialization
tails = 0 # variable initialization
# iteration = loops
guess = input("Heads or Tails?: ")
coin = random.randrange(0,2) # 0: heads, 1: tails

while True:
    print(f"User guessed: {guess} and Coin flipped to: {coin}")
    if guess == "Heads" and coin == 0:
        print("You Win!")
    elif guess == "Tails" and coin == 1:
        print("You Win!")
    else:
        print("You Lose!")
    if coin == 0:
        heads += 1
    else:
        tails += 1
    exit_status = input("End the game: (Y/N)")
    if exit_status == "Y":
        break
# end of while loop
print(f"Number of Heads: {heads} | Number of Tails: {tails}")