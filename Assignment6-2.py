import random

start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))

secret_number = random.randint(start, end)

guess_count = 0

while True:
    
    n = int(input("Enter your guess: "))

    guess_count += 1

    if secret_number > n:
        print("The number guessed is Smaller")

    elif secret_number < n:
        print("The number guessed is Larger")

    elif secret_number == n:
        print("You guessed the number")
        print("Total guesses:", guess_count)
        break 

    else:
        print("The input is invalid")