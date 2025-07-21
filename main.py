from cliente_controller import lines, register, list, find, deleteall, deleteone, update, seed_test_data
import re
from rich.console import Console
console = Console()

while True:
    console.print("\n========= MENU =========", style="bold white")
    console.print("[0] GERAR DADOS DE TESTE AUTOMÁTICOS", style="cyan")
    console.print("[1] REGISTRAR CLIENTES", style="cyan")
    console.print("[2] LISTAR CLIENTES", style="cyan")
    console.print("[3] ESPECIFICAR CLIENTE", style="cyan")
    console.print("[4] DELETAR UM CLIENTE", style="cyan")
    console.print("[5] DELETAR TODOS OS CLIENTES", style="cyan")
    console.print("[6] ALTERAR CLIENTE", style="cyan")
    console.print("[9] SAIR", style="cyan")
    console.print("(sempre digite 9 para interromper um processo)", style="dim")

    choice = str(input("Digite: "))
    if choice == "0":
        seed_test_data()
    elif choice == "1":
        register()
    elif choice == "2":
        list()
    elif choice == "3":
        find()
    elif choice == "4":
        deleteone()
    elif choice == "5":
        deleteall()
    elif choice == "6":
        update()
    elif choice == "9":
        console.print("Muito obrigado pela escolha, até a próxima!", style="bold yellow")
        break
    elif not choice:
        console.print("\nO CAMPO NÃO PODE FICAR VAZIO", style="bold red")
    else:
        console.print("\nDIGITE UM NÚMERO VÁLIDO", style="bold red")
