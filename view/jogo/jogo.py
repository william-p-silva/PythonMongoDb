from domain.entity.jogo import Jogo
from rich import print
from rich.panel import Panel

class Tela_Jogo:

    def tela_jogo(self, jogo_class):
        conteudo = f"[green]Título do Jogo: {jogo_class.Titulo} [/ ]"
        conteudo += f"\nIdentificador (ID) do Jogo: {jogo_class.Jogo_Id}"
        conteudo += f"\nDescrição do Jogo: {jogo_class.Descricao}"
        conteudo += f"\nIdentificador (ID) do Usuário: {jogo_class.Usuario_Id}"

        if getattr(jogo_class, "Usuario_Email", None):
            conteudo += f"\n[blue]Email do usuário vinculado: {jogo_class.Usuario_Email}[/]"
        else:
            conteudo += "\n[yellow]Email do usuário vinculado: Nenhum[/]"

        conteudo += "\n[yellow]Plataformas[/]:"
        for p, plataforma in enumerate(jogo_class.Plataformas):
            conteudo += f"\n\tPlataforma {p+1}: {plataforma}"

        conteudo += "\n[yellow]Conquistas:[/]"
        for c, conquista in enumerate(jogo_class.Conquistas):
            conteudo += f"\n\tConquista {c+1}: {conquista['nome']} : {conquista['raridade']}"

        conteudo += "\n[yellow]Especificações:[/]"
        for e, especificacao in enumerate(jogo_class.Especificacoes_User):
            for chave, valores in especificacao.items():
                conteudo += f"\n\t{chave}: {valores}"
        painel = Panel(conteudo, title=f"{jogo_class.Titulo}", border_style="red", width=90)
        print(painel)