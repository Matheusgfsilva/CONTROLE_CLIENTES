from rich import print
from rich.prompt import Prompt
from cliente import Cliente
import json #ler e salvar dados no formato json
import os #verifica se o arquivo existe
import re #limpador de CPF


DB_PATH = "/Users/matheusgomes/Documents/CONTROLE_CLIENTES /database.json"
def db_confrim():

    #verifica se o arquivo existe
    if not os.path.exists(DB_PATH):
        print("\n[red]NÃO ENCONTREI BASE DE DADOS[/red]")
        return None
    
    #abre e carrega os dados
    with open(DB_PATH, "r") as file: #"r" é de read, ou seja, nao esta modificando nada
        try:
            clientes = json.load(file)
        except json.JSONDecodeError:
            print("\n[red]ERRO AO LER O ARQUIVO[/red]")
            return None
    
    #verifica se há clientes
    if not clientes:
        print("[yellow]Nenhum cliente cadastrado![/yellow]")
        return None
    
    return clientes

def lines(msg): 
    print(f"[bold magenta]{'-' * (len(msg)+2)}[/]")
    print(f" {msg}")
    print(f"[bold magenta]{'-' * (len(msg)+2)}[/]")

def quit(any):
    if any == "9":
        print("\n[yellow]OPERAÇÃO CANCELADA![/yellow]\n")
        return True

def name_verf(nome):
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
        if not nome:
            print("[red]O campo não pode ficar vazio![/red]")
        elif not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", nome):
            print("[red]Digite somente letras![/red]")
        else:
            return nome
        nome = Prompt.ask("Nome").strip().capitalize()
        if quit(nome):
            return(False)

def cpf_verf(cpf):
    while True:
        if not cpf:
            print("[red]O campo não pode ficar vazio![/red]")
        elif not re.fullmatch(r"[0-9.-]+", cpf):
            print("[red]Digite caracteres válidos![/red]")
        else: 
            cpf_limpo = re.sub(r"[.-]", "", cpf) #o ruim que ele ainda pode digitar nas casas erradas
            if len(cpf_limpo) == 11:
                # Verifica se todos os dígitos são iguais
                if cpf_limpo == cpf_limpo[0] * 11:
                    print("[red]CPF inválido![/red]")
                else:
                    # Cálculo do primeiro dígito verificador
                    soma = sum(int(cpf_limpo[i]) * (10 - i) for i in range(9))
                    dig1 = (soma * 10 % 11) % 10
                    # Cálculo do segundo dígito verificador
                    soma = sum(int(cpf_limpo[i]) * (11 - i) for i in range(10))
                    dig2 = (soma * 10 % 11) % 10
                    # Valida os dígitos
                    if cpf_limpo[-2:] == f"{dig1}{dig2}":
                        cpf_padrao = f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:11]}"
                        return(cpf_padrao)
                    else:
                        print("[red]CPF inválido![/red]")
            else:
                print("[red]O CPF deve ter 11 dígitos![/red]")
        cpf = Prompt.ask("CPF").strip()
        if quit(cpf):
            return(False)

def cellverf(cell):
    ddds_validos = {'11', '12', '13', '14', '15', '16', '17', '18', '19',
                    '21', '22', '24', '27', '28',
                    '31', '32', '33', '34', '35', '37', '38',
                    '41', '42', '43', '44', '45', '46',
                    '51', '53', '54', '55',
                    '61', '62', '63', '64', '65', '66', '67', '68', '69',
                    '71', '73', '74', '75', '77', '79',
                    '81', '82', '83', '84', '85', '86', '87', '88', '89',
                    '91', '92', '93', '94', '95', '96', '97', '98', '99'}
    while True:
        if not cell:
            print("[red]O campo não pode ficar vazio![/red]")
        elif not re.fullmatch(r"[0-9()-]+", cell.replace(" ", "")):
            print("[red]Digite caracteres válidos![/red]")
        else:
            cell = cell.replace(" ", "")
            cell_limpo = re.sub(r"[()-]", "", cell)
            ddd = cell_limpo[:2]
            if len(cell_limpo) != 11:
                print("[red]O telefone deve ter 11 dígitos (DD + 9 + telefone)![/red]")
            elif cell_limpo[2] != "9":
                print("[red]O número deve começar com 9 após o DDD![/red]")
            elif ddd not in ddds_validos:
                print("[red]DDD inválido![/red]")
            else:
                cell_limpo = f"({cell_limpo[:2]}){cell_limpo[2:7]}-{cell_limpo[7:11]}"
                return(cell_limpo)
        cell = Prompt.ask("Telefone").strip()
        if quit(cell):
            return(False)

