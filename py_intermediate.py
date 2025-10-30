
# observações:

# Refatorar: editar o código
# Usar return! não é comum dar prints em funções! 
# 0 = Falsy
# *args:
#       --> Empacotamento e desempacotamento
#       --> Dentro de uma tupla
#       --> Passa quantidade ilimitada de argumentos não nomeados
# Higher Order Functions: 
#       --> função que pode receber outras funções como argumentos /
# ou retornar uma função como resultado




# def - função personalizada
...
"""def frutas():
    print("fruta1")
    print("fruta2")
    print("fruta3")

frutas()"""

...
"""def imprimir(a,b,c):
    print(a,b,c)

imprimir(1,2,3)
imprimir(4,5,6)"""

...
"""def saudacao(nome="Sem nome"):
    print(f"Olá, {nome}!")

saudacao("Enfermeiro Elson")
saudacao() # se eu não passar o valor"""

...
"""def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 6)"""


# argumentos nomeados e não nomeados (posicionais)
"""
def soma(x,y):
    print(f"{x=} {y=} | x+y={x+y}")

soma(8,9) # posicional
soma(y=5, x=2) # nomeado"""


# valores padrão para os parâmetros:
"""
def soma(x,y,z=None): #None é o parâmetro
    if z is not None:
        print(f"{x=} {y=} {z=} | x+y+z:{x+y+z}")
        print("com z!")
    else:
        print(f"{x=} {y=} | x+y:{x+y}")
        print("sem z!")

soma(2,6)
soma(3,5,9)"""


# Escopo de funções e módulos:
"""
x = 10

def escopo():
    x=1     # só posso utilizar dentro da def!
    print(x)

    def soma(y):
        print(f"soma: {x+y}")

    soma(2)


escopo()
print(f"x de fora: {x}") 
# o x de fora não é o mesmo que o de dentro!"""


# retorno das funções (return):

"""def soma(x,y):
    if x > 10:
        return 10 # os dois vão ser literal 10
    return x + y

soma1 = soma(8,3)
soma2 = soma(2,4)
print(soma1+soma2)"""


# *args para quantidade de argumentos
...
"""x, y, *args= 1,2,3,4
print(x,y,args)"""

...
"""def soma (*args):
    args = list(args) # originalmente tupla, agora list
    print(args, type(args))
    
soma(1,2,3,4)"""

...
"""def soma (*args): 
    total = 0
    for numero in args:
        total += numero
    return total

soma_num = soma(1,2,3)
print(soma_num)"""

...
"""def soma(*args):
    return sum(args)

soma_total = soma(4,5,6)
print(soma_total)

numeros = 10,25,30,45,50
outra_soma = soma(*numeros) # empacotar 
print(outra_soma)"""


# Exercicios com função
...
"""def ex1(*args):
    resultado = 1 # vc não pode começar a multiplicar por 0
    for num in args:
        resultado *= num
    return resultado

print(ex1(1,4,5,6))"""

...
"""def ex2(num):
    multiplo_de_dois = num % 2 == 0

    if multiplo_de_dois:    
        return "Par!"
    return "Impar!"

num_escolhido = int(input("Número: "))
print(ex2(num_escolhido))"""


# Higher Order Functions

"""def saudacao(msg, nome):
    return f"{msg}, {nome}" 

def executa(funcao, *args): # funcao = saudacao | args = bom dia, jorge
    return funcao(*args)

variavel = executa(saudacao, "Bom dia", "Jorge")
print(variavel)"""


# Closure e funções que retornam outras funções:

"""def  criar_saudacao(saudacao):
    def saudar(nome):
            return f"{saudacao}, {nome}"
    return saudar

falar_bom_dia = criar_saudacao("Bom dia")
falar_boa_noite = criar_saudacao("Boa noite")

for nome in ["Jorge", "Rogerio", "Elson"]:
      print(falar_bom_dia(nome))
      print(falar_boa_noite(nome))"""


# Exercicios com função 2:

aaa