from infrastructure.data.repository.jogosRepositorys import JogoRepository
from rich.prompt import Prompt, Confirm
from view.jogo.jogo import Tela_Jogo
from domain.entity.jogo import Jogo
from rich import print


class Deletar_Jogo:
    def __init__(self):
        self.jogo_repository = JogoRepository()


    def execute(self):
        tela_jogo = Tela_Jogo()
        while True:
            nome_jogo = Prompt.ask("[yellow]Digite o nome do jogo que deseja deletar[/]")
            jogo = self.jogo_repository.buscar_jogo_nome(nome_jogo)
            if jogo:
                jogo_class = Jogo(
                        jogo_id=jogo["jogo_id"],
                        titulo=jogo["titulo"],
                        descricao=jogo["descricao"],
                        usuario_id=jogo["usuario_id"],
                        conquistas=jogo["conquistas"],
                        especificacoes_user=jogo["especificacoes_user"],
                        plataformas=jogo["plataformas"]
                    )
                tela_jogo.tela_jogo(jogo_class=jogo_class)
                confirm = Confirm.ask("[red]Tem certeza que deseja deletar este jogo?[/]")
                if confirm:
                    self.jogo_repository.deletar_jogo(jogo["jogo_id"])
                    print("[green]Jogo deletado com sucesso![/]")
                    break
            else:
                print("Jogo não encontrado. Verifique as letras Maíusculas e Minúsculas e tente novamente.")
            