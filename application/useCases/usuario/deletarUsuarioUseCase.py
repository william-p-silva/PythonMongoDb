from rich import print
from rich.prompt import Confirm, Prompt

from infrastructure.data.repository.usuariosRepository import UsuarioRepository


class DeletarUsuarioUseCase:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def execute(self):
        email = Prompt.ask("Digite o email do usuário que deseja deletar")
        if email == "-1":
            print("[yellow]Operação cancelada.[/]")
            return
        if not email.strip() or "@" not in email:
            print("[red]Email inválido. Informe um email com '@'.[/]")
            return

        usuario = self.usuario_repository.buscar_usuario_por_email(email)
        if not usuario:
            print("[yellow]Nenhum usuário encontrado com esse email.[/]")
            return

        confirmar = Confirm.ask("Tem certeza que deseja deletar este usuário?")
        if not confirmar:
            print("[yellow]Operação cancelada.[/]")
            return

        nome_digitado = Prompt.ask("Digite exatamente o nome do usuário para confirmar a exclusão")
        if nome_digitado != usuario["nome"]:
            print("[red]Nome incorreto. Exclusão cancelada.[/]")
            return

        self.usuario_repository.deletar_usuario(email)
        print("[green]Usuário deletado com sucesso![/]")
