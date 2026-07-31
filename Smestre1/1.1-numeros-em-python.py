# aula completa: numeros em python.py

""""
vamos aprender:
1- tipos de numeros 
2-conversoes de tipos
3-hierarquia numerica
4-operaçoes matematicas
5-coerção de tipos
6-verificação de tipos
7-entrada de dados
"""
###########################
##PASSO 01 - TIPOS NUMERICOS 
###########################
# INT-> NUMEROS INTEROS 
# FLOAT-> NUMEROS COM CASAS DECMAIS 
# COMPLEX -> NUMEROS COMPLEXOS (USADO EM MATEMATICA / ENGEARIA )#

print("--TIPOS DE NUMERICOS--")

# EXEMPLOS 01 - NUMEROS INTEROS
# CRIAMOS UMA VARIAVEL  CHAMADO NUMERO_INTERO
numero_imteiro=10 
print("valor:",numero_imteiro)

# type() mostra qual é o tipo da variavel 
print("tipo:", type(numero_imteiro)
      
#exemplo 2 - numero decimal
numero_decimal = 3.13
print("tipo:", type(numero_decimal))

#exemplo 3 - numeros cmplexos
#um número complexo possui duas partes:
#numero normal (numero normal)
  #parte imaginária (mutiplicad por j)
#estruturada geral;
#numero =a +bj

# a = parte real
# parte imaginária      
# j = unidade imaginária

numero_complexo = 2+3j
print("valor:", numero_complexo)
print("tipo:", type(numero_complexo))

#git clone e copiar o link

#exemplo 03 - acessando cada parte do número 

# .real retorna a parte real 
print("parte real:", numero_complexo.real)
#.img retorna a parte imaginária 
print ("parte imaginária:", numero_complexo.imag)

# apenas para separar visualmente a saída no terminal
print("\n\n")
  
  #ddaos vindos do usuario são textos (string), muitas vezes é nescessario converter eles

print("=== conversão ====")

# float -> int
valor =int (3.9)
print("int(3.9):", valor)
print("tipo:", type(valor))
 
 #string -> int
valor1 = "10"
print(type, (valor1))

valor2 =int ("10")
print('int ("10"):', valor2)
print("tipo:", type(valor2))

#int --> float
valor3 = float(10)
print("valor(10):", valor3)
print("tipo:", type(valor3))
      

      


