# Resumo do funcionamento do try/except
# O bloco 'try' tenta executar o código, se houver erro, ele entra no bloco 'except'
# O bloco 'except' captura o erro específico e pode ser tratado da maneira desejada
# Exemplo de estrutura básica:
# try:
#     # Código que pode gerar um erro
# except TipoDeErro:
#     # Código que é executado quando ocorre um erro

# Exemplo 1: Usando uma lista
def acessar_lista(lista, indice):
    try:
        # Tentamos acessar o elemento pelo índice
        return lista[indice]
    except IndexError:
        # Se o índice não existir, tratamos o erro
        return "Índice fora do alcance!"

# Testando a função com diferentes índices
minha_lista = [1, 2, 3, 4]
print(acessar_lista(minha_lista, 2))  # Saída: 3
print(acessar_lista(minha_lista, 5))  # Saída: Índice fora do alcance!

# Exemplo 2: Usando divisão e tratando o erro de divisão por zero
def dividir(a, b):
    try:
        # Tentamos realizar a divisão
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        # Se o divisor for zero, tratamos o erro
        return "Não é possível dividir por zero!"

# Testando a função com diferentes valores
print(dividir(10, 2))  # Saída: 5.0
print(dividir(10, 0))  # Saída: Não é possível dividir por zero!

# Exemplo 3: Usando funções e listagem de números
def converter_lista_para_inteiros(lista):
    numeros_convertidos = []
    for item in lista:
        try:
            # Tentamos converter o item para inteiro
            numero = int(item)
            numeros_convertidos.append(numero)
        except ValueError:
            # Se não for possível converter, adicionamos uma mensagem de erro
            numeros_convertidos.append(f"'{item}' não é um número válido.")
    return numeros_convertidos

# Testando a função com uma lista de elementos mistos
lista_de_strings = ['10', '20', 'abc', '30']
print(converter_lista_para_inteiros(lista_de_strings)) 
# Saída: [10, 20, "'abc' não é um número válido.", 30]


