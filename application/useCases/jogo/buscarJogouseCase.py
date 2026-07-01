
from domain.entity.jogo import Jogo
from infrastructure.data.repository.jogosRepositorys import JogoRepository
from rich.prompt import Prompt
from rich import print 
from rich.panel import Panel
from view.jogo.jogo import Tela_Jogo

class BuscarJogoUseCase:
	def __init__(self):
		self.jogo_repository = JogoRepository()
	
	
	def buscar_jogo_por_nome(self):
		while True:
			nome_jogo = Prompt.ask("Digite o nome do jogo que deseja buscar")
			if not nome_jogo.strip():
				print("Nome inválido. Por favor, digite um nome válido.")
				continue
			if nome_jogo == "-1":
				break
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
				tela_jogo = Tela_Jogo()
				tela_jogo.tela_jogo(jogo_class)
			else:
				print("Jogo não encontrado. Verifique as letras Maíusculas e Minúsculas e tente novamente.")