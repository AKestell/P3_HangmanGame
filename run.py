import ramdom

class HangmanGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.film_to_guess = self.choose_film()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_attempts = 6

    def choose_film(self):
        films = []