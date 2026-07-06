from infrastructure.data.repository.jogosRepositorys import JogoRepository
from infrastructure.data.repository.usuariosRepository import UsuarioRepository
from rich.prompt import Prompt, Confirm
from domain.entity.jogo import Jogo
from view.jogo.jogo import Tela_Jogo
from rich.panel import Panel
from rich import print
from application.utils.terminal import Terminal
from time import sleep

class AlterarJogoUseCase:
    def __init__(self):
        self.jogo_repository = JogoRepository()
        self.usuario_repository = UsuarioRepository()

    def execute(self):
        terminal = Terminal()
        while True:
            terminal.limpar_terminal()
            nome_jogo = Prompt.ask("Digite o nome do jogo que deseja alterar (ou '-1' para sair)")
            if nome_jogo == "-1":
                break
            jogo = self.jogo_repository.buscar_jogo_nome(nome_jogo)
            if jogo:
                tela_jogo = Tela_Jogo()
                jogo_class = Jogo(
                    jogo_id=jogo["jogo_id"],
                    titulo=jogo["titulo"],
                    descricao=jogo["descricao"],
                    usuario_id=jogo["usuario_id"],
                    conquistas=jogo["conquistas"],
                    especificacoes_user=jogo["especificacoes_user"],
                    plataformas=jogo["plataformas"],
                    usuario_email=jogo.get("usuario_email")
                )

                tela_jogo.tela_jogo(jogo_class)

                print()
                if jogo_class.Usuario_Email:
                    print(f"[blue]Email do usuário vinculado atualmente: {jogo_class.Usuario_Email}[/]")
                else:
                    print("[yellow]Nenhum email de usuário vinculado atualmente.[/]")

                alterar_email = Confirm.ask("Deseja alterar o email do usuário vinculado?")
                if alterar_email:
                    while True:
                        novo_email = Prompt.ask("Digite o novo email do usuário vinculado")
                        if not novo_email.strip() or "@" not in novo_email:
                            print("[red]Email inválido. Informe um email com '@'.[/]")
                            continue
                        usuario = self.usuario_repository.buscar_usuario_por_email(novo_email)
                        if not usuario:
                            print("[yellow]Nenhum usuário encontrado com esse email.[/]")
                            continue
                        jogo_class.Usuario_Email = usuario["email"]
                        print("[green]Email vinculado atualizado.[/]")
                        break

                print()
                new_titulo = Prompt.ask("Digite o novo título do jogo (ou pressione Enter para manter o atual)", default=jogo_class.Titulo)
                jogo_class.Titulo = new_titulo

                new_descricao = Prompt.ask("Digite a nova descrição do jogo (ou pressione Enter para manter a atual)", default=jogo_class.Descricao)
                jogo_class.Descricao = new_descricao

                conteudo = "Você deseja alterar as plataformas ou adicionar uma nova plataforma? \n(Digite 'alterar' para alterar, 'adicionar' para adicionar, ou pressione Enter para manter as atuais)"

                print()
                painel = Panel(conteudo, title="Alterar Plataformas", border_style="blue", width=90)
                print(painel)
                print()

                acao_plataforma = Prompt.ask("Digite sua escolha", choices=["alterar", "adicionar"], default="")
                if acao_plataforma == "alterar":
                    for index, plataforma in enumerate(jogo_class.Plataformas):
                        new_plataforma = Prompt.ask(f"Digite a nova plataforma para substituir '{plataforma}' (ou pressione Enter para manter a atual)", default=plataforma)
                        
                        jogo_class.Plataformas[index] = new_plataforma
                        print(jogo_class.Plataformas[index])
                if acao_plataforma == "adicionar":                    
                    new_plataformas = Prompt.ask("Digite as novas plataformas separadas por vírgula (ou pressione Enter para não adicionar novas)")
                    list_new_plataforams = new_plataformas.split(",") if new_plataformas else []
                    for index, plataforma in enumerate(list_new_plataforams):
                        jogo_class.add_plataformas(plataforma.strip())


                conteudo = "Você deseja alterar as conquistas ou adicionar uma nova conquista? \n(Digite 'alterar' para alterar, 'adicionar' para adicionar, ou pressione Enter para manter as atuais)"

                print()
                painel = Panel(conteudo, title="Alterar Conquistas", border_style="blue", width=90)
                print(painel)
                print()

                acao_conquista = Prompt.ask("Você deseja alterar as conquistas ou adicionar uma nova conquista? \n(Digite 'alterar' para alterar, 'adicionar' para adicionar, ou pressione Enter para manter as atuais)", choices=["alterar", "adicionar"], default="")

                if acao_conquista == "alterar":
                    for index, conquista in enumerate(jogo_class.Conquistas):
                        new_nome = Prompt.ask(f"Digite o novo nome para a conquista '{conquista['nome']}' (ou pressione Enter para manter o atual)", default=conquista['nome'])

                        new_raridade = Prompt.ask(f"Digite a nova raridade para a conquista '{conquista['raridade']}' (ou pressione Enter para manter a atual)", default=conquista['raridade'])

                        jogo_class.Conquistas[index] = {"nome": new_nome, "raridade": new_raridade}

                if acao_conquista == "adicionar":
                    new_nome = Prompt.ask("Digite o nome da nova conquista (ou pressione Enter para não adicionar novas)")
                    new_raridade = Prompt.ask("Digite a raridade da nova conquista (ou pressione Enter para não adicionar novas)")

                    if new_nome and new_raridade:
                        jogo_class.add_conquistas(new_nome, new_raridade)

                conteudo = "Você deseja alterar as especificações do usuário ou adicionar uma nova especificação do usuário? \n(Digite 'alterar' para alterar, 'adicionar' para adicionar, ou pressione Enter para manter as atuais)"
                
                print()
                painel = Panel(conteudo, title="Alterar Especificações do Usuário", border_style="blue", width=90)
                print(painel)
                print()

                acao_especificacao = Prompt.ask("Você deseja alterar as especificações do usuário ou adicionar uma nova especificação do usuário? \n(Digite 'alterar' para alterar, 'adicionar' para adicionar, ou pressione Enter para manter as atuais)", choices=["alterar", "adicionar"], default="")

                if acao_especificacao == "alterar":
                    for index, especificacao in enumerate(jogo_class.Especificacoes_User):
                        for chave, valor in list(especificacao.items()):
                            new_chave = Prompt.ask(f"Digite a nova chave para '{chave}' (ou pressione Enter para manter a atual)", default=chave)                            
                            new_valor = Prompt.ask(f"Digite o novo valor para '{chave}' (ou pressione Enter para manter o atual)", default=valor)
                            
                            jogo_class.Especificacoes_User[index][new_chave] = new_valor

                if acao_especificacao == "adicionar":
                    new_titulo = Prompt.ask("Digite o título da nova especificação do usuário (ou pressione Enter para não adicionar novas)")
                    new_descricao = Prompt.ask("Digite a descrição da nova especificação do usuário (ou pressione Enter para não adicionar novas)")

                    if new_titulo and new_descricao:
                        jogo_class.add_especificacoes_user(new_titulo, new_descricao)

                self.jogo_repository.alterar_jogo(jogo_class.Jogo_Id, jogo_class.to_json())

                print("[green]Alterando Jogo [/]", end='')
                for c in range(5):
                    sleep(0.3)
                    print("[green] . [/green]", end='')
                print()
                break
            else:
                print("Jogo não encontrado. Verifique as letras Maíusculas e Minúsculas e tente novamente.")