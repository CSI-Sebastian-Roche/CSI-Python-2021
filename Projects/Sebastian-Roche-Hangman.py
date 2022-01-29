import random
word_list = ["San Juan", "Ponce", "Caguas", "Cabo Rojo", "Humacao", "Vieques", "Moca", "Mayagüez", "San Sebastian", "Cidra"]

def display_hangman(tries):
    word = random.choice(word_list)
    return word.upper()



    (( def play(word):
        word_completion = "_" * len(word)
        guessed = False
        guessed_letters = []
        guessed-words = []
        tries = 6
        print("Welcome to Hangman!")
        print("Theme: Pueblos de Puerto Rico")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
        while not guessed and tries > 0:
            guess = input("Guess a letter or word: ").upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You already tried", guess, "!")
                    elif guess not in word:
                        print(guess, "Isn't in the word")
                        tries - = 1
                        guessed_letters.append(guess)
                        else:
                            print("Good Job!", guess, "is in the word")
                            guessed_letters.append(guess)
                            wold_as_list = list(wordd_completion)
                            indices = [i for i, leter in enumerate(word) if letter == guess]
                            for index in indices: 
                                word_as_list[index] = guess
                                word_completion == "".join(word_as_list)
                                if "_" not in word_completion:
                                    guessed = True
                    elif len(guess) == len(word) and guess.isalpha():
                        if guess in guessed_letters:
                            print("You already tried", guess, "!")
                            elif guess != word:
                                print(guess, "Is not the word")
                                tries -= 1
                                guessed_word.append(guess)
                                else:
                                    guessed = True
                                    word_completion = word 
                                else:
                                    print("Invalid input")
                                    print(display_hangman(tries))
                                    print(word_completion)
                                    print("\n")

                                    if guessed:
                                        print"Good Job, you guessed the word!!! :)"
                                        else:
                                            print("Im sorry, but you ran out of tries. The word was" + word + "Maybe nesxt time!")





        ))

def display_hangman(tries):
    stages = [ """
                    --------
                    |   |
                    |   O
                    |  /|\\
                    |  / \\ 
                    |
                    --
                    """,
                    """
                    --------
                    |   |
                    |   O
                    |  /|\\
                    |  / 
                    |
                    --
                    """,
                    """
                    --------
                    |   |
                    |   O
                    |  /|\\
                    |  
                    |
                    --
                    """,
                    """
                    --------
                    |   |
                    |   O
                    |  /|
                    |  
                    |
                    --
                    """,
                    """
                    --------
                    |   |
                    |   O
                    |   |
                    |  
                    |
                    --
                    """,
                    """
                    --------
                    |   |
                    |   O
                    |  
                    |  
                    |
                    --
                    """,
                    """
                    --------
                    |   |
                    |   
                    |  
                    |  
                    |
                    --
                    """,


    ]
    return stages[tries]
    def main():
        word = get_word(word_list)
        play(word)
        while input("Again? (Y/N)" ). upper() == "Y":
            word = get_word(word_list)
            play(word)


            if _name_ == "__main__":
                main()


                