
import time
from view.home import Home
from application.utils.escolhaUser import Escolhas
from application.utils.terminal import Terminal
from rich import print


home = Home()
escolhas = Escolhas()
terminal = Terminal()

def main():
    global control
    if control == 0:
        home.tela_boas_vinda()
        control = 2
    else: 
        terminal.limpar_terminal()

    home.tela_escolhas()
    escolha_usuario = escolhas.capturar_escolha()
    if escolha_usuario == -1: 
        terminal.limpar_terminal()
        print("[black on red]Escolha inválida. [/]")
        return
    else:
        terminal.limpar_terminal()
        print(f"\n[green]Você escolheu [yellow][{escolha_usuario}][/yellow] {escolhas.ListaEscolhas[escolha_usuario]}[/]")
    if escolha_usuario == 0:
        home.sair()
        return True

    print()
    escolhas.redirecionar_escolha(escolha_usuario)


control = 0
if __name__ == "__main__":
    while True:
        parar = main()
        if parar:
            break