#Calcular: faça a comparação de dois números inteiros e diga qual é maior (solicitar).
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))
if(num1 >= num2):
  print(f"{num1} é maior ou igual {num2}")
else:
  print(f"{num2} é maior ou igual {num1}")

#Solicitando um número inteiro, apresente se é par ou ímpar
x = int(input("Digite um número inteiro: "))
if (x%2 == 0):
  print(f"{x} é um número par!")
else:
  print(f"{x} é um núemro ímpar!")

#Solicite o ano de nascimento e o ano atual e apresente se pode ou não tirar a CNH 
ano_n = int(input("Digite seu ano de nascimento: "))
ano_a = int(input("Digite o ano que está: "))
idade = int(ano_a - ano_n)
print(f"Você tem {idade} anos de idade")
if (idade >= 18):
  print("Você já pode tirar sua Carteira Nacional de Habilitação!")
else:
  print("Você ainda não pode tirar sua Carteira Nacional de Habilitação")

#Calcular: tempo de empresa para receber bonificação
#Solicitar ano que entrou, ano atual e salário 
#Funcionários com -5 anos de empresa receberam bonificação de 10%
#Funcionários com +5 anos de empresa receberam bonificação de 20%
ano = int(input("Digite o ano que estamos: "))
inicio = int(input("Digite o ano que entrou na empresa "))
salario = float(input("Digitei o valor do seu salário: R$ "))
tempo = int(atual - inicio)
if tempo >= 5:
  bonus = (salario * 0.2)
else:
  bonus = (salario * 0.1)
print("Parabéns! Você tem {} anos de empresa!".fomat(tempo))
print("Você reebeu uma bonificação de R$ {}".format(buns))
print("Seu salário agora é de R$ {}".format(salario+bonus))

#
