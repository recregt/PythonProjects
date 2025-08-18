import random
secret_number = random.randint(1,100)
print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        
        if guess < secret_number:
            print("Guess higher.")
        elif guess > secret_number:
            print("Guess lower.")
        else:
            print("Congratulations! You guessed correctly.")
            break
    except ValueError:
        print("Invalid input. Please enter a number.")