def mail_verf(mail):
    while True:
        if not mail:
            print("[red]O campo não pode ficar vazio![/red]")
        elif not re.fullmatch(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", mail):
            print("[red]Digite um E-mail válido![/red]")
        else:
            return(mail)
        mail = Prompt.ask("E-mail").strip()
        if quit(mail):
            return(False)

def repeat_cpf(cpf):
    clientes = db_confrim()
    if clientes is None:
        return
    
    repeat = False
    while True:
        if not cpf:
            print("[red]O campo não pode ficar vazio![/red]")
        elif not re.fullmatch(r"[0-9.-]+", cpf):
            print("[red]Digite caracteres válidos![/red]")
        else: 
            cpf_limpo = re.sub(r"[.-]", "", cpf) #o ruim que ele ainda pode digitar nas casas erradas
            if len(cpf_limpo) == 11:
                # Verifica se todos os dígitos são iguais
                if cpf_limpo == cpf_limpo[0] * 11:
                    print("[red]CPF inválido![/red]")
                else:
                    # Cálculo do primeiro dígito verificador
                    soma = sum(int(cpf_limpo[i]) * (10 - i) for i in range(9))
                    dig1 = (soma * 10 % 11) % 10
                    # Cálculo do segundo dígito verificador
                    soma = sum(int(cpf_limpo[i]) * (11 - i) for i in range(10))
                    dig2 = (soma * 10 % 11) % 10
                    # Valida os dígitos
                    if cpf_limpo[-2:] == f"{dig1}{dig2}":
                        cpf_padrao = f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:11]}"
                        if any(cliente["cpf"] == cpf_padrao for cliente in clientes):
                            print("[yellow]CPF já cadastrado[/yellow]") 
                        else:
                            return(cpf_padrao)
                    else:
                        print("[red]CPF inválido![/red]")
            else:
                print("[red]O CPF deve ter 11 dígitos![/red]")
        cpf = Prompt.ask("CPF").strip()
        if quit(cpf):
            return(False)

def register(): #ver como o quit fica mais organizado
    nome = Prompt.ask("Nome").strip().title()
    if quit(nome):
        return
    nome = name_verf(nome)
    if not nome:
        return

    cpf = Prompt.ask("CPF").strip()
    if quit(cpf):
        return
    
    cpf = repeat_cpf(cpf)
    if not cpf:
        return

    cell = Prompt.ask("Telefone").strip()
    if quit(cell):
        return
    cell = cellverf(cell)
    if not cell:
        return

    mail = Prompt.ask("E-mail").strip()
    if quit(mail):
        return
    mail = mail_verf(mail)
    if not mail:
        return

    novo_cliente = Cliente(nome, cpf, cell, mail)
    print(f"\n[green]Cliente cadastrado: {novo_cliente}[/green]\n")

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
    print("-"*30)
    print("")
    for cliente in clientes:
        print(f"[bold]Nome:[/] {cliente['nome']}")
        print(f"[bold]CPF:[/] {cliente['cpf']}")
        print(f"[bold]Telefone:[/] {cliente['cell']}")
        print(f"[bold]E-mail:[/] {cliente['mail']}")
        print("")
    print("-" * 30)

def deleteone():
    clientes = db_confrim()
    if clientes is None:
        return

    while True:
        cpf_alvo = Prompt.ask("Digite o CPF do cliente que deseja deletar").strip()
        if quit(cpf_alvo):
            return
        cpf_alvo = cpf_verf(cpf_alvo)
        if not cpf_alvo:
            return
        clientes_att = [] #lista para os clientes sem o deletado
        cliente_encontrado = False
        confirm = True

        for cliente in clientes:
            if cliente["cpf"] == cpf_alvo:
                cliente_encontrado = True
                cliente_alvo = cliente
            else:
                clientes_att.append(cliente) #adicionando na lista nova
        
        if cliente_encontrado:
            print("")
            print(f"[bold]Nome:[/] {cliente_alvo['nome']}")
            print(f"[bold]CPF:[/] {cliente_alvo['cpf']}")
            print(f"[bold]Telefone:[/] {cliente_alvo['cell']}")
            print(f"[bold]E-mail:[/] {cliente_alvo['mail']}")
            print("")
            while True:
                confirm = Prompt.ask("Esse é o cliente que deseja deletar?[S]/[N]").strip().upper()
                if confirm == "S":
                        with open(DB_PATH, "w") as file: #"w" de write, voce esta apagando o conteudo anterior
                            json.dump(clientes_att, file, indent=4) #passando a lista nova para o json
                        print("[green]Cliente deletado![/green]")
                        break
                
                elif not confirm:
                    print("[red]O campo não pode ficar vazio![/red]")

                elif confirm == "N":
                    break
                
                else:
                    print("[red]Digite um caractere válido![/red]")

        else:
            print("[yellow]Cliente não encontrado[/yellow]")
        
        if confirm == "S":
            break
   
