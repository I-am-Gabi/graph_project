import random
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E, Frame

import sys

sys.path.append('../')
from engine.Action import Action
from engine.coordinator import run


class GuessingGame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Network Analyzer")
        self.master.minsize(200, 200)

        self.secret_number = random.randint(1, 100)
        self.guess = None
        self.num_guesses = 0

        explanation = "\nO objetivo desta interface é facilitar a analise da infra-estrutura da rede.\n\n" \
                      "[QUIT] - Botão para fechar a interface\n" \
                      "[SPM] - Rodar o algoritmo de menor caminho com multiplos critérios\n" \
                      "[Bottleneck] - Rodar o algoritmo para analisar gargalos na rede"
        self.message = ""
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)

        self.explanation = Label(master, text=explanation)
        self.explanation.grid(row=0, column=0, columnspan=2, sticky=W + E)

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.quit_button = Button(master, text="Quit", command=self.quit)
        self.spm_button = Button(master, text="SPM", command=self.run_spm)
        self.analyzer_bottleneck_button = Button(master, text="Bottleneck", command=self.run_analyzer_bottleneck)

        self.label.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.entry.grid(row=2, column=0, columnspan=2, sticky=W+E)
        self.quit_button.grid(row=3, column=0)
        self.spm_button.grid(row=3, column=1)
        self.analyzer_bottleneck_button.grid(row=3, column=2)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.guess = None
            return True

        try:
            guess = int(new_text)
            if 1 <= guess <= 100:
                self.guess = guess
                return True
            else:
                return False
        except ValueError:
            return False

    def run_spm(self):
        self.message = run(action=Action.SPM, start=0, target=3)
        self.label_text.set(self.message)

    def run_analyzer_bottleneck(self):
        pass

"""
    def guess_number(self):
        self.num_guesses += 1

        if self.guess is None:
            self.message = "Guess a number from 1 to 100"

        elif self.guess == self.secret_number:
            suffix = '' if self.num_guesses == 1 else 'es'
            self.message = "Congratulations! You guessed the number after %d guess%s." % (self.num_guesses, suffix)
            self.guess_button.configure(state=DISABLED)
            self.reset_button.configure(state=NORMAL)

        elif self.guess < self.secret_number:
            self.message = "Too low! Guess again!"
        else:
            self.message = "Too high! Guess again!"

        self.label_text.set(self.message)

    def reset(self):
        self.entry.delete(0, END)
        self.secret_number = random.randint(1, 100)
        self.guess = 0
        self.num_guesses = 0

        self.message = "Guess a number from 1 to 100"
        self.label_text.set(self.message)

        self.guess_button.configure(state=NORMAL)
        self.reset_button.configure(state=DISABLED)
"""


root = Tk()
my_gui = GuessingGame(root)
root.mainloop()