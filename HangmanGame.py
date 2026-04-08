import random

# ── Predefined word list ──────────────────────────────────────────────────────
WORDS = ["python", "hangman", "coding", "keyboard", "laptop"]

# ── Hangman ASCII stages (0 = fresh, 6 = game over) ──────────────────────────
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========""",
]

MAX_WRONG = 6


def display_state(guessed_letters, secret_word, wrong_count, wrong_letters):
    """Print the current hangman figure, word progress, and wrong guesses."""
    print(HANGMAN_STAGES[wrong_count])
    print()

    # Show word with blanks for unguessed letters
    display_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )
    print(f"  Word: {display_word}")
    print(f"  Wrong guesses ({wrong_count}/{MAX_WRONG}): {', '.join(sorted(wrong_letters)) if wrong_letters else '-'}")
    print()


def get_guess(guessed_letters):
    """Prompt the player for a valid, new single letter."""
    while True:
        guess = input("  Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠  Please enter a single letter (a-z).")
        elif guess in guessed_letters:
            print(f"  ⚠  You already guessed '{guess}'. Try another.")
        else:
            return guess


def play():
    """Run one full game of Hangman."""
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_letters = set()
    wrong_count = 0

    print("\n" + "=" * 40)
    print("       Welcome to HANGMAN!")
    print("=" * 40)
    print(f"  The word has {len(secret_word)} letters. Good luck!\n")

    while True:
        display_state(guessed_letters, secret_word, wrong_count, wrong_letters)

        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            print(f"  🎉 You won! The word was '{secret_word}'.")
            break

        # Check lose condition
        if wrong_count >= MAX_WRONG:
            print(f"  💀 Game over! The word was '{secret_word}'.")
            break

        # Get player's guess
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"  ✅ '{guess}' is in the word!\n")
        else:
            wrong_letters.add(guess)
            wrong_count += 1
            print(f"  ❌ '{guess}' is NOT in the word.\n")


def main():
    """Main loop — lets the player replay without restarting the script."""
    while True:
        play()
        again = input("\n  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! Goodbye 👋\n")
            break


if __name__ == "__main__":
    main()