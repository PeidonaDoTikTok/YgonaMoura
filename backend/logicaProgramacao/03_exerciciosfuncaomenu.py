#criar função de menu de opções e pedir a opção desejada ao usuário
saldo = 0
def menu():
    while opcao != "sair":

        print("========== Menu de Opções ========== \n")
        print("1 - Depositar \n")

        opcao = input("Digite a opção: ")

        if opcao == "1":
            depositar(saldo)

        elif opcao == "2":
            sacar(saldo)

        elif opcao == "3":
            verSaldo(saldo)
             
        elif opcao == "sair":
          print("Até breve")
            break

def depositar(saldo):
    valor = input("Digite o valor do depósito: ")
    saldo += valor

def sacar(saldo)
    valor = input("Digite o valor do saque: ")
    saldo -= valor

def verSaldo()
    print("Seu saldo é: ",saldo)



#quando usar print e nn usar
#pq nn fez fora a saida
#pq float




