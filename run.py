from tkinter import Tk, Label, Entry, Button
from guess import GuessingGame


class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("Number Guessing Game")
        self.window.geometry("500x500")
        self.window.minsize(800, 600)
        self.window.maxsize(800, 600)
        self.window.config(padx=50, pady=50)

        self.game = None

        self.hint = Label(self.window, text="To start Game push start button", font=("Arial", 16, "bold"))
        self.hint.pack()

        self.input_number = Entry(self.window, font=("Arial", 16, "bold"))
        self.input_number.config(state="readonly")
        self.input_number.pack()

        self.start_button = Button(self.window, text="Start", font=("Arial", 16, "bold"),
                                   command=self.start_button_command)
        self.start_button.pack()

        self.check_button = Button(self.window, text="Check", font=("Arial", 16, "bold"),
                                   command=self.check_button_command)
        self.check_button.config(state="disabled")
        self.check_button.pack()

        self.restart_button = Button(self.window, text="Restart", font=("Arial", 16, "bold"),
                                     command=self.restart_button_command)
        self.restart_button.config(state="disabled")
        self.restart_button.pack()

        self.window.mainloop()

    def start_button_command(self):
        self.game = GuessingGame()
        self.start_button.config(state="disabled")
        self.input_number.config(state="normal")
        self.restart_button.config(state="normal")
        self.check_button.config(state="normal")
        self.hint.config(text="Game is started. Guess numbers between 1 and 50")

    def restart_button_command(self):
        self.game = GuessingGame()
        self.hint.config(text="Game is restarted. Guess numbers between 1 and 50")

    def check_button_command(self):
        if self.input_number.get() and self.input_number.get().isnumeric():
            guessed_number = int(self.input_number.get())
            self.game.check(guessed_number)
            if self.game.is_game_over:
                self.start_button.config(state="normal")
                self.input_number.config(state="disabled")
                self.restart_button.config(state="disabled")
                self.check_button.config(state="disabled")
                self.hint.config(text=f"{self.game.hint}")
            else:
                self.hint.config(text=f"{self.game.hint}\nlive is {self.game.guesses}")
        else:
            self.hint.config(text="Wrong input")


App()
