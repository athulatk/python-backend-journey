import random

def play_round():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("\nChoose rock, paper, or scissors: ").lower()

    if user_choice == 'q':
        return None

    if user_choice not in choices:
        print("Invalid choice. Try again.")

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
        return 1
    else:
        print("Computer wins!")

    return 0


def main():
    print("Welcome to Rock–Paper–Scissors!")
    print("Press 'q' anytime to quit.")
    score = 0

    while True:
        updated_score = play_round()
        if updated_score is None:
            print("Your score: ", score)
            print("Thanks for playing! Goodbye!")
            break
        score += updated_score


if __name__ == "__main__":
    main()