def deleteall():
    clientes = db_confrim()
    if clientes == None:
        return
    confirm = Prompt.ask("Tem certeza que deseja deletar TODOS os clientes [S]/[N]?").strip().upper()
    while True:
        if confirm == "S":
            clientes_empty = []
            with open(DB_PATH, "w") as file:
                json.dump(clientes_empty, file)
            print("[green]Clientes deletados![/green]")
            break
        elif confirm == "N":
            print("[yellow]Nenhum cliente deletado![/yellow]")
            break
        elif not confirm:
            print("[red]O campo não pode ficar vazio![/red]")
        else:
            print("[red]Digite um caractere válido![/red]")
        confirm = Prompt.ask("Tem certeza que deseja deletar TODOS os clientes [S]/[N]?").strip().upper()

def find():
    clientes = db_confrim()
    if clientes == None:
        return
    while True:
        how_find = Prompt.ask("Você quer procurar por CPF[1], Nome[2], Telefone[3] ou E-mail[4]?").strip()
        if not how_find:
            print("[red]O campo não pode ficar vazio[/red]")
        elif quit(how_find):
            return
        elif how_find not in ["1", "2", "3", "4"]:
            print("[red]Digite um número válido![/red]")
        else:
            break

    if how_find == "1":
        exist = False
        cpf_client = Prompt.ask("Digite o CPF que voce quer pesquisar").strip()
        if quit(cpf_client):
            return
        cpf_client = cpf_verf(cpf_client)
        if not cpf_client:
            return
        for cliente in clientes:
            if cliente['cpf'] == cpf_client:
                print("")
                print("-"*30)
                print(f"[bold]Nome:[/] {cliente['nome']}")
                print(f"[bold]CPF:[/] {cliente['cpf']}")
                print(f"[bold]Telefone:[/] {cliente['cell']}")
                print(f"[bold]E-mail:[/] {cliente['mail']}")
                print("-"*30)
                print("")
                exist = True
                break
        if not exist:
            print("[yellow]CPF não encontrado![/yellow]")

    if how_find == "2":
        exist = False
        name_client = Prompt.ask("Nome do(s) cliente(s) que você quer pesquisar").strip().title()
        if quit(name_client):
            return
        name_client = name_verf(name_client)
        if not name_client:
            return
        final_clients = []
        
        print("")
        print("-"*30, "\n")
        for cliente in clientes:
            if name_client in cliente['nome']:
                print(f"[bold]Nome:[/] {cliente['nome']}")
                print(f"[bold]CPF:[/] {cliente['cpf']}")
                print(f"[bold]Telefone:[/] {cliente['cell']}")
                print(f"[bold]E-mail:[/] {cliente['mail']}")
                print("")
                exist = True
        print("-"*30)
        if exist == False:
            print("[yellow]Nome não encontrado![/yellow]")

    if how_find == "3":
        exist = False
        cell_client = Prompt.ask("Digite o número que você quer pesquisar").strip()
        if quit(cell_client):
            return
        cell_client = cellverf(cell_client)
        if not cell_client:
            return
        print("")
        print("-"*30, "\n")
        for cliente in clientes:
            if cliente['cell'] == cell_client:
                print(f"[bold]Nome:[/] {cliente['nome']}")
                print(f"[bold]CPF:[/] {cliente['cpf']}")
                print(f"[bold]Telefone:[/] {cliente['cell']}")
                print(f"[bold]E-mail:[/] {cliente['mail']}")
                print("")
                exist = True
        print("-"*30)
        if not exist:
            print("[yellow]Telefone não encontrado![/yellow]")

    if how_find == "4":
        exist = False
        mail_client = Prompt.ask("Digite o e-mail que você quer pesquisar").strip()
        if quit(mail_client):
            return
        mail_client = mail_verf(mail_client)
        if not mail_client:
            return
        print("")
        print("-"*30, "\n")
        for cliente in clientes:
            if cliente['mail'] == mail_client:
                print(f"[bold]Nome:[/] {cliente['nome']}")
                print(f"[bold]CPF:[/] {cliente['cpf']}")
                print(f"[bold]Telefone:[/] {cliente['cell']}")
                print(f"[bold]E-mail:[/] {cliente['mail']}")
                print("")
                exist = True
        print("-"*30)
        if not exist:
            print("[yellow]E-mail não encontrado![/yellow]")

