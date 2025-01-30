from utils.decorators import new_page
from language_en import *


class Menu:

    def __init__(self, title, actions):
        self.title = title
        self.actions = actions

    @new_page
    def display(self):
        print(self.title)
        for i, action in enumerate(self.actions):
            print(f"{action.message}")

    def get_choice(self):
        while True:
            choice = input(INPUT_PROMPT)
            if choice.isdigit():
                choice = int(choice)
                if 0 <= choice <= len(self.actions):
                    return choice
            print(INVALID_INPUT_PROMPT)

    def run(self, *args, **kwargs):
        while True:
            self.display()
            choice = self.get_choice()
            action = self.actions[choice - 1]
            result = action.execute(*args, **kwargs)
            if result == -1:
                return