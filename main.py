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

def init_game_over() -> bool:
    return False


def init_lives_consumed() -> int:
    return 0


def init_guessed_letter_set() -> set:
    guessed_letter_set = set()
    return guessed_letter_set


def init_secret_word(word_list: list) -> str:
    secret_word = random.choice(word_list)
    return secret_word


def init_secret_word_set(secret_word: str) -> set:
    secret_word_set = {char for char in secret_word}
    return secret_word_set


def setup_game():
    game_over = init_game_over()
    lives_consumed = init_lives_consumed()
    guessed_letter_set = init_guessed_letter_set()
    secret_word = init_secret_word(SECRET_WORD_LIST)
    secret_word_set = init_secret_word_set(secret_word)
    return game_over, lives_consumed, secret_word, secret_word_set, guessed_letter_set


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


def update_guessed_letter_set(guessed_letter_set: set, guessed_letter: str) -> None:
    guessed_letter_set.add(guessed_letter)


def game_over_check(secret_word_set: set, guessed_letter_set: set) -> bool:
    if DEBUG:
        print(secret_word_set.issubset(guessed_letter_set))
    return secret_word_set.issubset(guessed_letter_set)

def check_life_loss(guessed_letter: str, secret_word_set: set) -> bool:
    if guessed_letter in secret_word_set:
        return False
    else:
        return True

def perform_game_logic(secret_word_set: set, guessed_letter_set: set) -> tuple[bool, bool]:
    guessed_letter = get_guessed_letter(guessed_letter_set)
    update_guessed_letter_set(guessed_letter_set, guessed_letter)
    if DEBUG:
        print(guessed_letter_set)
    game_over = game_over_check(secret_word_set, guessed_letter_set)
    life_loss = check_life_loss(guessed_letter, secret_word_set)
    return game_over, life_loss


# ==========================
# DISPLAY
# ==========================


def display_secret_word(secret_word: str, guessed_letter_set: set) -> None:
    displayed_word = ""
    for char in secret_word:
        if char in guessed_letter_set:
            displayed_word += char
        else:
            displayed_word += "_"
    print(displayed_word)


def display_lives_remaining(lives_consumed: int) -> None:
    print(f"{MAX_LIVES - lives_consumed} lives remaining.")


def display_results(secret_word: str, guessed_letter_set: set, lives_consumed: int) -> None:
    display_secret_word(secret_word, guessed_letter_set)
    display_lives_remaining(lives_consumed)


def display_greeting() -> None:
    print(f"Let's play Hangman! Try and guess my word. You have {MAX_LIVES} lives to guess correctly!\n")


def display_ending(lives_consumed: int, secret_word: str) -> None:
    lives_remaining = MAX_LIVES - lives_consumed
    if lives_consumed >= MAX_LIVES:
        print(f"\nToo Bad! You lost! My word was {secret_word}. Better luck next time.")
    elif lives_remaining == 1:
        print(f"\nCongratulations! You managed to win with {lives_remaining} life remaining!")
    else:
        print(f"\nCongratulations! You managed to win with {lives_remaining} lives remaining!")


# ==========================
# MAIN LOOP
# ==========================


def main():
    display_greeting()
    game_over, lives_consumed, secret_word, secret_word_set, guessed_letter_set = setup_game()
    while not game_over and lives_consumed < MAX_LIVES:
        game_over, life_loss = perform_game_logic(secret_word_set, guessed_letter_set)
        if life_loss:
            lives_consumed += 1
        display_results(secret_word, guessed_letter_set, lives_consumed)
    display_ending(lives_consumed, secret_word)


if __name__ == "__main__":
    main()
