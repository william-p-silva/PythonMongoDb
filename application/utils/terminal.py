

import os


class Terminal:
    def limpar_terminal(self):
        if os.name == "nt": os.system("cls")
        else: os.system("clear")