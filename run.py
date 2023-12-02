import random


class HangmanGame:
    def __init__(self):
        """
        Initialise the HangmanGame class.
        """
        self.reset()

    def reset(self):
        """
        Resets the game state.
        """
        self.film_to_guess = self.choose_film()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_attempts = 6

    def choose_film(self):
        """
        Choose a random 90s film from the list for the user to guess.
        """
        films = ["titanic", "clueless", "matrix", "fargo", "jumanji",
                 "braveheart", "trainspotting", "ghostbusters", "aladdin",
                 "goodfellas", "fargo", "heat", "armageddon", "volcano",
                 "unforgiven", "ghost", "tombstone", "philadelphia",
                 "misery", "clerks", "casino", "magnolia", "backdraft",
                 "hook", "beethoven", "cliffhanger", "coneheads", "assassins",
                 "goldeneye", "eraser", "godzilla", "blade", "dogma", ]
        return random.choice(films)

    def display_film(self):
        """
        Displays what letters of the film have been guessed so far.
        """
        display = ""
        for letter in self.film_to_guess:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display

    def hangman_graphic(self):
        """
        Display of the hangman graphic based on user guesses so far.
        """
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
            print("|     /|\\    ")
            print("|             ")
            print("|             ")
        elif self.incorrect_guesses == 5:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\\    ")
            print("|     /       ")
            print("|             ")
        else:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\\    ")
            print("|     / \\    ")
            print("|             ")
            print("The noose tightens around your neck, and you feel the")
            print("sudden urge to urinate.")
            print("GAME OVER!")
            self.reset()

    def play(self):
        """
        Gameplay code allowing users to input letters to guess the film.
        """
        print("Welcome to 90s Film Hangman!")

        while self.incorrect_guesses < self.max_attempts:
            current_display = self.display_film()
            print(f"\nFilm: {current_display}")
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
                print(f"Wrong guess! You have \
                {self.max_attempts - self.incorrect_guesses} attempts left.")
            else:
                print("Corret guess!")

            if all(letter in self.guessed_letters \
                for letter in self.film_to_guess):
                print(f"\nCongrats! You guessed the film {self.film_to_guess}")
                self.reset()
                break

        if self.incorrect_guesses == self.max_attempts:
            self.hangman_graphic()
            print(f"\nSorry, out of tries. The film was {self.film_to_guess}")


"""
Initiates gameplay
"""
game = HangmanGame()
game.play()
