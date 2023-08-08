i = 1
while i <= 3:
    Guess = int(input("Guess "))
    i = i + 1
    if Guess == 9:
        print("You win!")
        break
else: print("You lose!")