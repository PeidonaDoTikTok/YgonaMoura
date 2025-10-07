#excluir produtos no json

try:
    with open("loja.json",'r') as arquivo:
        inventario = json.load(arquivo)
    except FileNotFoundError:
        print("arquivo não encontrado")

novo_inventario = []
produto_excluido = False
 

id_produto_excluir = int (input("digite o id do produto para excluir"))
for produto in inventario:
    if produto['id'] != id_produto_excluir
    #se o id for diferente, adicionamos a nova lista
    novo_inventario.append(produto)
else:
    print("produto removido com sucesso!!")
    produto_excluido=True

if not produto_excluido:
    print("o id do produto não foi encontrado")

else:
    with open ("loja.json",'w')as arquivo:
        json.dump(novo_inventario,arquivo,indent=4)
    print("o arquivo foi atualizad0, produto removido")

#listar produtos do arquivo json
try:
    with open ("loja.json",'r') as arquivo:
        inventario = json.load(arquivo)

    if not inventario:
        print("o arquivo está vazio")
    else:
    print("----lista de produtos no inventário----")
    for produto in inventario:
        print(f"\n--Produto{produto.get('id')}--")
        print (f"Nome:{produto.get('nome_produto','n/a')}")
        print(f"Preço:{produto.get('preco_unitario',0):.2f}")
        print(f"Quantidade:{produto.get('quantidade',0)}unidades")
        print(f"Em estoque:{produto.get('em_estoque')}")
    Except FileNotFoundError:
        print("arquivo não encontrado")


#crie um sistema de gerenciamento de petshop
#devera ter os campos:nome,raça,idade,sexo,nome_dono,telefone_dono
#o nome do arquivo json deve ser "petshop.json."
#faça o crud completo
#ao terminar, demonstrar o exercicio para o professor

import json
import os

ARQUIVO = "petshop.json"

def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        return json.load(f)

def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

def adicionar_pet():
    dados = carregar_dados()
    pet = {}
    pet['nome'] = input("Nome do pet: ")
    pet['raca'] = input("Raça: ")
    pet['idade'] = input("Idade: ")
    pet['sexo'] = input("Sexo: ")
    pet['nome_dono'] = input("Nome do dono: ")
    pet['telefone_dono'] = input("Telefone do dono: ")

    dados.append(pet)
    salvar_dados(dados)
    print("Pet adicionado com sucesso!")

def listar_pets():
    dados = carregar_dados()
    if not dados:
        print("Nenhum pet cadastrado.")
        return
    for i, pet in enumerate(dados):
        print(f"\nPet {i+1}")
        for chave, valor in pet.items():
            print(f"{chave.capitalize()}: {valor}")

def atualizar_pet():
    dados = carregar_dados()
    if not dados:
        print("Nenhum pet cadastrado.")
        return

    listar_pets()
    try:
        indice = int(input("\nDigite o número do pet que deseja atualizar: ")) - 1
        if indice < 0 or indice >= len(dados):
            print("Número inválido.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    pet = dados[indice]
    print("Pressione ENTER para manter o valor atual.")
    for chave in pet.keys():
        novo_valor = input(f"{chave.capitalize()} ({pet[chave]}): ")
        if novo_valor.strip():
            pet[chave] = novo_valor

    salvar_dados(dados)
    print("Pet atualizado com sucesso!")

def deletar_pet():
    dados = carregar_dados()
    if not dados:
        print("Nenhum pet cadastrado.")
        return

    listar_pets()
    try:
        indice = int(input("\nDigite o número do pet que deseja deletar: ")) - 1
        if indice < 0 or indice >= len(dados):
            print("Número inválido.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    confirm = input(f"Tem certeza que deseja deletar o pet '{dados[indice]['nome']}'? (s/n): ")
    if confirm.lower() == 's':
        dados.pop(indice)
        salvar_dados(dados)
        print("Pet deletado com sucesso!")
    else:
        print("Operação cancelada.")

def menu():
    while True:
        print("\n--- Gerenciamento Petshop ---")
        print("1. Adicionar pet")
        print("2. Listar pets")
        print("3. Atualizar pet")
        print("4. Deletar pet")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_pet()
        elif escolha == "2":
            listar_pets()
        elif escolha == "3":
            atualizar_pet()
        elif escolha == "4":
            deletar_pet()
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
