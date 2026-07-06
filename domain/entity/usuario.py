
import uuid


class Usuario:
    def __init__(self, nome, email, idade=None, senhaHash=None):
        if not nome or not nome.strip():
            raise ValueError("Nome de usuário inválido. ")
        if not email or not email.strip():
            raise ValueError("Email inválido. ")
        if "@" not in email:
            raise ValueError("Email inválido. Informe um email com '@'.")

        if idade is not None:
            try:
                idade_int = int(idade)
                if idade_int <= 0 or idade_int >= 110:
                    raise ValueError("Idade inválida (idade deve ser maior que zero e meor que 110). ")
            except (TypeError, ValueError):
                raise ValueError("Idade inválida")
        else:
            idade_int = None

        self.Id = uuid.uuid4()
        self.Nome = nome
        self.Email = email
        self.Idade = idade_int
        self.Senha = senhaHash

    def to_json(self) -> dict:
        """Auxiliar para converter a entidade em um documento do MongoDB."""
        dados = {
            "id": str(self.Id),
            "nome": self.Nome,
            "email": self.Email,
        }
        if self.Idade is not None:
            dados["idade"] = self.Idade
        if self.Senha is not None:
            dados["senha"] = self.Senha
        return dados