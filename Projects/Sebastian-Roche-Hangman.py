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




        ))


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