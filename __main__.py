
import uuid
from view.home import Home
from application.utils.escolhaUser import Escolhas
from application.utils.terminal import Terminal
from rich import print

home = Home()
escolhas = Escolhas()
terminal = Terminal()

def main():
    home.tela_escolhas()
    escolha_usuario = escolhas.capturar_escolha()
    if escolha_usuario == -1: 
        terminal.limpar_terminal()
        print("[black on red]Escolha inválida. [/]")
        input()
    else:
        terminal.limpar_terminal()
        print(f"[green]Você escolheu [yellow][{escolha_usuario}][/yellow] {escolhas.ListaEscolhas[escolha_usuario]}[/]")
        input()
    if escolha_usuario == 0:
        return True
    escolhas.redirecionar_escolha(escolha_usuario)



if __name__ == "__main__":
    home.tela_boas_vinda()
    while True:
        parar = main()
        if parar:
            break