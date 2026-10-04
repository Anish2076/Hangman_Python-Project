import random
import os


# ============================================================
#                       HANGMAN GAME
# ============================================================

# ------------------------- CONFIG ---------------------------

WORDS = [
    "python",
    "computer",
    "developer",
    "programming",
    "software",
    "javascript",
    "database",
    "keyboard",
    "internet",
    "application"
]

MAX_ATTEMPTS = 6


# ---------------------- HANGMAN ART -------------------------

HANGMAN_STAGES = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


# ---------------------- CLEAR SCREEN ------------------------

def clear_screen():
    """Clear the terminal screen."""

    os.system("cls" if os.name == "nt" else "clear")


# ---------------------- GAME HEADER -------------------------

def display_header():
    """Display the game title."""

    print("=" * 55)
    print("                 HANGMAN GAME")
    print("=" * 55)
    print("       Guess the hidden word, one letter at a time!")
    print("=" * 55)


# ---------------------- SELECT WORD --------------------------

def select_word():

    print("\nChoose your first letter.")
    print("Your first letter will influence the random word!")

    while True:

        first_guess = input("Enter your first letter: ").lower().strip()

        # Validate input
        if len(first_guess) != 1:
            print("Please enter only ONE letter.")
            continue

        if not first_guess.isalpha():
            print("Please enter an alphabet letter.")
            continue

        # Find words containing the guessed letter
        matching_words = [
            word for word in WORDS
            if first_guess in word
        ]

        # If matching words are found
        if matching_words:

            secret_word = random.choice(matching_words)

            print("\nYour letter was:", first_guess)
            print("Matching words found:", len(matching_words))
            print("A random word has been selected!")

            return secret_word, first_guess

        # If no word contains the letter
        else:

            print("\nNo word in the list contains that letter.")
            print("Please choose another letter.")


# ---------------------- DISPLAY WORD -------------------------

def display_word(secret_word, guessed_letters):

    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


# ---------------------- DISPLAY GAME -------------------------

def display_game(
    secret_word,
    guessed_letters,
    wrong_guesses
):

    clear_screen()

    display_header()

    # Hangman drawing
    print(HANGMAN_STAGES[len(wrong_guesses)])

    # Current word
    print(
        "Word:",
        display_word(secret_word, guessed_letters)
    )

    # Guessed letters
    all_guesses = guessed_letters | wrong_guesses

    if all_guesses:
        print(
            "Guessed letters:",
            " ".join(sorted(all_guesses))
        )
    else:
        print("Guessed letters: None")

    print(
        "Wrong guesses :",
        len(wrong_guesses)
    )

    print(
        "Attempts left :",
        MAX_ATTEMPTS - len(wrong_guesses)
    )

    print("-" * 55)


# ---------------------- GET GUESS ----------------------------

def get_guess(
    guessed_letters,
    wrong_guesses
):

    while True:

        guess = input("Enter a letter: ").lower().strip()

        # Check length
        if len(guess) != 1:
            print("Please enter only ONE letter.")
            continue

        # Check alphabet
        if not guess.isalpha():
            print("Please enter an alphabet letter.")
            continue

        # Check repeated guess
        if (
            guess in guessed_letters
            or guess in wrong_guesses
        ):
            print("You already guessed that letter.")
            continue

        return guess


# ---------------------- CHECK WIN ----------------------------

def check_win(
    secret_word,
    guessed_letters
):

    return all(
        letter in guessed_letters
        for letter in secret_word
    )


# ---------------------- SCORE -------------------------------

def calculate_score(
    secret_word,
    wrong_guesses
):

    score = (
        len(secret_word) * 10
        - len(wrong_guesses) * 5
    )

    return max(score, 0)


# ---------------------- PLAY GAME ----------------------------

def play_game():

    clear_screen()

    display_header()

    # Select word based on first letter
    secret_word, first_guess = select_word()

    guessed_letters = set()
    wrong_guesses = set()

    # Automatically count first letter as a guess
    if first_guess in secret_word:
        guessed_letters.add(first_guess)
    else:
        wrong_guesses.add(first_guess)

    input("\nPress ENTER to start the game...")

    # Main game loop
    while len(wrong_guesses) < MAX_ATTEMPTS:

        display_game(
            secret_word,
            guessed_letters,
            wrong_guesses
        )

        # Check if player has won
        if check_win(
            secret_word,
            guessed_letters
        ):

            score = calculate_score(
                secret_word,
                wrong_guesses
            )

            print("\n" + "=" * 55)
            print("                 YOU WON!")
            print("=" * 55)

            print(
                f"Congratulations! The word was: "
                f"{secret_word}"
            )

            print(f"Your score: {score}")

            print("=" * 55)

            return

        # Get next guess
        guess = get_guess(
            guessed_letters,
            wrong_guesses
        )

        # Check guess
        if guess in secret_word:

            guessed_letters.add(guess)

            print("\nCorrect guess!")

        else:

            wrong_guesses.add(guess)

            print("\nWrong guess!")

        input("\nPress ENTER to continue...")

    # ---------------- GAME OVER ----------------

    display_game(
        secret_word,
        guessed_letters,
        wrong_guesses
    )

    print("\n" + "=" * 55)
    print("                 GAME OVER")
    print("=" * 55)

    print("You ran out of attempts.")
    print(f"The correct word was: {secret_word}")

    print("=" * 55)


# ---------------------- MAIN PROGRAM -------------------------

def main():

    while True:

        play_game()

        print()

        play_again = input(
            "Would you like to play again? (y/n): "
        ).lower().strip()

        if play_again != "y":

            print("\n" + "=" * 55)
            print("       Thanks for playing Hangman!")
            print("              Keep coding!")
            print("=" * 55)

            break


# ---------------------- START PROGRAM ------------------------

if __name__ == "__main__":
    main()