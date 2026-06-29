from rich import print
from rich.prompt import Prompt
from application.useCases.jogo.cadastrarJogoUseCase import Cadastrar_Jogo_UseCase
from view.jogo.acoesJogoView import Jogo_Tela

tela_jogo = Jogo_Tela()

class Escolhas:
    def __init__(self):
        self.ListaEscolhas = [ "Sair da plataforma", "Adicionar novo jogo", "Listar todos os jogos", 
                              "Buscar um jogo especifico", "Alterar algum jogo", "Deletar um jogo" ]


    def capturar_escolha(self):
        escolha = Prompt.ask(
            "[bold yellow]Selecione a Ação[/]",
            choices=["1", "2", "3", "4", "5", "0"],
            default="1",
            )
        try:
            escolha_int = int(escolha)
            if 0 <= escolha_int <= 5:  return escolha_int
            else: return -1           
        except:
            return -1


    def redirecionar_escolha(self, escolha: int):
        #Chamar um view e depois na view chama o useCase
        match escolha:
            case 1:
                tela_jogo.tela_adicionar_jogo()
                cadastro = Cadastrar_Jogo_UseCase()
                cadastro.execute()
            case 2:
                tela_jogo.tela_lista_jogos()
                input()
            case 3:
                tela_jogo.tela_buscar_jogo()
                input()
            case 4:
                tela_jogo.tela_alterar_jogo()
                input()
            case 5:
                tela_jogo.tela_deletar_jogo()
                input()
