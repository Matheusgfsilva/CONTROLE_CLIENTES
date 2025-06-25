from cliente_controller import lines, register, list, find, deleteall, deleteone, update

lines("CONTROLE DE CLIENTES")

while True:
    choice = int(input("REGISTRAR CLIENTES[1]\n" \
                        "LISTAR CLIENTES[2]\n" \
                        "DETALHAR CLIENTE[3]\n" \
                        "DELETAR UM CLIENTE[4]\n" \
                        "DELETAR TODOS OS CLIENTES[5]\n" \
                        "ATUALIZAR CLIENTE[6]\n" \
                        "SAIR[9]\n\n" \
                        "Digite: "))
    if choice == 1:
        register()
    if choice == 2:
        list()
    if choice == 3:
        find()
    if choice == 4:
        deleteone()
    if choice == 5:
        deleteall()
    if choice == 6:
        update()
    if choice == 9:
        break