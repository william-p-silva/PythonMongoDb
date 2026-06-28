from rich import print
from rich.panel import Panel
from rich.console import Console


class Home:
    console = Console()
    def tela_boas_vinda(self):
        conteudo = "[bold cyan]Boas-vindas ao Geek Vault! 🎮[/]\n\n"
        conteudo += "Este é o seu espaço personalizado para catalogar, consultar\n"
        conteudo += "e gerenciar os seus jogos favoritos.\n\n"
        conteudo += "[italic subtitle]Escolha uma das opções do menu abaixo para começar:[/]"
        painel = Panel(conteudo, 
                       title="[bold magenta] Geek Vault [/]",
                       subtitle="[yellow]v1.0.0[/]",
                       border_style="green",
                       expand=False)
        self.console.print(painel)


    def tela_escolhas(self):
        conteudo =  "[green][1][/] [blue]Adicionar novo jogo: \n"
        conteudo += "[green][2][/] Listar todos os jogos: \n"
        conteudo += "[green][3][/] Buscar um jogo especifico: \n"
        conteudo += "[green][4][/] Alterar algum jogo: \n"
        conteudo += "[green][5][/] Deletar um jogo: \n"
        conteudo += "[red][0][/] Sair da plataforma: [/blue]\n"
        painel = Panel(conteudo, 
                       title="[bold green]< Escolhas >[/]",
                       border_style="blue",
                       expand=False)
        self.console.print(painel)