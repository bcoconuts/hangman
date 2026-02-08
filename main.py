# hangman game

DEBUG = True
secret_word = "PYTHON"

def get_guessed_letter(guessed_letter_set: set) -> set:
    running = True
    while running:
        guessed_letter = set(input("Guess A Letter: ").strip().capitalize())
        if guessed_letter_set.isdisjoint(guessed_letter):
            guessed_letter_set.update(guessed_letter)
            running = False
        else:
            print("Already Guessed. Try Again.")

    return guessed_letter_set

def display_secret_word(secret_word: str, guessed_letter_set: set) -> str:
    displayed_word = ""
    for char in secret_word:
        if char in guessed_letter_set:
            displayed_word += char
        else:
            displayed_word += "_"
    print(displayed_word)
    return displayed_word


def main():
    guessed_letter_set = set()
    running = True
    while running:
        guessed_letter_set = get_guessed_letter(guessed_letter_set)
        if DEBUG == True: print(guessed_letter_set)
        displayed_word = display_secret_word(secret_word, guessed_letter_set)
        if displayed_word == secret_word:
            running = False
    print("Game Over")

if __name__ == "__main__":
    main()
