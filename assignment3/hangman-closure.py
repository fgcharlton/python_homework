# Task 4: Closure Practice
def make_hangman(secret_word): 
    secret_letters = list(secret_word)
    guesses = [] 
    def hangman_closure(letter): 
        correct_guesses = ""
        guesses.append(letter)
        for letters in secret_letters:
           if letters in guesses:
              correct_guesses += letters
           elif letters not in guesses:
              correct_guesses += "_"
        print(correct_guesses)
        if correct_guesses == secret_word:
            return True
        else:
            return False 
    return hangman_closure 

user_secret_word = input("What is your secret word? ")

game = make_hangman(user_secret_word)

finished = False 

while not finished:
    user_guess = input("What is your guess?")
    finished = game(user_guess)