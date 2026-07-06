from infrastructure.data.context.appDbContext import AppDbContext


class UsuarioRepository:
    def __init__(self):
        self.Context = AppDbContext()
        self.Collection = self.Context.Data_Base["usuarios"]

    def cadastro_usuario(self, usuario: dict):
        self.Collection.insert_one(usuario)

    def buscar_usuario_por_email(self, email: str):
        return self.Collection.find_one({"email": email})

    def deletar_usuario(self, email: str):
        self.Collection.delete_one({"email": email})
