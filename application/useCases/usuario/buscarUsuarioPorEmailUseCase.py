from rich import print
from rich.prompt import Prompt

from infrastructure.data.repository.usuariosRepository import UsuarioRepository


class BuscarUsuarioPorEmailUseCase:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def execute(self):
        email = Prompt.ask("Digite o email do usuário que deseja buscar")
        if not email.strip() or "@" not in email:
            print("[red]Email inválido. Informe um email com '@'.[/]")
            return

        usuario = self.usuario_repository.buscar_usuario_por_email(email)
        if usuario:
            print(f"[green]Usuário encontrado:[/] {usuario['nome']} - {usuario['email']}")
        else:
            print("[yellow]Nenhum usuário encontrado com esse email.[/]")
