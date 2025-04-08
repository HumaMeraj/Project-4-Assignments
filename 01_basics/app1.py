
# Constants
PROMPT: str = "What do you want? "
JOKE: str = "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY: str = "Sorry I only tell jokes."

def main():
    # Ask the user for input
    user_input = input(PROMPT)

    # Check if input is exactly "Joke"
    if user_input == "Joke":
        print(JOKE)
    else:
        print(SORRY)

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
