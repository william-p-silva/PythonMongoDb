
from domain.entity.jogo import Jogo
from infrastructure.data.repository.jogosRepositorys import JogoRepository
from rich.prompt import Prompt
from rich import print 
from rich.panel import Panel

class BuscarJogoUseCase:
	def __init__(self):
		self.jogo_repository = JogoRepository()
	
	
	def buscar_jogo_por_nome(self):
		while True:
			nome_jogo = Prompt.ask("Digite o nome do jogo que deseja buscar: ")
			if not nome_jogo.strip():
				print("Nome inválido. Por favor, digite um nome válido.")
				continue
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
				conteudo = f"[green]Título do Jogo: {jogo_class.Titulo} [/]"
				conteudo += f"\nIdentificador (ID) do Jogo: {jogo_class.Jogo_Id}"
				conteudo += f"\nDescrição do Jogo: {jogo_class.Descricao}"
				conteudo += f"\nIdentificador (ID) do Usuário: {jogo_class.Usuario_Id}"

				conteudo += "\n[yellow]Plataformas[/]:"
				for p, plataforma in enumerate(jogo_class.Plataformas):
					conteudo += f"\n\tPlataforma {p+1}: {plataforma}"

				conteudo += "\n[yellow]Conquistas:[/]"
				for c, conquista in enumerate(jogo_class.Conquistas):
					conteudo += f"\n\tConquista {c+1}: {conquista["nome"]} : {conquista["raridade"]}"
    
				conteudo += "\n[yellow]Especificações:[/]"
				for e, especificacao in enumerate(jogo_class.Especificacoes_User):
					for chave, valores in especificacao.items():
						conteudo += f"\n\t{chave}: {valores}"
				painel = Panel(conteudo, title=f"{jogo_class.Titulo}", border_style="red", width=90)
				print(painel)
			else:
				print("Jogo não encontrado.")