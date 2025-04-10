import random

print("Welcome to the High-Low Game!")
print("--------------------------------")

score = 0
rounds = 5  # total rounds

for round_number in range(1, rounds + 1):
    print(f"\nRound {round_number}")    
    # 🥅 Milestone #1: Generate random numbers
your_number = random.randint(1, 100)
computer_number = random.randint(1, 100)   
print(f"Your number is {your_number}")
# 🥅 Milestone #2: Get user input
guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower() 
# 🥅 Milestone #3: Game logic
if guess == "higher" and your_number > computer_number:
    print(f"You were right! The computer's number was {computer_number}")
    score += 1  # 🥅 Milestone #5
elif guess == "lower" and your_number < computer_number:
    print(f"You were right! The computer's number was {computer_number}")
    score += 1
else:
    print(f"Aww, that's incorrect. The computer's number was {computer_number}")
# Show current score after every round
print(f"Your score is now {score}")

# End of the game
print("\nThanks for playing!")
