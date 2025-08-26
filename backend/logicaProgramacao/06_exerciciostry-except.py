#usando(laços,função e try/except) crie um sistema para receber as notas de um aluno e calcule a média anual se digitar algo sem ser número tratar o erro


def calcular_media():
    notas = []
    for i in range(4):  # 4 bimestres
        while True:
            try:
                nota = float(input(f"Digite a nota {i+1}: "))
                notas.append(nota)
                break
            except ValueError:
                print("Erro! Digite um número válido.")
    media = sum(notas) / len(notas)
    print(f"Média anual: {media:.2f}")

#calcular_media()



#usando(lista,função,laços,try/except) você deverá criar uma lista com números e mensagens. se for número adicionar a uma lista a-
#-parte. se for mensagem tratar com o erro de tipo ao final mostrar a lista só com os números

def separar_numeros(lista_mista):
    lista_numeros = []
    for item in lista_mista:
        try:
            numero = float(item)
            lista_numeros.append(numero)
        except (ValueError, TypeError):
            print(f"Ignorando mensagem: {item}")
    print("Lista só com números:", lista_numeros)

lista_mista = []

qtd = int(input("Quantos elementos você quer adicionar na lista? "))

for i in range(qtd):
    valor = input(f"Digite o elemento {i+1} (pode ser número ou mensagem): ")
    lista_mista.append(valor)

#separar_numeros(lista_mista)


#criar uma lista com cadastro de usuario
#cadastrar-alterar-excluir-listar=usar(função,lista,try/except,laços)


usuarios = []

def cadastrar_usuario():
    try:
        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade: "))
        email = input("Digite o email: ")
        usuario = {"nome": nome, "idade": idade, "email": email}
        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!\n")
    except:
        print("Erro ao cadastrar. Verifique os dados e tente novamente.\n")

def listar_usuarios():
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.\n")
    else:
        for i, u in enumerate(usuarios):
            print(f"{i} - Nome: {u['nome']}, Idade: {u['idade']}, Email: {u['email']}")
        print()

def alterar_usuario():
    listar_usuarios()
    try:
        indice = int(input("Digite o número do usuário que deseja alterar: "))
        if 0 <= indice < len(usuarios):
            nome = input("Novo nome: ")
            idade = int(input("Nova idade: "))
            email = input("Novo email: ")
            usuarios[indice] = {"nome": nome, "idade": idade, "email": email}
            print("Usuário alterado com sucesso!\n")
        else:
            print("Índice inválido.\n")
    except:
        print("Erro ao alterar usuário.\n")

def excluir_usuario():
    listar_usuarios()
    try:
        indice = int(input("Digite o número do usuário que deseja excluir: "))
        if 0 <= indice < len(usuarios):
            usuarios.pop(indice)
            print("Usuário excluído com sucesso!\n")
        else:
            print("Índice inválido.\n")
    except:
        print("Erro ao excluir usuário.\n")

def menu():
    while True:
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Alterar usuário")
        print("4 - Excluir usuário")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            alterar_usuario()
        elif opcao == "4":
            excluir_usuario()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")

menu()

