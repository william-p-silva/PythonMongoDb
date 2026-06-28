import uuid


class Jogo:
    def __init__(self, titulo: str, descricao: str, usuario_id: uuid.UUID, 
                 plataformas: list = None, especificacoes_user: list = None, conquistas: list = None):

        if not titulo.strip(): raise ValueError("Titulo inválido. ")
        if not descricao.strip(): raise ValueError("Descrição inválida. ")
        if usuario_id == None: raise ValueError("Id do usuário inválido. ")

        self.Jogo_Id = uuid.uuid4()
        self.Usuario_Id = usuario_id
        self.Titulo = titulo
        self.Descricao = descricao
        self.Plataformas = plataformas if plataformas is not None else [] 
        self.Especificacoes_User = especificacoes_user if especificacoes_user is not None else []
        self.Conquistas = conquistas if conquistas is not None else []
    

    def add_plataformas(self, plataforma: str):
        self.Plataformas.append(plataforma)


    def add_conquistas(self, nome: str, raridade: str, desbloqueada: bool):
        self.Conquistas.append({
            "nome": nome,
            "raridade": raridade,
            "desbloqueada": desbloqueada
            })


    def add_especificacoes_user(self, titulo: str, descricao: str):
        self.Especificacoes_User.append({
            "titulo": titulo,
            "descricao": descricao
            })


    def to_json(self) -> dict:
        """Auxiliar para converter a entidade em um documento do MongoDB."""
        return {
            "jogo_id": str(self.Jogo_Id),
            "usuario_id": self.Usuario_Id,
            "titulo": self.Titulo,
            "descricao": self.Descricao,
            "plataformas": self.Plataformas,
            "especificacoes_user": self.Especificacoes_User,
            "conquistas": self.Conquistas            
            }

