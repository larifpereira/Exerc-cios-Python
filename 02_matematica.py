# Calcular: 2 mais 3 vezes 3 
print(2 + (3*3))

# Calcular 4 elevado a 2, dividido por 3
print ((4**2)/3)

# Calcular: 9 elevado a 2 mais 2 vezes 6 menos 1
print ((((9**2)+2)*6)-1)

# Calcular 7 elevado a 2 mais 3 vezes 4 menos 2
print ((((7**2)+3)*4)-2)

# Calcular: 5 elevado a 2 menos 1 vezes 3 mais 6
print ((((5**2)-1)*3)+6)

# Calcular: 8 elevado a 2 mais 4 divido por 2 menos 5
print ((((8**2)+4)/2)-5)

#Calcular: número elevado a potência (solicitar)
n = float(input("Digite um número: "))
pot = int(input("Digite a potência: "))
calculo = (n**pot)
print("{} elevado a {} é igual a: {}".format(n,pot,calculo))

# Calcular: 403 dividido por 73 (inteiro)
v1 = 403
v2 = 73
div = int((v1/v2))
print(f"{v1} dividido por {v2} é: {div}")

# Calcular: 403 dividido por 73 (decimal)
v1 = 403
v2 = 73
div = float((v1/v2))
print(f"{v1} dividido por {2} é: {div}")

# Calcular: média de 3 notas (solicitar)
n1 = float(input("Digite o valor da 1ª prova: "))
n2 = float(input("Digite o valor da 2ª prova: "))
n3 = float(input("Digite o valor da 3ª prova: "))
media = float((n1+n2+n3)/3)
print(f"Sua média é de {media}")

# Calcular: quantas vezes o número 73 cabe no 403 (inteiro)
numx = 73
num = 403
res = int(403/73)
sobra = int(403%73)
print(f"A quantidade de vezes que o {numx} cabe no {num} é {res} e sobra {sobra}")

# Calcular: quantas vezes o número 73 cabe no 403 (decimal)
numx = 73
num = 403
res = float(403/73)
sobra = float(403%73)
print(f"A quantidade de vezes que o {numx} cabe no {num} é {res} e sobra {sobra}")

# Calcular: valor absoluto da diferença entre 54 e 57
print(abs(54-57))

# Calcular: menor valor entre 29, 31 e 34
print(min(29,31,34))

#Calcular: menor valor entre 12, 1 e 64
print(min(12,1,64))

