"""Adding 6 turns to Wordle. Also defining functions to make code look better."""

__author__ = "730510654"


def contains_char(word: str, single_character: str) -> bool:
    """Searches for single character in the word."""
    assert len(single_character) == 1
    tracking_index = 0

    while tracking_index < len(word):
        if single_character == word[tracking_index]:
            return True
        tracking_index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Gives a green, yellow, or white box based on whether the letters match up or not."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    tracking_index = 0
    resulting_colors = ""

    while tracking_index < len(secret):
        if guess[tracking_index] == secret[tracking_index]:
            resulting_colors += GREEN_BOX
        elif contains_char(secret, guess[tracking_index]):
            resulting_colors += YELLOW_BOX
        else:
            resulting_colors += WHITE_BOX
        tracking_index += 1
    return resulting_colors


def input_guess(expected_length: int) -> str:
    """Prompts the user for a guess that matches the proper amount of letters asked."""
    guess: str = input(f"Input a {expected_length} character word: ")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret = "codes"
    current_turn = 1
    win = False

    while current_turn <= 6 and not win:
        print(f"=== Turn {current_turn}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            win = True
        else:
            current_turn += 1
    if win:
        print(f"You won in {current_turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()