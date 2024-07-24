from random import randint


class GuessingGame():
    def __init__(self):
        self.guesses = 7
        self.expected_value = randint(1, 50)
        self.guessed_number = None
        self.is_correct = False
        self.hint = None
        self.is_game_over = False

    def check(self, input_number):
        self.guessed_number = input_number

        if self.guesses > 1:
            if self.guessed_number == self.expected_value:
                self.is_correct = True
                self.is_game_over = True
                self.hint = f"You found the number {self.expected_value}"
            elif self.guessed_number > self.expected_value:
                self.hint = "Incorrect number, it is less than {}".format(self.guessed_number)
                self.guesses -= 1
            elif self.guessed_number < self.expected_value:
                self.hint = "Incorrect number, it is greater than {}".format(self.guessed_number)
                self.guesses -= 1
        else:
            self.hint = "Game over, you lost"
            self.is_game_over = True
