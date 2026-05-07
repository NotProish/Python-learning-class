import random

def start_cheat_code():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    last_distance = None

    print("The ISA secret number game that's for cool people only 😎")
    print("Guess the secret number between 1 and 100. You have 10 attempts.")
   

    while attempts < max_attempts:
        user_input = input("Enter your guess: ").lower()

        # cheat code
        if user_input == "isacheatcode":
            print("Cheat code activated! The secret number is:", secret_number)
            continue

        try:
            guess = int(user_input)

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

        except ValueError:
            print("That's not a valid number. Please try again.")
            continue

        attempts += 1
        distance = abs(secret_number - guess)

        if distance == 0:
            print(f"Congratulations! You've guessed the secret number {secret_number} in {attempts} attempts!")
            break
        elif last_distance is not None:
            if distance < last_distance:
                print("Warmer! You're getting closer.")
            else:
                print("Colder! You're getting farther away.")
        else:
            print("This is your first guess!")

        last_distance = distance

    else:
        print("You ran out of attempts womp womp")

    print(f"\nGame Over. The secret number was {secret_number}. Thanks for playing!")


start_cheat_code()