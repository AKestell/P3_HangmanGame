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

    def display_film(self):
        display = ""
        for letter in self.film_to_guess:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display

    def hangman_graphic(self):
        if self.incorrect_guesses == 0:
            print("________      ")
            print("|      |      ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif self.incorrect_guesses == 1:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif self.incorrect_guesses == 2:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /       ")
            print("|             ")
            print("|             ")
        elif self.incorrect_guesses == 3:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|      ")
            print("|             ")
            print("|             ")
        elif self.incorrect_guesses == 4:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|             ")
            print("|             ")
        elif self.incorrect_guesses == 5:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     /       ")
            print("|             ")
        else:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     / \     ")
            print("|             ")
            print("The noose tightens around your neck, and you feel the")
            print("sudden urge to urinate.")
            print("GAME OVER!")
            self.reset()


    def play(self):
        print("Welcome to 90s Film Hangman!")

        while self.incorrect_guesses < self.max_attempts:
            current_display = self.display_film()
            print(f"\Film: {current_display}")
            self.hangman_graphic()

            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a valid letter.")
                continue

            if guess in self.guessed_letters:
                print("You've already guessed that letter. Please try again")
                continue

            self.guessed_letters.append(guess)

            if guess not in self.film_to_guess:
                self.incorrect_guesses += 1
                print(f"Wrong guess! You have {self.max_attempts - self.incorrect_guesses} attempts left.")
            else:
                print("Corret guess!")

            if set(self.guessed_letters) == set(self.film_to_guess):
                print(f"\nCongratulations! You guessed the film: {self.film_to_guess}")
                self.reset()

        if self.incorrect_guesses == self.max_attempts:
            print(f"\nSorry, you're out of attempts. The film was: {self.film_to_guess}")

game = HangmanGame()

game.play()



