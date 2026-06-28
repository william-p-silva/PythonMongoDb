from rich import print

class Escolhas:
    def __init__(self):
        self.ListaEscolhas = [ "Sair da plataforma", "Adicionar novo jogo", "Listar todos os jogos", 
                              "Buscar um jogo especifico", "Alterar algum jogo", "Deletar um jogo" ]


    def capturar_escolha(self):
        print("[yellow]Digite sua escolha: [/]", end="")
        escolha = str(input())
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
                print("escolha 1")
            case 2:
                print("escolha 2")
            case 3:
                print("escolha 3")
            case 4:
                print("escolha 4")
            case 5:
                print("escolha 5")
