Controle de Clientes em Python

Este projeto é um programa simples e funcional desenvolvido em Python para realizar o cadastro e gerenciamento de clientes, com armazenamento local em um arquivo JSON. Ele foi criado com foco em oferecer uma interface clara e intuitiva para que qualquer pessoa consiga registrar, visualizar, alterar e remover informações de clientes com facilidade.

Objetivo

O objetivo do projeto é permitir que usuários possam armazenar os dados de seus clientes e manuseá-los da melhor forma possível. Com ele, é possível listar todos os registros, visualizar os dados de um cliente específico, deletar um ou todos os cadastros, e também alterar as informações de qualquer cliente, sempre que necessário.

Funcionalidades
	•	Registrar novos clientes
	•	Listar todos os clientes
	•	Consultar dados de um cliente específico
	•	Atualizar informações de um cliente
	•	Deletar um cliente individualmente
	•	Deletar todos os registros
	•	Gerar dados de teste automaticamente
	•	Menu interativo com navegação simples no terminal

Estrutura do Projeto

O projeto está organizado da seguinte forma:
	controle-clientes-python/
	├── main.py                  -> Responsável pelo menu principal e execução geral
	├── cliente.py               -> Classe Cliente com métodos __init__ e __str__
	├── cliente_controller.py    -> Funções responsáveis por adicionar, buscar, atualizar e excluir clientes
	├── database.json            -> Arquivo JSON que funciona como banco de dados local
	└── README.md                -> Arquivo de documentação

Armazenamento

Todos os dados dos clientes são armazenados localmente no arquivo database.json. O programa lê e escreve neste arquivo de forma automática, garantindo que todas as operações realizadas no terminal fiquem salvas.

Como Executar
	1.	Clone ou baixe o repositório para seu computador.
	2.	Certifique-se de que o Python 3.6 (ou superior) está instalado.
	3.	No terminal, execute o arquivo principal com: “python main.py”
	4.	O menu será exibido no terminal. A partir dele, você pode navegar pelas funcionalidades disponíveis.

Requisitos
	•	Python 3.6 ou superior
	•	Biblioteca opcional: rich (para exibir o menu com cores no terminal)
		Instalação: “pip install rich”

Autor

Este projeto foi desenvolvido por Matheus Gomes, estudante de Ciência da Computação na Universidade Federal da Paraíba (UFPB), como parte de sua jornada de aprendizado em programação com Python.


————————————————————————————————————————————————————————————————————————————————


Customer Management in Python

This project is a simple and functional program developed in Python to register and manage customers, with local storage using a JSON file. It was created with a focus on offering a clear and intuitive interface so that anyone can easily register, view, update, and remove customer information.

Purpose

The purpose of this project is to allow users to store their customer data and manage it in the best possible way. With this tool, you can list all records, view information about a specific customer, delete one or all records, and also update any customer’s data whenever necessary.

Features
	•	Register new customers
	•	List all customers
	•	View specific customer data
	•	Update customer information
	•	Delete a single customer
	•	Delete all customers
	•	Automatically generate test data
	•	Interactive menu with simple terminal navigation

Project Structure

The project is organized as follows: 	controle-clientes-python/
	├── main.py                  -> Handles the main menu and program execution
	├── cliente.py               -> Customer class with __init__ and __str__ methods
	├── cliente_controller.py    -> Functions for adding, searching, updating, and deleting customers
	├── database.json            -> JSON file used as a local database
	└── README.md                -> Documentation file

Storage

All customer data is stored locally in the database.json file. The program reads from and writes to this file automatically, ensuring that all operations performed in the terminal are saved.

How to Run
	1.	Clone or download the repository to your computer.
	2.	Make sure Python 3.6 (or higher) is installed.
	3.	In the terminal, run the main file with: “python main.py”
		4.	The menu will appear in the terminal. From there, you can navigate through all available features.

Requirements
	•	Python 3.6 or higher
	•	Optional library: rich (to display colored terminal menus)
		To install: “pip install rich”

Author

This project was developed by Matheus Gomes, a Computer Science student at the Federal University of Paraíba (UFPB), as part of his learning journey in Python programming.
	