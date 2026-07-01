from infrastructure.data.context.appDbContext import AppDbContext
from domain.entity.jogo import Jogo

class JogoRepository:
    def __init__(self):
        self.Context = AppDbContext()
        self.Collection = self.Context.Data_Base["jogos"]

    def cadastro_jogos(self, jogo: dict):
        self.Collection.insert_one(jogo)

    def listar_jogos(self):
        return self.Collection.find()