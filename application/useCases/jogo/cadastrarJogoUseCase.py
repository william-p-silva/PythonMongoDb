from rich import print
from rich.prompt import Confirm, Prompt, IntPrompt

from domain.entity.jogo import Jogo

class Cadastrar_Jogo_UseCase:
    def execute(self):
        while True:
            nome = Prompt.ask("Digite o Nome do Jogo")
            if not nome.strip(): 
                print("[red]Nome inválido. [/]")
                continue

            descricao = Prompt.ask("Digite a Descrição do Jogo")
            if not descricao.strip(): 
                print("Descrição inválida. ")
                continue

            num_plataformas = IntPrompt.ask("Em Quantas Plataformas o Jogo está Disponível")
            list_plataformas = []
            c = 0
            while c < num_plataformas:
                plataforma = Prompt.ask("Digite o Nome ou Sigla da Plataforma")
                if not plataforma.strip(): 
                    print("[red]Plataforma inválida. ")
                    continue
                c += 1
                list_plataformas.append(plataforma)

            confirma = Confirm.ask("Você Deseja Adicionar suas Conquistas")
            if confirma:
                num_conquistas = IntPrompt.ask("Quantas conquistas você gostaria de adicionar")
                c = 0
                list_conquista = []
                while c < num_conquistas:
                    nome_conquista = Prompt.ask("[yellow]Qual o Nome da Conquista [/]")
                    if not nome_conquista.strip():
                        print("[red]O nome da conquista é inválido. [/]")
                        continue
                    raridade_conquista = Prompt.ask("[green]Qual a Raridade da Conquista[/]")
                    if not raridade_conquista.strip():
                        print("[red]Raridade inválida. ")
                        continue

                    dict_conquista = {"nome": nome_conquista, "raridade": raridade_conquista}
                    list_conquista.append(dict_conquista)
                    c += 1



            opcao = str(input())
            if opcao == "-1" or nome == "-1": break