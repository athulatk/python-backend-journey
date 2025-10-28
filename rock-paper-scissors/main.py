import random

def play_round():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("\nChoose rock, paper, or scissors: ").lower()

    if user_choice == 'q':
        return None

    if user_choice not in choices:
        print("Invalid choice. Try again.")
        return True

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a Tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")

    return True


def main():
    print("Welcome to Rock–Paper–Scissors!")
    print("Press 'q' anytime to quit.")

    while True:
        keep_playing = play_round(score)
        if keep_playing is None:
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
