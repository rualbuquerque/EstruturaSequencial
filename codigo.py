import  math
import numpy as np
import scipy as sp

'''
#1
print('1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.')
print ("Hello World")

print()

#2
print('2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].')

numero = input('Digite um número: ')
print("O número informado foi ", numero)

print()

#3
print("3. Faça um Programa que peça dois números e imprima a soma.")
firstnumber = input("Digite um número: ")
secondnumber = input("Digite outro número: ")
soma = int(firstnumber) + int(secondnumber)
print( "A soma dos dois números informados é", soma)

print()


#4
print("Faça um Programa que peça as 4 notas bimestrais e mostre a média.")
nota1 = input("Informe sua nota do primeiro bimestre: ")
nota2 = input("Informe sua nota do segundo bimestre: ")
nota3 = input("Informe sua nota do terceiro bimestre: ")
nota4 = input("Informe sua nota do quarto bimestre: ")

média = (int(nota1) + int(nota2) + int(nota3) + int(nota4)) / 4

print("A sua média é:", média)

print()


#5

print("5. Faça um Programa que converta metros para centímetros.")
metros = input("Informe sua altura em metros: ")
centimetros = float(metros) *100
print("Sua altura em centímetros é", centimetros, "centímetros")

print()

#6
print("6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.")
raio = input("Informe o raio do círculo (em metros. Use um ponto para decimais, se aplicável): ")
raio2 = float(raio)
raioquadrado = raio2 * raio2
pi = 3.14
area = pi * raioquadrado
print("A área do círculo informado é = ", area, "metros")
print()


#7

print("7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.")
quadrado = input("Informe o comprimento do lado do quadrado (em metros. Use um ponto para decimais, se aplicável): ")
quadrado2 = float(quadrado)
area = quadrado2 * quadrado2
print("A área deste quadrado é de", area, "metros")

print()

#8

print("8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.")
hora = input("Quanto você ganha por hora? ")
semana = input("Quantas horas você trabalha por semana? ")
mes = int(semana) * 4
hora = int(hora)
salario = hora * mes

print("Você ganha ", salario, "por mês")

print()


#9

print("9. Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.")
fahrenheit = input("Qual a temperatura em Fahrenheit? ")
fahrenheit = int(fahrenheit)
celsius = (5*(fahrenheit - 32)/9)

print (fahrenheit, "em fahrenheit", "são", celsius,"º Celsius")

print()



#10

print("10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.")
celsius = input("Informe a temperatura em Celsius: ")
celsius = int(celsius)
fahrenheit = (celsius * 9 / 5) + 32

print(celsius,"º celsius", "são", fahrenheit, "fahrenheit.")

print()


#11

print("11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:"
      "\n 1) o produto do dobro do primeiro com metade do segundo."
      "\n 2) a soma do triplo do primeiro com o terceiro."
      "\n 3) o terceiro elevado ao cubo.")

inteiro1 = input("Digite um número inteiro: ")
inteiro1 = int(inteiro1)

inteiro2 = input("Digite outro número inteiro: ")
inteiro2 = int(inteiro2)

numeroreal = input("Digite um número real: ")
numeroreal = float(numeroreal)
print()

#1
dobrointeiro1 = inteiro1 + inteiro1
metadesegundo = inteiro2 /2
resultado1 = dobrointeiro1 * metadesegundo

print("O produto do dobro do primeiro número com a metade do segundo é: ", resultado1)

#2
triplointeiro1 = inteiro1 * 3
resultado2 = triplointeiro1 + numeroreal

print("A soma do triplo do primeiro com o terceiro é ", resultado2)

#3
cubonumeroreal = numeroreal **3

print("O terceiro número elevado ao cubo é ", cubonumeroreal)

print()

#12

print("Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58")
print()
print("Descubra o seu peso ideal")
print()

altura = input("Qual é a sua altura? ")
altura = float(altura)

pesoideal = ((72.7 * altura) - 58)

print("O seu peso ideal é ", pesoideal, "kg")

print()


#13

print("Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:"
      "\n Para homens: (72.7*h) - 58"
      " \n Para mulheres: (62.1*h) - 44.7")

genero = input("Qual é o seu gênero? (F para feminino e M para masculino): ")
peso = input("Qual é o seu peso? ")
peso = float(peso)

altura = input("Qual é a sua altura? ")
altura = float(altura)


if genero == "F":
    pesoideal = ((62.1 * altura) - 44.7)

else:
    pesoideal = ((72.7 * altura) - 58)

print("O seu peso ideal é ", pesoideal, "kg")


print()

#14

print("14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu "
      "\n trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do "
      "\n estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você "
      "\n faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a "
      "\n quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os "
      "\n dados do programa com as mensagens adequadas.")
print()

pescaria = input("Digite o peso do peixe pescado (em kg. Use um ponto para indicar decimais): ")
pescaria = float(pescaria)

excedente = pescaria - 50

if excedente > 0:
    multa = excedente * 4
    print("A multa a ser paga é de ", multa, "reais.")

else:
    print("Não há multa a ser paga em relação a este peixe.")

print ()


#15

print("15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e "
      "\n mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% "
      "\n para o INSS e 5% para o sindicato, faça um programa que nos dê:"
      "\n salário bruto; quanto pagou ao INSS; quanto pagou ao sindicato; o salário líquido; calcule os descontos e o "
      "salário líquido, conforme a tabela abaixo:"
      "\n + Salário Bruto : R$"
      "\n - IR (11%) : R$"
      "\n - INSS (8%) : R$"
      "\n - Sindicato ( 5%) : R$"
      "\ n= Salário Liquido : R$")

print()

hora = input("Quanto você ganha por hora? ")
semana = input("Quantas horas você trabalha por semana? ")
mes = int(semana) * 4
hora = float(hora)

salariobruto = hora * mes
impostoderenda = (salariobruto * 11)/100
inss = (salariobruto*8)/100
sindicato = (salariobruto*5)/100
salarioliquido = salariobruto - impostoderenda - inss - sindicato

print()

print("O seu salário bruto é: R$", salariobruto)
print("IR (11%): R$", impostoderenda)
print("INSS (8%): R$", inss)
print("Sindicato (5%): R$", sindicato)
print("Salário Líquido: R$", salarioliquido)

print ()

#16

print("16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser "
      "\n pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é "
      "\n vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a "
      "\n serem compradas e o preço total.")

print()

area = input("Qual o tamanho (em metros quatrados) da área a ser pintada? ")
area = int(area)

lata = 54

qtdlata = area / lata
qtdlata = math.ceil(qtdlata)
preco = qtdlata * 80
preco = math.ceil(preco)

print("Você precisará comprar", qtdlata, "latas e gastará", preco, "reais.")
