# Calcular: faça a comparação de dois números inteiros e diga qual é maior (solicitar).
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))
if(num1 >= num2):
  print(f"{num1} é maior ou igual {num2}")
else:
  print(f"{num2} é maior ou igual {num1}")

# Solicitando um número inteiro, apresente se é par ou ímpar
x = int(input("Digite um número inteiro: "))
if (x%2 == 0):
  print(f"{x} é um número par!")
else:
  print(f"{x} é um núemro ímpar!")

# Solicite o ano de nascimento e o ano atual e apresente se pode ou não tirar a CNH 
ano_n = int(input("Digite seu ano de nascimento: "))
ano_a = int(input("Digite o ano que está: "))
idade = int(ano_a - ano_n)
print(f"Você tem {idade} anos de idade")
if (idade >= 18):
  print("Você já pode tirar sua Carteira Nacional de Habilitação!")
else:
  print("Você ainda não pode tirar sua Carteira Nacional de Habilitação")

# Calcular: tempo de empresa para receber bonificação
# Solicitar ano que entrou, ano atual e salário 
# Funcionários com -5 anos de empresa receberam bonificação de 10%
# Funcionários com +5 anos de empresa receberam bonificação de 20%
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

# Calcule para o usuário o valor total da sua compra
# Faça o escolher uma das alternativas: maçã, banana e laranja e a quantidade que deseja
# Valores: maça = 2.30 | banana = 1.85 | laranja = 3.60 
print("Escolha o que deseja comprar: ")
print("1 - Maçã")
print("2 - Banana")
print("3 - Laranja")
produto = int(input("Qual fruta deseja comprar? ")
quant = int(input("Quantas unidades? ")
if produto == 1:
  pagar = quant * 2.3
  print(f"Você comprou {quant} maça(s). Total a pagar R$ {pagar}")
elif produto == 2:
  pagar = quant * 1.85
  print(f"Você comprou {quant} banana(s). Total a pagar R$ {pagar}")
elif produto == 3:
  pagar = quant * 3.6
  print(f"Você comprou {quant} laranja(s). Total a pagar R$ {pagar}")
else:
  print("Produto inválido! Tente novamente.")
