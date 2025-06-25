class Cliente:
    def __init__(self, nome, cpf, cell, mail):
        self.nome = nome
        self.cpf = cpf
        self.cell = cell
        self.mail = mail

    def __str__(self):
        return (f"Nome: {self.nome}, CPF: {self.cpf}, Telefone: {self.cell}, E-mail: {self.mail}")