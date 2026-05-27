# ======================================================
# MÓDULO 1 — CRIAÇÃO DE STRINGS
# ======================================================

# EX1
# Crie uma variável chamada texto1 com o valor "Logica"
# usando aspas duplas e exiba o conteúdo.

texto1 = "logica"
print(texto1)

# EX2
# Crie uma variável chamada texto2 com o valor
# 'Eu sou top em python' usando aspas simples e exiba.

texto2 = 'Eu sou top em python'
print(texto2)

# EX3
# Crie uma string usando aspas simples que contenha
# aspas duplas dentro do texto: copa "padrão fifa".

print( '"copa padrão fifa"')

# EX4
# Crie uma string usando aspas duplas que contenha
# aspas simples dentro do texto: copa 'padrão fifa'.

print( "'copa padrão fifa'" )

# ======================================================
# MÓDULO 2 — STRINGS MULTILINHA
# ======================================================

# EX5
# Crie uma string multilinha representando um menu
# com as opções:

textos= """
-A  Exibe ajuda
-E  Execute agora, quero jogar!
"""

# EX6
# Crie uma string multilinha contendo um poema
# com três versos.


poema = """\
O sol nasceu brilhando,
Os pássaros cantam no ar,
E a vida começa a sorrir.
"""

# ======================================================
# MÓDULO 3 — CONCATENAÇÃO AUTOMÁTICA
# ======================================================

# EX7
# Use concatenação automática de literais para unir
# as palavras "Volei" e "top!".

print("volei " "é top")

# EX8
# Concatene automaticamente as strings
# "Python", " é ", "demais" em uma única string.

print("Python  é  demais")

# ======================================================
# MÓDULO 4 — STRINGS COMO SEQUÊNCIAS
# ======================================================

# EX9
# Atribua "software" a uma variável chamada st
# e mostre a primeira letra da string.

st = "software"
print(st[0])

# EX10
# Usando a mesma string "software",
# mostre a última letra.

print(st [-1])

# EX11
# Mostre os caracteres do índice 1 até o índice 4
# (sem incluir o 4) da string "software ".


print(st [1:4])

# EX12
# Mostre os caracteres do início até o índice 3
# da string "software".


print(st [0:3])

# EX13
# Mostre os caracteres do índice 2 até o final
# da string "software".

print(st [2:7])

# EX14
# Mostre o tamanho da string "software"
# usando a função len().

print("tamanho da string", len(st))

# EX15
# Acesse o último caractere de "software"
# usando índice positivo (sem usar -1).
 
print(st [7])

# EX16
# Mostre os caracteres que estão nos índices pares
# da string "software".

print(st[::2])

# EX17
# Inverta a string "software".

print(st[::1])

#-----------------
# 5) operações com strings
#-----------------
#python permite varias operaçoes com o strings
print("m" in st)
#significa que a letra "m" existe dentro de strings
print("x" not in st)
#significa que "x" não existe  na strings
print("m" * 20 )
#multiplicar repete a strings
print("m" + "maracana")
#operador + concatena strings

#----------------------
# 6) strings são imutaveis
#----------------------
#strings não podem ser alterados diretamneta!!!
#isso significa que o conteudo original não muda
#o que acontece é a criação de uma nova strings

texto = "python 3"
#metodo replace cria uma strings
texto = texto.replace("3", "2")
print(texto)

#---------------------
# 7) metodos importantes
#---------------------
# strings possuem varios metodos uteis

cidade = "maracana"
#coloca a primeira linha maiusculo
print(cidade.replace())

#conta quantas vezes aquela letra
print(cidade.count("a"))

#verificar se começa com "m"
print(cidade.startswith("m"))

#verificar se termina com "z"
print(cidade.endswith("z"))

frase = "copa de 2022"

# Divide a strinhgs em uma linha
print(frase.split(" "))

#--------------------------
# 8) formato de strings
#--------------------------
