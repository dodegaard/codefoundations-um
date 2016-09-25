import random

def get_random_word():
    words = ["pizza","cheese","apples"]
    random_word = words[random.randint(0, len(words) - 1)]
    return random_word

def show_word(word):
    print(word)

def play_word_games():
    strikes = 0
    max_strikes = 3
    playing = True

    word = get_random_word()

    blanked_word = "_" * len(word)

    while playing:
        show_word(blanked_word)

        #letter = get_guess()

        strikes += 1

        if strikes >= max_strikes:
            playing = False
        
    if strikes >= max_strikes:
        print("Sorry. Game over.")
    else:
        print("Winner!")
    
print("Start the Game")
play_word_games()
print("End the Game")
