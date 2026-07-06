from time import sleep
from infrastructure.data.repository.jogosRepositorys import JogoRepository
from infrastructure.data.repository.usuariosRepository import UsuarioRepository
from rich import print
from rich.prompt import Confirm, Prompt, IntPrompt

from domain.entity.jogo import Jogo

class Cadastrar_Jogo_UseCase:
    def __init__(self):
        self.jogo_repository = JogoRepository()
        self.usuario_repository = UsuarioRepository()

    def execute(self):

        while True:
            opcao = 0
            list_especificacoes = []
            list_plataformas = []
            list_conquista = []

            nome = Prompt.ask("Digite o Nome do Jogo")
            if not nome.strip(): 
                print("[red]Nome inválido. [/]")
                continue
            if nome == "-1": 
                opcao = -1
                break

            descricao = Prompt.ask("Digite a Descrição do Jogo")
            if not descricao.strip(): 
                print("Descrição inválida. ")
                continue

            num_plataformas = IntPrompt.ask("Em Quantas Plataformas o Jogo está Disponível")
            c = 0
            while c < num_plataformas:
                plataforma = Prompt.ask(f"Digite o Nome ou Sigla da {c+1}° Plataforma")
                if not plataforma.strip(): 
                    print("[red]Plataforma inválida. ")
                    continue
                c += 1
                list_plataformas.append(plataforma)

            confirma_conquista = Confirm.ask("Você Deseja Adicionar suas Conquistas")
            if confirma_conquista:
                num_conquistas = IntPrompt.ask("Quantas conquistas você gostaria de adicionar")
                c = 0
                while c < num_conquistas:
                    nome_conquista = Prompt.ask(f"[yellow]Qual o Nome da {c +1}° Conquista [/]")
                    if not nome_conquista.strip():
                        print("[red]O nome da conquista é inválido. [/]")
                        continue
                    raridade_conquista = Prompt.ask(f"[green]Qual a Raridade da {c +1}° Conquista[/]")
                    if not raridade_conquista.strip():
                        print("[red]Raridade inválida. ")
                        continue

                    dict_conquista = {"nome": nome_conquista, "raridade": raridade_conquista}
                    list_conquista.append(dict_conquista)
                    c += 1
            
            confirma_especificacoes = Confirm.ask("Você desejá adicionar especificações proprias? (Exemplo horas de Jogo)")
            if confirma_especificacoes:
                num_especificacoes = IntPrompt.ask("Quantas especifícações você deseja adicionar")
                c = 0
                print("\nVocê tera de colocar o titulo e o valor da sua especificação")
                print("Exemplo: \n\tHoras Jogadas: 555")
                while c < num_especificacoes:
                    titulo_especificacao = Prompt.ask(f"Qual o Título da {c + 1}° especificação")
                    if not titulo_especificacao.strip():
                        print("Título inválido. ")
                        continue
                    valor_especificacao = Prompt.ask(f"Digite o valor da {c + 1}° especificação")
                    if not valor_especificacao.strip():
                        print("Valor inválido. ")
                        continue
                    dict_especificacao = {titulo_especificacao: valor_especificacao}
                    list_especificacoes.append(dict_especificacao)
                    c += 1
            try:
                usuario_email = None
                userID = None
                alocar_usuario = Confirm.ask("Deseja alocar este registro a um usuário cadastrado? (y/n)")
                while alocar_usuario:
                    email = Prompt.ask("Digite o email do usuário")
                    if email.strip() == "-1":
                        print("[yellow]Você optou por não vincular um usuário a este jogo.[/]")
                        break
                    if not email.strip() or "@" not in email:
                        print("[red]Email inválido. Tente novamente ou digite -1 para cancelar a vinculação.[/]")
                        continue

                    usuario = self.usuario_repository.buscar_usuario_por_email(email)
                    if usuario:
                        usuario_email = usuario["email"]
                        userID = usuario["id"]
                        print("[green]Usuário encontrado. Registro vinculado ao email informado.[/]")
                        break

                    print("[yellow]Nenhum usuário encontrado com esse email. Tente novamente ou digite -1 para cancelar a vinculação.[/]")

                jogo = Jogo(titulo=nome, descricao=descricao, usuario_id=userID, plataformas=list_plataformas,
                            conquistas=list_conquista, especificacoes_user=list_especificacoes,
                            usuario_email=usuario_email)
                jogo_preparado = jogo.to_json()
                self.jogo_repository.cadastro_jogos(jogo_preparado)
                break
            except Exception:
                print("[red]Ocorreu um erro inesperado. Tente novamente[/]")

        if opcao != -1:
            print("[green]Jogo cadastrado[/]")
            print("Precione enter para sair")
            input()
        else:
            print("[yellow]Voltando [/]", end='')
            for c in range(5):
                sleep(0.5)
                print("[yellow] . [/]", end='')
        