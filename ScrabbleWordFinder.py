class WordFinder():
    def __init__(self):
        self.words_path = "words.txt"   # Path to words file - a file containing every word seperated by a new line
        self.words = []                 # A list of all words

        self.LoadWords()                # Load the words

    def LoadWords(self):                # Load all the words from self.words_path file into self.words
        print("Loading Words...")
        
        f = open(self.words_path, "r")

        while True:
            word = f.readline().replace("\n", "")

            if word == "":  # End of file
                break

            self.words.append(word)

        word_count = len(self.words)

        print(str(word_count) + " Words Loaded!")

    def WordSearch(self, hand, board):      # Search for words matching hand and board.
        # hand = list of letters in the word.
        # board = list of letters at a specific possistion in the word [letter, start_range, end_range] e.g. [['p', 0, 1], ['o', 1, 5]]

        # Make every letter lower case

        low_hand = []
        low_board = []
        all_letters = [] # All letters avalible

        for letter in hand:
            low_letter = letter.upper()
            
            low_hand.append(low_letter)
            all_letters.append(low_letter)

        for board_possistion in board:
            low_letter = board_possistion[0].upper()
            
            low_possistion = board_possistion
            low_possistion[0] = low_letter

            low_board.append(low_possistion)
            all_letters.append(low_letter)


        # Generate multiple letter lists - each containing all hand letters and one of the board letters

        letter_lists = []

        for board_possistion in low_board:
            letter_lists.append(low_hand + board_possistion[:1])

        if len(letter_lists) == 0:
            letter_lists = [low_hand]

        # Search 1 - Get all words which can be made from the letters in all_letters

        all_matching_words = []

        for letter_list in letter_lists:    # Find words for each of the letter lists
            for word in self.words:
                match = True            # If there is a match
                found = []              # A list of indexes of all_letters - This will be appended when a letter in word matches a letter in all_letters, the append value will be the index of all_letters. This is to match words with more than one of the same letter

                word_letters = self.ListString(word)

                for word_letter in word_letters:    # Check all word_letters are in all_letters. If not set match = False
                    letter_match = False

                    for search_letter in letter_list:   # Checks if word_letter is in all_letters without being used twice. if not set letter_match = False
                        if word_letter == search_letter:        # If the word_letter is in all_letters, check it has not already been checked
                            letter_index = all_letters.index(search_letter)

                            if letter_index in found:   # That letter is already used
                                continue

                            else:
                                found.append(letter_index)
                                letter_match = True

                                break

                    if not letter_match:
                        match = False

                if match:
                    all_matching_words.append(word)


        # Search 2 - Only includ words matching board conditions

        if len(low_board) > 0: # Only run this if there is any board letters
            matching_words = []

            for word in all_matching_words:
                match = False

                for board_possistion in low_board:
                    start = board_possistion[1]
                    stop = board_possistion[2]

                    if start < 0:
                        start = start + 1
                        start = len(word) + start

                    if stop < 0:
                        stop = stop + 1
                        stop = len(word) + stop
                    
                    for index in range(start, stop + 1):
                        if len(word) <= index:
                            continue
                        
                        if word[index] == board_possistion[0]:
                            match = True
                            break

                if match:
                    matching_words.append(word)

        else:
            matching_words = all_matching_words


        # Remove duplicated words

        words = []

        for word in matching_words:
            if not word in words:
                words.append(word)

        # Sort the words, shortest first

        words.sort(key = self.SortLength)

        return words

    def SortLength(self, word): # For use with sorting
        return len(word)
                

    def CLISearch(self):    # Use the CLI to Search for words
        hand = raw_input("Enter the letters in your hand >  ")  # Get hand letters
        hand = self.ListString(hand.strip())                    # Remove Spaces and seperate into a list

        index = 0
        board = []

        while True:     # Get board letters
            board_letter = raw_input("Enter a board letter (Enter to skip) > ")

            if board_letter == "":
                break

            try:
                start_range = input("Start range of letter possistion in word: ") - 1

            except:
                print("Error no number.")
                continue

            try:
                end_range = input("End range of letter possistion in word (Enter for the same as start): ") - 1

            except:
                end_range = start_range

            board.append([board_letter, start_range, end_range])

        print("Searching...")
        words = self.WordSearch(hand, board)

        if len(words) == 0:
            print("No matching Words found.")

        else:
            print("-------- Found Words --------\n" + "\n".join(words) + "\n-----------------------------")

    def ListString(self, string):   # Turn a string into a list
        string_list = []

        for char in string:
            string_list.append(char)

        return string_list
        

if __name__ == "__main__":
    WF = WordFinder()

    print("\nWelcome to Word Finder!\n\n\tMade By: Nick Wright\n\n")

    while True:
        WF.CLISearch()
