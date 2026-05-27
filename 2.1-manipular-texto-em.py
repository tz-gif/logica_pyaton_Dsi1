# AULA COMPLETA - STRINGS EM PYTHONY

# - CRIAÇÃO DE STRINGS
# - STRINGS MULTILISMHA
# - INDICES E SLICES 
# - PERAÇÃO COM STRINGS
# - IMUTABILIDADE
# - FORMATAÇÃO DE TEXTO
# - UNICODE E BYTES

#-------------------
# 1 CRIANÇÃO DE STRIGS
#-------------------
# STRIGS SÃO TEXTOS EM PYTHON
# PODEN SER CRIADAS COMO UDSANDO ASPAS SIMPLES  OU DUPLAS

TEXTO1 = "python"
TEXTO2 = "Curso de python"
TEXTO3 = "Copa "padrão fifa"

print(texto1, text02, texto3, texto4)

# Python permitir misturar aspas simples e duplas, dentro das strings sem precisar escarpar carcters

#------------------
# 2) strings multilhinas
#------------------
# usando tres aspas ("""ou'''') para citar textos que ocumpa varias linhas 

menu - """\
uso: programa[opções]
-h exibe ajuda
-u url do dataset

""""""""""'"""

print(menu)

# essa formato é muito usado para:
# - menus
# - documentçaõ
# - textos longos

#--------------------------
# 3) contanaçaõ automatico
#--------------------------
# Qaundo duas strings aparecem lado a lado, o python junta automaticamente

texto =("copa" "2026" "neymar é show memsmo?")
print(texto)

#---------------------------
# 4) string como sequencia
#---------------------------
# uma string funciona como um sequencia de caracteres, cada caracteres possui um indice
 

st = "maracana"
print ("primeira letra:" sta[0])
# só exibi a letra:m

print ("ultima letra:", st[-1])

print ("trecho 1:4", st a[1:4])

print ("do inicio até 3", sta[:3])

print ("do 2 até o fim:", st[2:]
       
print ("tamanho", len(st))