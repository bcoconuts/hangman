# hangman game


# ==========================
# CONFIG
# ==========================

import random

ALPHABET = {
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
}
SECRET_WORD_LIST = ["PYTHON", "TESTING"]
MAX_LIVES = 6
DEBUG = False

# ==========================
# GAME SETUP
# ==========================


def init_secret_word(word_list: list) -> str:
    secret_word = random.choice(word_list)
    return secret_word


def setup_game():
    game_over = False
    lives_remaining = MAX_LIVES
    guessed_letter_set = set()
    secret_word = init_secret_word(SECRET_WORD_LIST)
    secret_word_set = {char for char in secret_word}
    return game_over, lives_remaining, guessed_letter_set, secret_word, secret_word_set


# ==========================
# GAME LOGIC
# ==========================


def get_guessed_letter(guessed_letter_set: set) -> str:
    running = True
    while running:
        guessed_letter = input("\nGuess A Letter: ").strip().capitalize()
        if guessed_letter not in ALPHABET:
            print("\nInvalid Input. Try Again.")
        elif guessed_letter in guessed_letter_set:
            print("\nAlready Guessed. Try Again.")
        else:
            running = False

    return guessed_letter

def play_game_loop() -> tuple[int, str]:
    game_over, lives_remaining, guessed_letter_set, secret_word, secret_word_set = setup_game()
    while not game_over and lives_remaining > 0:
        guessed_letter = get_guessed_letter(guessed_letter_set)
        guessed_letter_set.add(guessed_letter)
        game_over = secret_word_set.issubset(guessed_letter_set)
        if guessed_letter not in secret_word_set:
            lives_remaining -= 1
        display_results(secret_word, guessed_letter_set, lives_remaining)
    
    return lives_remaining, secret_word


# ==========================
# DISPLAY
# ==========================

def display_results(secret_word: str, guessed_letter_set: set, lives_remaining: int) -> None:
    displayed_word = ""
    for char in secret_word:
        if char in guessed_letter_set:
            displayed_word += char
        else:
            displayed_word += "_"
    print(displayed_word)
    print(f"{lives_remaining} lives remaining.")


def display_greeting() -> None:
    print(f"Let's play Hangman! Try and guess my word. You have {MAX_LIVES} lives to guess correctly!\n")


def display_ending(lives_remaining: int, secret_word: str) -> None:
    if lives_remaining <= 0:
        print(f"\nToo Bad! You lost! My word was {secret_word}. Better luck next time.")
    elif lives_remaining == 1:
        print(f"\nClose Call! You managed to win with only {lives_remaining} life remaining!")
    else:
        print(f"\nCongratulations! You won with {lives_remaining} lives remaining!")


# ==========================
# MAIN LOOP
# ==========================


def main():
    display_greeting()
    lives_remaining, secret_word = play_game_loop()
    display_ending(lives_remaining, secret_word)


if __name__ == "__main__":
    main()
