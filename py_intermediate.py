
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
# dict: dicionários em Python
#       --> usar {} ou a classe dict para criar um dicionário!
# métodos dunder : começam com __ 
#       --> implementar comportamento padrão de objetos /
#           operadores e built-ins.



# métodos de dict: 

#   --> len - quantas chaves
#   --> keys - iterável com as chaves
#   --> values - iterável com os valores
#   --> items - iterável com as chaves e valotes
#   --> setdefault - adiciona valor se a chave não existe
#   --> copy - retorna uma cópia rasa (shallow copy)|(valores imutaveis)
#   --> get - obtém uma chave
#   --> pop - apaga um item acom a chave especificada (del)
#   --> popitem - apaga o último item adicionado
#   --> update - atualiza um dicionário com outro



# cores!: 

# verde: \033[32m
# azul: \033[34m
# vermelho: \033[31m
# magenta: \033[95m

# \033[0m --- colocar no final para cor não manter





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


# Exercicio com função:
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


# Higher Order Functions:

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


# Exercicio com função 2:
"""
def aumenta(num):
    resposta = []
    for i in range(4):
        resultado = num * i
        resposta.append(resultado)
    return resposta
    
print(aumenta(5))""" # outra versão


"""
def duplica(num):
    resposta = num * 2
    return resposta

def triplica(num):
    resposta = num * 3
    return resposta

def quadriplica(num):
    resposta = num * 4
    return resposta

num_escolhido = int(input("digite um número inteiro: "))

while True: 
    opcao = int(input("(1) - sair | (2) - x2 | (3) - x3 | (4) - x4: "))
    if opcao == 1:
        print("adeus!")
        break
    if opcao == 2:
        print(duplica(num_escolhido))
        continue
    if opcao == 3:
        print(triplica(num_escolhido))
        continue
    if opcao == 4:
        print(quadriplica(num_escolhido))
        continue"""


# Introdução ao tipo de dados dict: 

"""pessoa = {
    "nome": "Elson",
    "profissão": "Enfermeiro",
    "idade": 40,
    "altura": 1.8,
    "endereços": [
        {"rua": "tal tal", "número": 79},
        {"rua": "tal tal 2", "número": 99}
    ]
}

print(f"\033[32m{pessoa['profissão']} {pessoa['nome']}") # verde
print()

for chave in pessoa: 
    print(chave, ":", pessoa[chave])"""


# Manipulando chaves e valores em dicionários Python (dict): 

"""pessoa = {}

chave_1  = "nome"
chave_2 = "sobrenome"
pessoa[chave_1] = "Jorge"
pessoa[chave_2] = "Silvinha"

print(pessoa)
print(pessoa[chave_1]) 
print(pessoa[chave_2]) """


# Métodos úteis nos dicionários Python - PT 1 (dict):
"""
pessoa = {
    "nome": "Jorge",
    "sobrenome": "Silvinha",
}

print(len(pessoa))
print(list(pessoa.keys())) # tem como chamar a posição, tipo [0]
print(list(pessoa.items())) # tem tuplas interna

for chave, valor in pessoa.items():
    print(chave, valor)

pessoa.setdefault("idade", 12) # criando chave idade
print(pessoa["idade"])"""


# Shallow Copy vs Deep Copy (copy)

"""import copy

d1 = {
    "c1": 1,
    "c2": 2,
    "l1": [0,1,2] # valor mutavel não muda com copia rasa

}
d2 = d1.copy() # copia rasa (não precisa do import)
d2 = copy.deepcopy(d1) # copia profunda (precisa do import)

d2["c1"] = 1000
d2["l1"][1] = 999999

print(d1)
print(d2)"""


# Métodos úteis nos dicionários Python - PT 2 (dict):
"""
pessoa = {
    "nome": "Jorge",
    "sobrenome": "Silvinha",
    "idade": 12,
}

print(pessoa["nome"])
print(pessoa.get("nome", None))

nome = pessoa.pop("nome") 
print(pessoa)

ultima_chave = pessoa.popitem()
print(pessoa)

pessoa.update({
    "idade": 22, # modifica, pois já existe
    "profissao": "Enfermeiro" # adiciona pois não existe

})
print(pessoa)

pessoa.update(profissao="Papazete", idade=27) # Update pode ser assim tbm
print(pessoa)"""


# Exercicio - sistema de perguntas e respostas: 
"""
perguntas = [
    {
        "pergunta": "quanto é 2+2?",
        "opcoes": ["1","2","3","4"],
        "resposta": "4"
    },
    {
        "pergunta": "quanto é 3+5?",
        "opcoes": ["4","5","8","9"],
        "resposta": "8"
    },
    {
        "pergunta": "quanto é 3+3?",
        "opcoes": ["2","4","6","8"],
        "resposta": "6"
    }    
]

i = 0
acertos = 0
while i < len(perguntas): 
    print("Pergunta:", perguntas[i]["pergunta"])

    for indice, opcao in enumerate(perguntas[i]["opcoes"]):
        print(f"{indice})", opcao)

    resposta = (input("digite a resposta: "))
    if resposta == perguntas[i]["resposta"]:
        print("\033[32mCorreto!\033[0m\n")
        acertos+=1
    else: 
        print("\033[31mErrado!\033[0m\n")
    i+=1


print(f"você acertou {acertos} pergunta(s)!")"""



