from infrastructure.data.context.appDbContext import AppDbContext
from domain.entity.jogo import Jogo

class JogoRepository:
    def __init__(self):
        self.Context = AppDbContext()
        self.Collection = self.Context.Data_Base["jogos"]

    def cadastro_jogos(self, jogo: dict):
        self.Collection.insert_one(jogo)

    def listar_jogos(self, usuario_id_sistema: str):
        return self.Collection.find()

    def buscar_jogo_nome(self, nome: str):
        return self.Collection.find_one({"titulo": nome})
    
    def alterar_jogo(self, jogo_id: str, jogo_atualizado: dict):
        self.Collection.update_one({"jogo_id": jogo_id}, {"$set": jogo_atualizado})