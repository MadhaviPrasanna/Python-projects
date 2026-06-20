import random

# ==========================================
# HANGMAN GAME PROJECT
# ==========================================

# Dictionary containing categories and words
word_categories = {
    "Animals": ["tiger", "zebra", "monkey", "rabbit", "elephant"],
    "Fruits": ["apple", "banana", "orange", "grapes", "mango"],
    "Technology": ["python", "laptop", "robot", "keyboard", "monitor"]
}


# Function to display game rules
def display_rules():
    print("\n" + "=" * 50)
    print("            HANGMAN GAME RULES")
    print("=" * 50)
    print("1. A random word will be selected.")
    print("2. You must guess the word one letter at a time.")
    print("3. You can make only 6 incorrect guesses.")
    print("4. Correct guesses reveal letters in the word.")
    print("5. Guess all letters before attempts run out.")
    print("=" * 50)


# Function to select a random category and word
def choose_word():
    category = random.choice(list(word_categories.keys()))
    word = random.choice(word_categories[category])
    return category, word


# Function to display current word
def display_word(hidden_word):
    print("\nCurrent Word:")
    print(" ".join(hidden_word))


# Function to play one game
def play_game():

    category, secret_word = choose_word()

    hidden_word = ["_"] * len(secret_word)

    guessed_letters = []

    wrong_guesses = 0
    max_attempts = 6

    score = 0

    print("\nCategory:", category)
    print("Word Length:", len(secret_word))

    # Main game loop
    while wrong_guesses < max_attempts and "_" in hidden_word:

        display_word(hidden_word)

        print("\nGuessed Letters:", guessed_letters)
        print("Wrong Attempts:", wrong_guesses, "/", max_attempts)
        print("Score:", score)

        guess = input("\nEnter a letter: ").lower()

        # Input Validation
        if len(guess) != 1:
            print("Please enter only ONE letter.")
            continue

        if not guess.isalpha():
            print("Please enter an alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Correct Guess
        if guess in secret_word:

            print("Correct Guess!")

            count = 0

            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    hidden_word[i] = guess
                    count += 1

            score += count * 10

        # Wrong Guess
        else:
            wrong_guesses += 1
            score -= 5

            print("Wrong Guess!")
            print("Remaining Chances:",
                  max_attempts - wrong_guesses)

    # Final Result
    print("\n" + "=" * 50)

    if "_" not in hidden_word:
        print("CONGRATULATIONS!")
        print("You guessed the word successfully.")
        print("Word:", secret_word)
        print("Final Score:", score)

    else:
        print("GAME OVER!")
        print("You have used all attempts.")
        print("Correct Word:", secret_word)
        print("Final Score:", score)

    print("=" * 50)


# Main Program
def main():

    display_rules()

    while True:

        play_game()

        choice = input(
            "\nDo you want to play again? (yes/no): "
        ).lower()

        if choice != "yes":
            print("\nThank you for playing Hangman!")
            print("Project Ended Successfully.")
            break


# Program starts here
main()
