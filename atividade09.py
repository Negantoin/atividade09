#Exercício Python 09: faça um software que verifique entre 2 numeros qual o maior
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
if numero1 > numero2:
    print("O primeiro número (", numero1, ") é maior que o segundo número (", numero2, ")")
else:
    print("O primeiro número (", numero1, ") é menor que o segundo número (", numero2, ")")