# ScrabbleWordFinder
Search for Words in the board game Scrabble

This is a simple Python script to assist (cheat) with the game Scrabble.
I made this because I am awful at the game.

Launch the script in the same directory as words.txt or change the path defined in the head of the script (self.words_path = "words.txt").

How to use
----------

When you run the script it will prompt you for information about your hand and the letters on the board. Enter the information and then a list of possible words will be generated.

Prompts:

Enter the letters in your hand >
  Enter the letters that appear in your hand with no spaces e.g. “ynop”

The next prompts will loop until you do not enter any more data. Just press enter to skip and end the loop.

Enter a board letter (Enter to skip) >
  Enter a letter of a word on the Scrabble board which can have a word attached to it e.g. “p”
  
Start range of letter position in word:
  This is the start range of the possible position the board letter would be in the word if that letter was used. This value starts at 1 and can end at any limit. This can also be a negative number for that end of the word. E.g. -1 would be the last letter of the word.
  
End range of letter position in word (Enter for the same as start):
  This is the end range of the possible position the board letter would be in the word if that letter was used. 


Running Example
---------------

Enter the letters in your hand > ntypho
Enter a board letter (Enter to skip) > y
Start range of letter possistion in word: 2
End range of letter possistion in word (Enter for the same as start):
Enter a board letter (Enter to skip) >

NY
OY
HYP
HYPO
PYOT
TYPO
PYTHON
TYPHON

