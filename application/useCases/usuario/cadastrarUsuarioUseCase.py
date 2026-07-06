from rich import print
from rich.prompt import Prompt

from domain.entity.usuario import Usuario
from infrastructure.data.repository.usuariosRepository import UsuarioRepository


class CadastrarUsuarioUseCase:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def execute(self):
        while True:
            nome = Prompt.ask("Digite o nome do usuário")
            if not nome.strip():
                print("[red]Nome inválido.[/]")
                continue
            if nome == "-1":
                print("[yellow]Voltando...[/]")
                return

            email = Prompt.ask("Digite o email do usuário")
            if not email.strip() or "@" not in email:
                print("[red]Email inválido. Informe um email com '@'.[/]")
                continue

            try:
                usuario = Usuario(nome=nome, email=email)
                self.usuario_repository.cadastro_usuario(usuario.to_json())
                print("[green]Usuário cadastrado com sucesso![/]")
                break
            except ValueError as error:
                print(f"[red]{error}[/]")
