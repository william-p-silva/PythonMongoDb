from rich import print
from rich.prompt import Prompt

from application.useCases.usuario.cadastrarUsuarioUseCase import CadastrarUsuarioUseCase
from application.useCases.usuario.buscarUsuarioPorEmailUseCase import BuscarUsuarioPorEmailUseCase
from application.useCases.usuario.deletarUsuarioUseCase import DeletarUsuarioUseCase
from view.usuario.usuario import Usuario_Tela


class EscolhaUsuario:
    def __init__(self):
        self.tela = Usuario_Tela()

    def capturar_escolha(self):
        escolha = Prompt.ask(
            "[bold yellow]Selecione a ação de usuário[/]",
            choices=["1", "2", "3", "0"],
            default="1",
        )
        try:
            return int(escolha)
        except ValueError:
            return -1

    def redirecionar_escolha(self, escolha: int):
        if escolha == 1:
            self.tela.tela_cadastrar_usuario()
            CadastrarUsuarioUseCase().execute()
        elif escolha == 2:
            self.tela.tela_buscar_usuario()
            BuscarUsuarioPorEmailUseCase().execute()
        elif escolha == 3:
            self.tela.tela_deletar_usuario()
            DeletarUsuarioUseCase().execute()
        elif escolha == 0:
            print("[yellow]Voltando ao menu principal...[/]")
