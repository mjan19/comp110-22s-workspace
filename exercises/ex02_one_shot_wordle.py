"""Adding loops into Wordle exercise."""

__author__ = "730510654"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret_word: str = "python"
number_of_letters = len(secret_word)
tracking_index = 0 
resulting_colors = ""
letters_guess: str = input(f"What is your {number_of_letters}-letter guess? ")
while len(letters_guess) != number_of_letters:
    letters_guess: str = input(f"That was not {number_of_letters} letters! Try again: ")
while tracking_index < len(letters_guess):
    if letters_guess[tracking_index] == secret_word[tracking_index]:
        resulting_colors += GREEN_BOX
    else:
        exist_anywhere_else: bool = False
        alternate_indices = 0
        while not exist_anywhere_else and alternate_indices < number_of_letters:
            if letters_guess[tracking_index] == secret_word[alternate_indices]:
                exist_anywhere_else: bool = True
            else:
                alternate_indices += 1
        if exist_anywhere_else:
            resulting_colors += YELLOW_BOX
        else:
            resulting_colors += WHITE_BOX
    tracking_index += 1
print(resulting_colors)
if letters_guess == secret_word:
    print("Woo! You got it!")
    exit()
else:
    print("Not quite. Play again soon!")
    exit()