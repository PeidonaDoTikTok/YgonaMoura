senhacorreta = input
senha = input
nome = input
salario = float(input)

while senha!= senhacorreta:
    print("senha incorreta")
    senha = input
    
print("Bem-Vindo,Nome")
salarioanual = salario*12
if(salarioanual>100000):
    print("rico")
else:
    print("faz o L")