def update(): #COMO QUEBRAR O FOR? TENHO QUE FAZER DE FORMA MAIS OTIMIZADA
    clientes = db_confrim()
    if clientes == None:
        return
    
    while True:
        clientes_att = []
        cliente_exist = False
        confirm = "N"
        cpf_att = Prompt.ask("Digite o CPF do cliente que você deseja atualizar").strip()
        if quit(cpf_att):
            return
        cpf_att = cpf_verf(cpf_att)
        if not cpf_att:
            return
        
        for cliente in clientes:
            if cliente['cpf'] == cpf_att:
                cliente_exist = True
                print("")
                print(f"[bold]Nome:[/] {cliente['nome']}")
                print(f"[bold]CPF:[/] {cliente['cpf']}")
                print(f"[bold]Telefone:[/] {cliente['cell']}")
                print(f"[bold]E-mail:[/] {cliente['mail']}")
                print("")
                while True:
                    confirm = Prompt.ask("É esse cliente que você deseja atualizar o cadastro?[S]/[N]").strip().upper()
                    if confirm == "S":
                        while True:
                            escolha = Prompt.ask("Você quer atualizar: [1] Nome, [2] CPF, [3] Telefone, [4] E-mail, [5] Tudo").strip()
                            if quit(escolha):
                                return
                            elif escolha not in ["1", "2", "3", "4", "5"]:
                                print("[red]Escolha inválida![/red]")
                                continue

                            nome = cliente['nome']
                            cpf = cliente['cpf']
                            cell = cliente['cell']
                            mail = cliente['mail']

                            if escolha == "1":
                                nome = name_verf(Prompt.ask("Novo nome").strip())
                                if not nome:
                                    return
                            elif escolha == "2":
                                cpf = repeat_cpf(Prompt.ask("Novo CPF").strip())
                                if not cpf:
                                    return
                            elif escolha == "3":
                                cell = cellverf(Prompt.ask("Novo telefone").strip())
                                if not cell:
                                    return
                            elif escolha == "4":
                                mail = mail_verf(Prompt.ask("Novo e-mail").strip())
                                if not mail:
                                    return
                            elif escolha == "5":
                                nome = name_verf(Prompt.ask("Novo nome").strip())
                                if not nome:
                                    return
                                cpf = repeat_cpf(Prompt.ask("Novo CPF").strip())
                                if not cpf:
                                    return
                                cell = cellverf(Prompt.ask("Novo telefone").strip())
                                if not cell:
                                    return
                                mail = mail_verf(Prompt.ask("Novo e-mail").strip())
                                if not mail:
                                    return

                            novo_cliente = Cliente(nome, cpf, cell, mail)
                            clientes_att.append({
                                "nome": novo_cliente.nome,
                                "cpf": novo_cliente.cpf,
                                "cell": novo_cliente.cell,
                                "mail": novo_cliente.mail
                            })
                            break
                        break
                    elif confirm == "N":
                        break
                    elif not confirm:
                        print("[red]O campo não pode ficar vazio![/red]")
                    else:
                        print("[red]Digite apenas os caracteres válidos[/red]")
            else:
                clientes_att.append(cliente)

        if confirm == "S":       
            break

        if cliente_exist == False:
            print("[yellow]Cliente não encontrado[/yellow]")
            break
        
    if cliente_exist == True:
        with open(DB_PATH, "w") as file:
            json.dump(clientes_att, file, indent=4)
        print("[green]Cliente atualizado[/green]")

def seed_test_data():
    clientes = [
        {"nome": "Mateus Gomes", "cpf": "127.561.224-59", "cell": "(83)99106-0871", "mail": "mateusgfs@gmail.com"},
        {"nome": "Tiago Gomes", "cpf": "123.456.789-09", "cell": "(11)88888-8888", "mail": "tiago@email.com"},
        {"nome": "Renata Silva", "cpf": "456.789.123-01", "cell": "(21)99999-9999", "mail": "renata@email.com"},
        {"nome": "Elisa Barbosa", "cpf": "111.444.777-35", "cell": "(31)77777-7777", "mail": "elisa@email.com"},
        {"nome": "Joelton Félix", "cpf": "741.852.963-06", "cell": "(41)66666-6666", "mail": "joelton@email.com"},
        {"nome": "Letícia Gomes", "cpf": "159.753.486-20", "cell": "(51)55555-5555", "mail": "leticia@email.com"},
        {"nome": "Nathalia Feitosa", "cpf": "321.654.987-98", "cell": "(61)44444-4444", "mail": "nathalia@email.com"},
        {"nome": "Túlio Feitosa", "cpf": "987.654.321-00", "cell": "(71)33333-3333", "mail": "tulio@email.com"},
        {"nome": "Leonardo Freire", "cpf": "852.741.963-03", "cell": "(81)22222-2222", "mail": "leonardo@email.com"},
    ]

    with open(DB_PATH, "w") as file:
        json.dump(clientes, file, indent=4)
    print("[green]Clientes de teste adicionados com sucesso.[/green]")
