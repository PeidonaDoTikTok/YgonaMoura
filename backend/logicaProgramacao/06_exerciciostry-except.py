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

calcular_media()



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

separar_numeros(lista_mista)




