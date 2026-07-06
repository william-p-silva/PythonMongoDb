import uuid


class Jogo:
    def __init__(self, titulo: str, descricao: str, usuario_id: int, jogo_id: str = None,
                 plataformas: list = None, especificacoes_user: list = None, conquistas: list = None,
                 usuario_email: str = None):

        if not titulo.strip(): raise ValueError("Titulo inválido. ")
        if not descricao.strip(): raise ValueError("Descrição inválida. ")
        if usuario_id == None: raise ValueError("Id do usuário inválido. ")

        self.Jogo_Id = jogo_id if jogo_id is not None else uuid.uuid4()
        self.Usuario_Id = usuario_id
        self.Titulo = titulo
        self.Descricao = descricao
        self.Plataformas = plataformas if plataformas is not None else [] 
        self.Especificacoes_User = especificacoes_user if especificacoes_user is not None else []
        self.Conquistas = conquistas if conquistas is not None else []
        self.Usuario_Email = usuario_email
    

    def add_plataformas(self, plataforma: str):
        self.Plataformas.append(plataforma)


    def add_conquistas(self, nome: str, raridade: str):
        self.Conquistas.append({
            "nome": nome,
            "raridade": raridade
            })


    def add_especificacoes_user(self, titulo: str, descricao: str):
        self.Especificacoes_User.append({
            titulo: descricao
            })


    def to_json(self) -> dict:
        """Auxiliar para converter a entidade em um documento do MongoDB."""
        dados = {
            "jogo_id": str(self.Jogo_Id),
            "usuario_id": self.Usuario_Id,
            "titulo": self.Titulo,
            "descricao": self.Descricao,
            "plataformas": self.Plataformas,
            "especificacoes_user": self.Especificacoes_User,
            "conquistas": self.Conquistas
        }
        if self.Usuario_Email is not None:
            dados["usuario_email"] = self.Usuario_Email
        return dados

