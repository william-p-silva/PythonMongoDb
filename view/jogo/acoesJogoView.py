from rich import print
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt, Confirm

class Jogo_Tela:
    def tela_adicionar_jogo(self):
        conteudo = "[green]Aqui você vai adicionar um jogo a sua coleção. [/]"
        conteudo += "\n[blue]Para isso vou precisar de algumas informações. [/]"
        conteudo += "\n\t[white]Nome do Jogo \n"
        conteudo += "\n\tDescrição do Jogo \n"
        conteudo += "\n\tQuais Plataformas o Jogo está Disponível [yellow](Você terá de colocar uma por uma)[/yellow] \n"
        conteudo += "\n\tCaso Queira Você Podera Adicionar Suas Conquistas [yellow](opcional)[/yellow] \n"
        conteudo += "\n\tVocê Pode adicionar Tópicos Propríos [yellow](opcional)[/yellow][/]\n"
        conteudo += "\n[red]Ou Digite -1 Para Voltar[/]"
        painel = Panel(conteudo, title="Adicionar Jogo", style="green", width=90)
        print(painel)

    
    def tela_lista_jogos(self):
        conteudo = "[yellow]Sua Lista de Jogos. [/]"
        conteudo += "\n[blue]Precione Enter Para Ver Sua Lista[/]"
        conteudo += "\n[red]Ou Digite -1 Para Voltar[/]"
        painel = Panel(conteudo, title="Lista de Jogos", style="blue", width=90)
        print(painel)


    def tela_buscar_jogo(self):
        conteudo = "\n[blue]Qual o Nome do Jogo que Você Deseja Encontrar? "
        conteudo += "\n[red]Ou Digite -1 Para Voltar[/]"
        painel = Panel(conteudo, title="Buscador de Jogos", style="yellow", width=90)
        print(painel)


    def tela_alterar_jogo(self):
        conteudo = "Qual Jogo Você Gostaria de Alterar? "
        conteudo += "\n[red]Ou Digite -1 Para Voltar[/]"
        painel = Panel(conteudo, title="Alterar Jogo", style="yellow", width=90)
        print(painel)


    def tela_deletar_jogo(self):
        conteudo = "[red]Qual Jogo Você Gostaria de Deletar? "
        conteudo += "\nOu Digite -1 Para Voltar[/]"
        painel = Panel(conteudo, title="Deletar Jogo", style="red", width=90)
        print(painel)

