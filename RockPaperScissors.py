import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while True:
        user = input("Pick rock, paper, or scissors: ").lower()

        if user not in choices:
            print("that's not even an option buddy 💀")
            continue

        computer = random.choice(choices)
        print("Computer picked:", computer)

        if user == computer:
            print("TIE TIE TIE BUDDY")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("you win heres a cookie 🍪")
            user_score += 1
        else:
            print("you lost 💀")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        again = input("play again? (y/n): ").lower()
        if again != "y":
            break

    try:
        with open("game_results.txt", "w") as file:
            file.write(f"Final Score:\nYou: {user_score}\nComputer: {computer_score}\n")
        print("results saved to game_results.txt")
    except:
        print("error saving file 😭")

    print("thanks for playing ✌️")


play_game()
