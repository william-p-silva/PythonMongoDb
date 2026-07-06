from rich import print
from rich.panel import Panel


class Usuario_Tela:
    def tela_menu_usuario(self):
        conteudo = "[green]Gerenciamento de Usuários[/]"
        conteudo += "\n[blue]1 - Cadastrar usuário[/]"
        conteudo += "\n[blue]2 - Buscar usuário por email[/]"
        conteudo += "\n[blue]3 - Deletar usuário[/]"
        conteudo += "\n[red]0 - Voltar[/]"
        painel = Panel(conteudo, title="Usuários", style="magenta", width=90)
        print(painel)

    def tela_cadastrar_usuario(self):
        conteudo = "[green]Cadastre um novo usuário com nome e email.[/]"
        conteudo += "\n[red]Digite -1 para voltar[/]"
        painel = Panel(conteudo, title="Cadastro de Usuário", style="green", width=90)
        print(painel)

    def tela_buscar_usuario(self):
        conteudo = "[blue]Digite o email do usuário que deseja localizar.[/]"
        conteudo += "\n[red]Digite -1 para voltar[/]"
        painel = Panel(conteudo, title="Buscar Usuário", style="yellow", width=90)
        print(painel)

    def tela_deletar_usuario(self):
        conteudo = "[red]Digite o email do usuário que deseja deletar.[/]"
        conteudo += "\n[red]Digite -1 para voltar[/]"
        painel = Panel(conteudo, title="Deletar Usuário", style="red", width=90)
        print(painel)
