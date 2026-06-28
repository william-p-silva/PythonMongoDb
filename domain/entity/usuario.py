
import uuid


class Usuario:
    def __init__(self, nome, idade, senhaHash, email):
        if not nome.strip(): raise ValueError("Nome de usuário inválido. ")
        if not email.strip(): raise ValueError("Email inválido. ")
        try:
            idade_int = int(idade)
            if idade_int <= 0 or idade_int >= 110: 
                raise ValueError("Idade inválida (idade deve ser maior que zero e meor que 110). ")
        except:
            raise ValueError("Idade inválida")

        self.Id = uuid.uuid4()
        self.Nome = nome
        self.Email = email
        self.Idade = idade_int
        self.Senha = senhaHash


    def to_json(self) -> dict:
        """Auxiliar para converter a entidade em um documento do MongoDB."""
        return {
            "id": str(self.Id),
            "nome": self.Nome,
            "idade": self.Idade,
            "email": self.Email,
            "senha": self.Senha
            }