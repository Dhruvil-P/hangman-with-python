import random

import hangmanWordList
import hangman_stages

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)
# word list
wordList = hangmanWordList.word_list
wordListLen = len(wordList)
display = []  # blank list to hold the _

#  Guessing any random word from the list
randomIndex = random.randint(0, wordListLen - 1)
chosenWord = wordList[randomIndex]
chosenWordLen = len(chosenWord)


# for inserting _ till the word's length
for j in range(chosenWordLen):
    display.append('_')


endGame = False
lives = 6
while endGame == False:

    # User input for the letter
    guess = input("Enter a letter -->").lower()

    if guess in display:
        print(f"You have already guessed {guess}")
    #  Check guessed letter
    for pos in range(chosenWordLen):
        letter = chosenWord[pos]
        if letter == guess:
            display[pos] = letter

    # if user gives wrong answer
    if guess not in chosenWord:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life ")
        if lives == 0:
            endGame = True
            print('''
__  ______  __  __    __   ____  _____ ______
\ \/ / __ \/ / / /   / /  / __ \/ ___// ____/
 \  / / / / / / /   / /  / / / /\__ \/ __/   
 / / /_/ / /_/ /   / /__/ /_/ /___/ / /___   
/_/\____/\____/   /_____|____//____/_____/   
                                             
''')

    # display of the words
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print('''
__  ______  __  __    _       _______   __
\ \/ / __ \/ / / /   | |     / /  _/ | / /
 \  / / / / / / /    | | /| / // //  |/ / 
 / / /_/ / /_/ /     | |/ |/ // // /|  /  
/_/\____/\____/      |__/|__/___/_/ |_/   
                                                                                                              
 '''
              )

    # for the ASCII characters of hangman
    print(hangman_stages.stages[lives])
