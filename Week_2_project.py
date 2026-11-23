import random 
secret_number = random.randint(1, 100)



# 3. Ask the user to choose difficulty
print("\nChoose your difficulty:")
print("1. Easy (5 attempts)")
print("2. Medium (3 attempts)")
print("3. Hard (2 attempts)")

level = input("\nEnter your choice: ")

# 4. Set attempts based on difficulty
if level == "1":
    attempts = 5
    print("\nYou selected Easy!")

elif level == "2":
    attempts = 3
    print("\nYou selected Medium!")

elif level == "3":
    attempts = 2
    print("\nYou selected Hard!")

else:
    print("\nInvalid choice! Please restart the game.")
    attempts = 0

# 5. Count the attempts used
used_attempts = 0

# 6. Start the game
while attempts > 0:

    # Ask the user to guess the number
    guess = int(input("\nEnter your guess (1-100): "))

    # Increase used attempts
    used_attempts += 1

    # Check the user's guess
    if guess == secret_number:
        print("\nCongratulations! You guessed correctly!")
        print("The secret number was:", secret_number)
        print("Total attempts used:", used_attempts)
        break

    elif guess > secret_number:
        print("Too High!")

    else:
        print("Too Low!")

    # Reduce remaining attempts
    attempts -= 1

    # Display remaining attempts
    print("Remaining guesses:", attempts)

# 7. Check if the player lost
if attempts == 0 and guess != secret_number:
    print("\nGAME OVER!")
    print("The correct number was:", secret_number)
    print("You used all your attempts.")

# 8. End message
print("\nThank you for playing!")
