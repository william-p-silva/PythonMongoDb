from pymongo import MongoClient


class AppDbContext:
    def __init__(self):
        self.Conexao = MongoClient("mongodb://localhost:27017/")
        self.Data_Base = self.Conexao["gerenciar_jogos"]
        


