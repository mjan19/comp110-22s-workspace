"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730510654"

number_of_matches = 0
five_character_word: str = input("Enter a 5-character word:")
if len(five_character_word) == 5:
    single_character: str = input("Enter a single character:")
    if len(single_character) == 1:
        print("Searching for " + single_character + " in " + five_character_word)
        if single_character == five_character_word[0]:
            print(single_character + " found at index 0")
            number_of_matches = number_of_matches + 1
        if single_character == five_character_word[1]:
            print(single_character + " found at index 1")
            number_of_matches = number_of_matches + 1
        if single_character == five_character_word[2]:
            print(single_character + " found at index 2")
            number_of_matches = number_of_matches + 1
        if single_character == five_character_word[3]:
            print(single_character + " found at index 3")
            number_of_matches = number_of_matches + 1
        if single_character == five_character_word[4]:
            print(single_character + " found at index 4")
            number_of_matches = number_of_matches + 1
        if number_of_matches == 0:
            print("No instances of " + single_character + " found in " + five_character_word)
        else: 
            if number_of_matches == 1:
                print("1 instance of " + single_character + " found in " + five_character_word)
            else:
                if number_of_matches > 1:
                    print(str(number_of_matches) + " instances of " + single_character + " found in " + five_character_word)
    else: 
        print("Error: Character must be a single character.")
        exit()
else:
    print("Error: Word must contain 5 characters")
    exit()