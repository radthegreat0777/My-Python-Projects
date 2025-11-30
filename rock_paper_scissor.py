import random

while True:
    choice = ["rock", "paper", "scissors"]
    computer = random.choice(choice)

    print("\n🎮 New Game Started! Choose '🪨 rock', '📃 paper', or '✂️ scissors'.")

    while True:
        try:
            user = input("Enter your choice (rock, paper, scissors): ").lower()
            if user not in choice:
                print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")
                continue

            if (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper") or (user == "paper" and computer == "rock"):
                print(f"""
                    Congrats! You win!
                    Computer chose {computer} and you chose {user}
                """)
                break  

            elif user == computer:
                print(f" It's a tie! \nComputer chose {computer} and you chose {user}")
                break

            else:
                print(f" You lose! \nComputer chose {computer} and you chose {user}")
                break
            
        except ValueError as e:
            print(f"Error: {e}")

    replay_game = input("Do you want to play again? (yes/no): ").lower()

    if replay_game not in ["yes", "y"]:
        print("Thanks for playing 👋")
        break