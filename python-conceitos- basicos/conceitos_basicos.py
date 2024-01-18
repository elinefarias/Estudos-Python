###############    Exercicios em Python - Conceitos Básicos   ############

''' 
# Exercício 1: Operações com números
# a) Declare duas variáveis, 'a' e 'b', e atribua valores a elas.
# b) Imprima a soma, subtração, multiplicação e divisão de 'a' por 'b'.

var_a = 10
var_b = 5

print(f"Soma: {var_a + var_b}")
print(f"Subtracao: {var_a - var_b}")
print(f"Multiplicacao: {var_a * var_b}")
print(f"Divisao: {var_a / var_b}")


#__________________________________________________________________________________________________
# Exercício 2: Manipulação de strings
# a) Declare uma variável 'frase' com uma string.
# b) Imprima o comprimento da string.
# c) Imprima a string em letras maiúsculas.
# d) Imprima a string em letras minúsculas.

var_frase = "Hello World"

print(f"Comprimento da string: {len(var_frase)}") #espaco tambem conta
print(f"String em caracteres Maiusculo: {var_frase.upper()}")
print(f"String em caracteres Minusculo: {var_frase.lower()}")


#________________________________________________________________________________________________________
# Exercício 3: Manipulação de listas
# a) Declare uma lista com alguns números.
# b) Adicione um número ao final da lista.
# c) Remova um número da lista.
# d) Imprima o último elemento da lista.

lista_numeros = [1, 2, 3, 4, 5]
print(f"Lista originial: {lista_numeros}")

lista_numeros.append(6)
lista_numeros.remove(1) # passa como argumento o numero que quer remover
print(f"Lista atualizada: {lista_numeros}")


#Em uma lista, os índices começam do 0 para o primeiro elemento, 1 para o 
#segundo, e assim por diante. Se você usar um índice negativo, Python conta a 
#partir do final da lista, sendo -1 o último elemento, -2 o penúltimo, e assim 
#por diante.

print(f"O último numero da lista atualizada é: {lista_numeros[-1]}")


#____________________________________________________________________________________________________________
# Exercício 4: Verificação de número par ou ímpar
# a) Declare uma variável 'numero' e atribua um número a ela.
# b) Use uma instrução 'if' para verificar se o número é par ou ímpar.
# c) Imprima uma mensagem indicando se o número é par ou ímpar.

var_numero = int(input("Digite um numero: ")) # a funcao input retorna uma string mesmo digitando um numero

if var_numero % 2 == 0 :
  print(f"Eh par")
else:
  print(f"Eh impar")


#_______________________________________________________________________________________
# Exercício 5: Verificação de número positivo, negativo ou zero
# a) Declare uma variável 'valor' e atribua um número a ela.
# b) Use uma instrução 'if', 'elif' e 'else' para verificar se o número é positivo, negativo ou zero.
# c) Imprima uma mensagem indicando a natureza do número.

var_valor = int(input("Digite um numero: "))

if var_valor > 0:
  print(f"Numero positivo")
elif var_valor == 0:
  print(f"Numero zero")
else:
  print(f"Numero negativo")
  
  
#___________________________________________________________________________________
# Exercício 6: Classificação de idade
# a) Declare uma variável 'idade' e atribua um valor a ela.
# b) Use instruções 'if' e 'elif' para classificar a idade em categorias como "criança", "adolescente", "adulto" e "idoso".
# c) Imprima a categoria correspondente à idade.

var_idade = float(input("Qual a sua idade em anos? "))

if var_idade < 1:
  print(f"Voce eh um baby")
elif var_idade >= 1 and var_idade < 13:
  print(f"Voce eh crianca") 
elif var_idade >= 13 and var_idade < 20:
  print(f"Voce eh adolescente")
elif var_idade >= 20 and var_idade < 60:
  print(f"Voce eh adulto")
else:
  print(f"Voce eh Idoso")
  
'''
#________________________________________________________________________________
# Exercício 7: Soma com loop for
# a) Crie um loop 'for' que soma os números de 1 a 10.
# b) Imprima o resultado.

var_soma = 0
for i in range(1,11):
  var_soma += i
print(f"O valor da soma eh: {var_soma}")


#________________________________________________________________________________
# Exercício 8: Contagem regressiva com loop while
# a) Crie um loop 'while' que conta regressivamente de 10 até 1.
# b) Imprima cada número durante a contagem regressiva.

var_time = 10
while var_time >= 1:
  print(f"{var_time}")
  var_time -= 1

#________________________________________________________________________________
# Exercício 9: Tabuada com loop for
# a) Solicite ao usuário que digite um número.
# b) Use um loop 'for' para imprimir a tabuada desse número, de 1 a 10.

var_num = int(input("Digite um número: "))
i = 1
for i in range(1,11):
  print(f"{var_num} X {i} = {i * var_num}")
  
  
# Exercício 10: Adivinhe o número com loop while
# a) Escolha um número aleatório entre 1 e 10.
# b) Peça ao usuário para adivinhar o número.
# c) Use um loop 'while' para continuar pedindo ao usuário até que ele acerte.

import random
numero_secreto = random.randint(1, 10)
chute = 0
tentativa = 0
while numero_secreto != chute:
  chute = int(input("Chute um valor entre (1,10)"))
  tentativa +=1
print(f"Parabéns! Você acertou em {tentativa} tentativas. O número era {numero_secreto}.")