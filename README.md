# EX1
# Use a função type() para verificar
# o tipo da variável "ano" com valor 2024.
ano = 2024
print("tipo:", type (ano))
''''''''''''''''''''''''''''''''''''''
# EX2
# Verifique se o número 3.14159
# é do tipo float usando isinstance().
numero = 3.14159
print (isinstance(numero, float))

# EX3
# Compare se o tipo de 100
# é igual ao tipo de True.

# EX4
# Use isinstance() para verificar
# se True pode ser considerado int.
resultado = isinstance (True, int)
print (resultado)


# EX5
# Verifique se o resultado de 5/2
# é do tipo float usando type() e isinstance().
resultado = 5/2
print("resultado",(isinstance (resultado, float)))

resultado = 5/2
print("resultado:",type (resultado))

# EX6
# Crie uma função que recebe um valor
# e imprime "É número!" se for int, float ou complex.
def verifica_numero(valor):

    if verifica_numero(valor, (int, float, complex)):
        print("Ex6: é número")
    else: 
        print( "Não é número.")
              
verifica_numero(42)
verifica_numero("texto")

# EX7
# Compare type() e isinstance()
# para verificar se um booleano
# é considerado inteiro.
resultado = isinstance(True, int)
print(resultado)

# EX8
# Descubra o tipo do número 3+4j
# usando type().
numero_complexo = 3 + 4j
print ("Valor:" , numero_complexo)
print ("Tipo:" ,type (numero_complexo))

# EX9
# Verifique se o valor None
# é do tipo NoneType usando isinstance().
valor = None
resultado = isinstance (None, type(None))
print ("Tipo:", type (resultado))


# EX10
# Verifique se o número 3.0
# é int, float ou complex usando isinstance()
# e depois teste especificamente se é int.
num1 = 3.0
resultado1 = isinstance(num1, int)
resultado2 = isinstance(num1, float)
resultado3 = isinstance(num1, complex)
print (resultado1)
print (resultado2)
print (resultado3)
print(isinstance(num1, int))
