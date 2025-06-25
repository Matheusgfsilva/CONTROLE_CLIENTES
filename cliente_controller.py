from cliente import Cliente
import json #ler e salvar dados no formato json
import os #verifica se o arquivo existe
import re #limpador de CPF


DB_PATH = "/Users/matheusgomes/Documents/Documentos py/DUX/CONTROLE CLIENTES/database.json"
def db_confrim():

    #verifica se o arquivo existe
    if not os.path.exists(DB_PATH):
        print("Nao encontrei base de dados")
        return None
    
    #abre e carrega os dados
    with open(DB_PATH, "r") as file: #"r" é de read, ou seja, nao esta modificando nada
        try:
            clientes = json.load(file)
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo")
            return None
    
    #verifica se há clientes
    if not clientes:
        print("Nenhum cliente cadastrado ainda")
        return None
    
    return clientes

def lines(msg): 
    print(("-") * (len(msg)+2))
    print(f" {msg}")
    print(("-") * (len(msg)+2))
    print("")

def name_verf():
    #talvez add letra maiuscula nos sobrenomes
    '''
    FORMA ANTIGA

    nome = input("Nome: ").strip().capitalize()
    while True:
        if not nome:
            nome = input("O campo não pode ficar vazio!\nNome: ").strip().capitalize()
        elif not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", nome):
            nome = input("Digite somente letras!\nNome: ").strip().capitalize()
        else:
            return nome
    '''

    while True:
        nome = input("Nome: ").strip().capitalize()
        if not nome:
            print("O campo não pode ficar vazio!")
        elif not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", nome):
            print("Digite somente letras!")
        else:
            return nome

def cpf_verf():
    while True:
        cpf = input("CPF: ").strip()
        if not cpf:
            print("O campo não pode ficar vazio!")

        elif not re.fullmatch(r"[0-9.-]+", cpf):
            print("Digite caracteres válidos!")
        
        else: 
            cpf_limpo = re.sub(r"[.-]", "", cpf) #o ruim que ele ainda pode digitar nas casas erradas
            if len(cpf_limpo) == 11:
                cpf_padrao = f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:11]}"
                return(cpf_padrao)
            else:
                print("O CPF deve ter 11 dígitos!")

def cellverf():
    while True:
        cell = input("Telefone: ").strip()
        if not cell:
            print("O campo não pode ficar vazio!")
        
        elif not re.fullmatch(r"[0-9()-]+", cell):
            print("Digite caracteres válidos!")
        
        else: 
            cell_limpo = re.sub(r"[()-]", "", cell)
            if len(cell_limpo) == 11:
                cell_limpo = f"({cell_limpo[:2]}){cell_limpo[2:7]}-{cell_limpo[7:11]}"
                return(cell_limpo)
            else:
                print("O telefone deve ter 11 dígitos(DD + 9 + telefone)!")

def mail_verf():
    while True:
        mail = input("E-mail: ").strip()
        if not mail:
            print("O campo não pode ficar vazio!")
        #ERRADO
        #elif (("@gmail.com") not in mail) or (("@hotmail.com" not in mail)) or (("@msn.com" not in mail)) or (("@icloud.com" not in mail)) or (("@outlook.com" not in mail)):
        elif not (("@gmail.com" in mail) or ("@hotmail.com" in mail) or ("@msn.com" in mail) or ("@icloud.com" in mail) or ("@outlook.com" in mail)):
            print("Digite um E-mail válido")
        else:
            return(mail)
        
def register():
    nome = name_verf()

    cpf = cpf_verf()

    cell = cellverf()

    mail = mail_verf()

    novo_cliente = Cliente(nome, cpf, cell, mail)
    print(f"Cliente cadastrado: {novo_cliente}")

    #verifica se o aquivo existe, se nao cria uma lista vazia
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r") as file:
            try:
                clientes = json.load(file)
            except json.JSONDecodeError:
                clientes = []
    else:
        clientes = []
#adicionar o novo cliente
    clientes.append({
        "nome": novo_cliente.nome,
        "cpf": novo_cliente.cpf,
        "cell": novo_cliente.cell,
        "mail": novo_cliente.mail
    })
#salva de volta no arquivo
    with open(DB_PATH, "w") as file:
        json.dump(clientes, file, indent=4)

def list():
    clientes = db_confrim()
    if clientes is None:
        return
    
    for cliente in clientes:

        print(f"Nome: {cliente['nome']}")
        print(f"CPF: {cliente['cpf']}")
        print(f"Telefone: {cliente['cell']}")
        print(f"E-mail: {cliente['mail']}")
        print("")

def deleteone():
    clientes = db_confrim()
    if clientes is None:
        return

    cpf_alvo = str(input("Digite o CPF do cliente que deseja deletar: "))
    clientes_att = [] #lista para os clientes sem o deletado

    cliente_encontrado = False
    for cliente in clientes:
        if cliente["cpf"] == cpf_alvo:
            cliente_encontrado = True
        else:
            clientes_att.append(cliente) #adicionando na lista nova
    
    if cliente_encontrado:
        with open(DB_PATH, "w") as file: #"w" de write, voce esta apagando o conteudo anterior
            json.dump(clientes_att, file, indent=4) #passando a lista nova para o json
        print("Cliente deletado!")
    else:
        print("Cliente não encontrado")
    
def deleteall():
    clientes = db_confrim()
    if clientes == None:
        return
    clientes_empty = []
    with open(DB_PATH, "w") as file:
        json.dump(clientes_empty, file)
    print("Clientes deletados")

def find():
    clientes = db_confrim()
    if clientes == None:
        return
    how_find = int(input("Você quer procurar um cliente por CPF[1] ou Nome[2]: "))
    if how_find == 1:
        cpf_client = str(input("Digite o CPF que voce quer pesquisar: "))
        for cliente in clientes:
            if cliente['cpf'] == cpf_client:
                print(f"Nome: {cliente['nome']}")
                print(f"CPF: {cliente['cpf']}")
                print(f"Telefone: {cliente['cell']}")
                print(f"E-mail: {cliente['mail']}")
                print("")
    if how_find == 2:
        name_client = str(input("Nome do(s) cliente(s) que você quer pesquisar: "))
        for cliente in clientes:
            if name_client in cliente['nome']:
                print(f"Nome: {cliente['nome']}")
                print(f"CPF: {cliente['cpf']}")
                print(f"Telefone: {cliente['cell']}")
                print(f"E-mail: {cliente['mail']}")
                print("")

def update():
    clientes = db_confrim()
    if clientes == None:
        return
    clientes_att = []
    cliente_exist = False
    cpf_att = input("Digite o CPF do cliente que você deseja atualizar: ")
    
    for cliente in clientes:
        if cliente['cpf'] == cpf_att:
            cliente_exist = True
            nome = input("Nome: ").capitalize()
            cpf = input("CPF: ")
            cell = input("Telefone: ")
            mail = input("e-mail: ")
            novo_cliente = Cliente(nome, cpf, cell, mail)
            clientes_att.append({
                "nome": novo_cliente.nome,
                "cpf": novo_cliente.cpf,
                "cell": novo_cliente.cell,
                "mail": novo_cliente.mail
            })
        else:
            clientes_att.append(cliente)
        
    if cliente_exist:
        with open(DB_PATH, "w") as file:
            json.dump(clientes_att, file, indent=4)
        print("Cliente atualizado")
    else:
        print("Cliente não encontrado")



