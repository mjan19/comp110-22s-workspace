"""Example of writing a function to search a list."""


def main() -> None:
    guess = input("What is the code word?")
    possible_answers: list[str] = ["pokemon", "wordle"]
    if contains(guess, possible_answers):
        print("We're letting you in the secret club.")
    else:
        print("Return back to Davis.")


def contains(needle: str, haystack: list[str]) -> bool:
    """Test if needle is found in haystack."""
    for item in haystack:
        if item == needle:
            return True
    return False


if __name__ == "__main__":  
    main()