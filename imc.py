nome = input('Digite seu nome: ')

#input é usado para receber algum dado.

peso = int(input("Digite seu peso: "))

#int é usado para receber valores inteiros.

altura = float(input("Digite sua altura: "))

#float é usado para receber números com casas decimnais.

imc=peso/(altura*altura)

#print é usado para fornecer algum dado no terminal.

if imc < 18.5:
    print(nome,"tem IMC igual a",((imc)),"classificado como Abaixo do peso" )

elif imc <=24.9:
    print(nome,"tem IMC igual a",((imc)),"classificado como Peso ideal" )

elif imc <=29.9:
    print(nome,"tem IMC igual a",((imc)),"classificado como Sobrepeso")

elif imc <=34.9:
    print(nome,"tem IMC igual a",((imc)),"classificado como Obesidade grau 1")

elif imc <=39.9:
    print(nome,"tem IMC igual a",((imc)),"classificado como Obesidade grau 2")

elif imc <=40:
    print(nome,"tem IMC igual a",((imc)),"classificado como Obesidade grau 3")

else:
    print(nome, "Seloko, num compensa.")

#if, elif e else, é a criação de uma condição.

