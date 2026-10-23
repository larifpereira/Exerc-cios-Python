# Strings e operadores:
# Concatenação (+) e Repetição (*)

# Apresentar: A---B
s1 = "A" + "-" * 10 + "B"
print(s1)

# Apresentar: A   B
s1 = "A" + " " * 10 + "B"
print(s1)

# Apresentar: A   ---   B  
s1 = "A" + (" " * 5) + ("-" * 5) + (" " * 5) + "B"
print(s1)

# Concatenação e repetição de strings:
s1 = "ant"
s2 = "bat"
s3 = "cod"
# "ant bat cod"
print(s1 + " " + s2 + " " + s3)
# "ant ant ant ... (10 vezes)"
print((s1 + " ")*10)
# "ant bat bat cod cod cod"
print(((s1 + " ")*1) + ((s2 + " ")*2) + ((s3 + " ")*3))
# Outra opção: "ant bat bat cod cod cod"
print(1*(s1 + " ")+ 2*(s2 + " ")+ 3*(s3+" "))
# "ant bat and bat ... (10 vezes)"
print((s1+ " "+ s2 + " ")*10)
# "batbatcod batbatcod ... (5 vezes)"
print((s2 + s2 + s3 + " ")*5)
