import random

class HangmanGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.film_to_guess = self.choose_film()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_attempts = 6

    def choose_film(self):
        films = ["titanic", "jurassic park", "the matrix", "forrest gump", "pulp fiction",
                 "braveheart", "the silence of the lambs", "schindlers list", "the lion king",
                 "saving private ryan", "a few good men", "fight club", "dances with wolves",
                 "the shawshank redemption", "home alone", "the fifth element", "the truman show",
                 "goodfellas", "the green mile", "my cousin vinny", "american history x", "the fugitive",
                 "fargo", "the sixth sense", "the big lebowski", "heat", "groundhog day", 
                 "edward scissorhands", "pretty woman",]
        return random.choice(films)

game = HangmanGame()

print(game.film_to_guess)
print(game.guessed_letters)
print(game.incorrect_guesses)
print(game.max_attempts)