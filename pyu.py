 
# observações:

# python tem tipagem dinâmica/forte (não precisa declarar)
# c tem tipagem estática/forte (precisa declarar)
# tipos imutaveis: str, int, float, bool
# copiar linha Shift + Alt + Seta
# numero_str.isdigit(): # isdigit: verifica se é um número
# CONSTANTE = "variaveis" que não vão mudar
# \ pode usar pra quebrar linha
# algoritmo: solução criada para determinado problema
# flag: marcar um local
# .is_integer(): verifica se o float não tem parte decimal
# .isalpha(): garante que só tem letras
# .isdigit(): garante que só tem números INTEIROS
#     ---> usar try/except para usar com FLOAT
#     ---> except ValueError: executa somente se houver um erro
# .capitalize(): coloca a primeira letra em maisculo
# .strip(): remove espaços do início e do fim.  (   oi   ) = oi
# .append(): adiciona um item no final de uma lista (array)
# .join(): "*".join(nome) = j*o*r*g*e
# .startswith(): verificação booleana 
# .enumerate(): numerar itens de uma lista
# .count(): conta quantas vezes tal string, lista ou tupla aparecem 
# FUNÇÃO vs MÉTODO: funcao(objeto) || objeto.metodo()  
# SORTED retorna a lista ordenada em ordem crescente
# REVERSE retorna em ordem reversa (nesse caso da maior pra menor)
# com SORT alteramos a propria lista
# .remove, .insert (remove e insere)
# fatiamento = f"{string[0:3]} de {string[4:]}
# built-in: embutido, recursos em python sem precisar importar nada
# ctrl + c: keyboard interrupt
# import.os --> os.system('cls' if os.name == 'nt' else 'clear'): limpa
# eval(expressao): interpreta string  
# if palavra is False // if palavra is None // if palavra is True
# if num in num_permitidos // if num not in num_permitidos
# key: diz que criterio deve ser utilizado para comparação
#     ---> print(max(frase, key=frase.count))
#     ---> funciona com tudo que é iteravel
# range: range(start, stop, step)
# for vs while:
#     ---> FOR: geralmente você sabe o inicio e o fim
#     ---> WHILE: não sei quantas repetições vão ter
# CRUD: Create, Read, Update and Delete
# lista: mutavel || tupla: imutavel

''' 
Docstrings
'''



# inicio
'''
print("eu", "ela", sep=" e ", end=" <3")

print(type(1.1)) # mostra o tipo 

print(10 == 10) # boolean: sim => True 
print(10 == 11) # boolean: não => False 
'''


# conversão de tipos, coerção 
'''
print(int("1"), type(int("1")))
print(int("1") + 1)
print(bool(" ")) # True: String com valor (espaço)
print(bool("")) # False: String vazia
print(str(11)+"b")
'''


# variáveis 
'''
nome_completo = "Isabella Ramos Rocha"
idade = 21
print(nome_completo, idade)
maior_de_idade = idade >= 18
print("Maior?:", maior_de_idade)

altura_cm = 170
altura_m = altura_cm/100
print("altura?:", altura_m)
'''


# operadores 
'''
divisao = 10/3
print(divisao)

divisao_inteira=10//3 # sem casa decimal
print(divisao_inteira)

exponenciacao = 2 ** 10 #2^10
print(exponenciacao)

modulo = 55 % 2 # resto da divisao
print(modulo)
'''


# testando operadores + variaveis 
'''
numero = int(input("num:"))
modulo_teste = numero % 2 
if modulo_teste == 0:
    print("é par") 
else:
    print("é ímpar")
'''


# concatenar 
'''
junta = str(1) +"c" 
a_vezes_dez = "A" * 10
tres_isa = "isa" * 3
print( junta, a_vezes_dez, tres_isa)
'''


# IMC + formatação 
'''
nome = "Isabella"
peso = 73
altura = 1.7
imc = peso / (altura * altura)

linha_de_texto = f"{nome} tem a altura: {altura}, peso: {peso} e imc: {imc:.2f}"
print (linha_de_texto) #f-strings

# :.f (duas casas decimais)
# :,.f (duas casas decimais + virgula)

teste = ... # Ellipsis (geralmente utilizado como placeholder)
'''


# formatação com format 
'''
a = "aa"
b = "bb"
c = 1.1

formato = "a={}, b={}, c={}".format(a,b,c)
# ou
string = "a={0}, a={0}, a={0}, b={1}, c={parametro:.2f}"
formato2 = string.format(a,b, parametro=c)

print(formato)
print(formato2)
'''


# if, elif, else 
'''
entrada = input("entrar ou sair? ")

if entrada == "entrar":
    print("entrou")
elif entrada == "sair":
    print("saiu")
else:
    print("error")
'''


# operadores relacionais (>, <, ==, !=, >= )
'''
primeiro = input("valor 1: ")
segundo = input("valor 2: ")

if primeiro > segundo: 
    print(f"primeiro ({primeiro}) é maior que o segundo ({segundo})")
elif segundo > primeiro:
    print(f"segundo ({segundo}) é maior que o primeiro ({primeiro})")
elif primeiro == segundo:
    print("números iguais")
else:
    print("error")
'''


# operadores lógicos (AND) 
'''
entrada = input("[E] Entrar ou [S] Sair: ")
senha_digitada=input("Digite a senha: ")
senha_permitida="123456"

if entrada=="E" and senha_digitada==senha_permitida:
    print("entrou")
elif entrada=="S":
    print("saiu")
else: 
    print("error")
'''


# avaliação de curto circuito 
'''
print(True and False and True) # False
print(False or 0 or True) # True
print(False or "abc" or True) # vai printar o 1º verdadeiro 
print(bool("")) # False
print(bool(" ")) # True
print(bool(0.1)) # True
print(bool(0.0)) # False
'''


# operadores lógicos (OR) 
'''
pergunta = input("S(sim) ou N(não): ")
numero_selecionado = input("escolha 1 ou 0: ")

if (pergunta == "s" or pergunta == "S") and numero_selecionado == "1":
    print("verdadeiro")
elif (pergunta == "n" or pergunta == "N") and numero_selecionado == "0":
    print("falso")
else: 
    print("erro")

    
senha = input("Senha: ") or "Sem senha"
print (senha)
'''


# operadores lógicos (NOT) 
'''
senha= input("Senha: ")
if senha != "":
    print("senha aceita")
elif not senha: # se não digitar senha
    print("erro")

print(not 1) # false 
print(not 0) # true 
'''


# operadores lógicos (IN & NOT IN) 
'''
nome= ("jorge")
print(nome[3])
print("j" in nome) #true
print("z" in nome) #false

if "o" in nome:
    print("tem letra o")

nome_digitar = input("Digite um nome: ")
encontrar = input("Digite letras para verificar: ").lower()

if encontrar in nome_digitar:
    print(f"{encontrar} tem no nome!")
else:
    print("tem não!")
'''


# interpolação de string com % 
'''
nome = "Roberval"
preco = 100.000
variavel = "%s pagou R$%.2f" % (nome, preco)
print (variavel) 
'''


# formatação com f-strings 
'''
variavel = "teste"
print(f"{variavel}")
print(f"{variavel:>10}")
print(f"{variavel:<10}")
print(f"{variavel:-^10}")
'''


# fatiamento de strings e função len 
'''
variavel = "cuzil"
print(variavel[0:4:2]) #fatiamento [inicio:fim:passo]
print(variavel[:2]) # começo ao indice 2
print(variavel[2:]) # indice 2 ao fim
print(len(variavel[:4])) # checar tamanho
print(variavel[::-1]) # printa ao contrário
'''


# exercicio 1 
"""
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f"{nome}")
    print(nome[::-1])

    if " " in nome:
        print("seu nome tem espaços")
    else:
        print("seu nome não tem espaços")

    print(f"seu nome tem {len(nome)} letras", )
    print(f"a primeira letra do seu nome é: {nome[0]}" )
    print(f"a ultima letra do seu nome é: {nome[-1]}" )
else:
    print("desculpe, você deixou campos vazios")
"""


# try e except para capturar erros 
"""
numero_str = (input("Vou dobrar o número que você digitar: "))
try: 
    print("STR: ", numero_str)
    numero_float = float(numero_str)
    print("FLOAT: ", numero_float)
    print(f"{numero_float:.2f} dobrado é {numero_float * 2:.2f}")
except: 
    print("não é um número")

# captura erros caso ocorram (se for letra pula, se não, printa)
"""


# variaveis, constantes e complexidade de codigo 
"""
velocidade = 61 # velocidade atual do carro
local_carro = 100 # local do carro na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # distancia onde o radar 1 pega

vel_passou_radar_1 = velocidade > RADAR_1

if vel_passou_radar_1:
    print("velocidade passou da maxima do radar 1")

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        vel_passou_radar_1:
    print("carro multado em radar 1")
"""


# id - identidade do valor na memória 
"""
v1 ="a"
v2 ="a"
v3 ="b"
print(id(v1))
print(id(v2))
print(id(v3))
"""


# flag, is, is not, none 
"""
condicao = True
passou_no_if = None # None: não valor

if condicao:
    passou_no_if = True # agora é True
    print("faça algo")
else:
    print("não faça algo")

print(passou_no_if, passou_no_if is None) 
print(passou_no_if, passou_no_if is not None)

if passou_no_if is None: 
    print("não passou no if")
elif passou_no_if is not None:
    print("passou no if")  
"""


# exercicio 2 
"""
num_float= float((input("digite um número inteiro: ")))

if num_float.is_integer():

    if num_float % 2 == 0:
        print("é par")
    else:
        print("é impar")

else:
    print("não é um inteiro")
"""


# exercicio 3 
"""
entrada = (input ("digite a hora em número inteiro: "))

try:
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print("bom dia")
    elif hora >= 12 and hora <= 17:
        print("boa tarde")
    elif hora >=18 and hora <=23:
        print("boa noite")
    else:
        print("horario desconhecido")
except:
    print("erro")
"""


# exercicio 4 
"""
nome_user = input("digite seu nome: ")

if nome_user.isalpha():
    if len(nome_user) <= 4:
        print("nome curto")
    elif len(nome_user) == 5 or len(nome_user) == 6:
        print("nome normal")
    elif len(nome_user) > 6:
        print("nome grande")
else:
    print("erro")
"""


# while e break: 
"""
condicao = True
array_nomes = []

while condicao:
   
    nome = input("nome: ")
    array_nomes.append(nome)
    print(f"o nome '{nome}' adicionado no array!")

    continuar = input("continuar? (S || N): ")

    if continuar.upper().strip() == "S":
        continue
    elif continuar.upper().strip() == "N":
        break
    else: 
        print("erro")

print(array_nomes)  
"""


# while contador < 10:
"""
contador = 0

while contador < 10:
    contador += 1
    print(contador)

print("acabou!")
"""


# exercicio 5
"""
condicao = 1
contador = []

while condicao:

    num_int = int(input("digite um num inteiro: "))
    if num_int != 0:
        print("ok")
        contador.append(num_int)
        
    else:
        qtd = len(contador) 
        soma = sum(contador)
        media = soma / qtd

        print(f"media: {media}, quantidade: {qtd}, soma: {soma}")
        break
"""
 

# while + continue
"""
contador = 0 

while contador <= 10: # pede 10 mas para no 8 (pula o 2,3 e 4)
    contador += 1

    if contador >= 2 and contador <= 4:
        print("kk pulei")
        continue

    print(contador)

    if contador == 8:
        break

print("acabo")

"""


# while + while (laços internos)
"""
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f"{linha}, {coluna}")
        coluna +=1    
    linha +=1
    

print("acabo")
"""


# exercicio - while + while (quadrado 4 por 4 com horizontal em *)
"""
qtd_linhas = 4
qtd_colunas = 4

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        if linha == coluna:     # 1,1 - 2,2 - 3,3 - 4,4
            print("0", end=" ")
        else:
            print("*", end=" ")    # end faz ficar lado a lado
        coluna += 1
    print()  # quebra de linha ao terminar a linha
    linha += 1

print("acabo") 
"""


# exercicio - guiado com while
"""
nome = "Jorge"
tamanho_nome = len(nome)
indice = 0
resultado = ""

while indice < tamanho_nome: 
    resultado += nome[indice]
    resultado += "*"
    indice += 1

print(resultado)

# ou

nome = "Rogerio"
join = "*".join(nome)
print(join)
"""


# exercicio - guiado Calculadora 
"""
while True:
    num1 = input("Enter a number: ")
    operadores_permitidos = "+-/*"
    operador = input("Enter an operator (+, -, *, /): ")
    num2 = input("Enter another number: ")


    # verificando se são números
    try:
        num1_float = float(num1)
        num2_float = float(num2)
    except ValueError:
        print("ERROR! Please enter numbers only!")
        continue


    # verificações de dados
    if len(operador) > 1:
        print("ERROR! Enter only one operator!")
        continue
    elif operador not in operadores_permitidos:
        print("ERROR! Enter only: +, -, / or *")
        continue

    if operador == "/" and num2_float == 0:
        print("ERROR! Division by zero")
        continue


    # cálculos
    if operador == "+":
        resultado = num1_float + num2_float
    elif operador == "-":
        resultado = num1_float - num2_float
    elif operador == "*":
        resultado = num1_float * num2_float
    elif operador == "/":
        resultado = num1_float / num2_float
        
    print(f"{num1_float} {operador} {num2_float} = {resultado}")


    # verificando se o user quer sair
    while True:
        opcao = input("Exit? [yes] or [no]: ").lower()

        if opcao in ["yes", "no"]:
            break
        else:
            print("ERROR! Please type 'yes' or 'no'!")

    if opcao == "yes":
        break
    elif opcao == "no":
        continue"""


# while / else (recurso meio meh)
"""
string = "jorge"

i = 0
while i < len(string):
    letra = string[i]

    if letra == "m":
        break

    print(letra, end= "")
    i+=1

else:
    print("|| não achei a letra")
print("fim")"""


# while - Qual letra apareceu mais vezes na frase?
"""
frase = "multiparadigma".upper()

i = 0

while i < len(frase): # laço de repetição
    
    letras = frase[i]

    print(letras, end="")
    i+=1
    
mais_frequente= max(frase, key=frase.count)
print(f" || {mais_frequente}")"""


# introdução ao for / in
"""
texto = "ibuprofeno"

novo_texto = ""
for letra in texto:
    novo_texto = f"*{letra}"
    print(novo_texto, end = "")"""


# range (start, stop, step) + for
"""F
numeros = range(5, 10, 2)

for numero in numeros:
    print(numero)"""


# __iter__ (cria um iterador) ou iter()
"""
texto = iter("Luiz")
print(texto) # --> endereço na memória"""


# exercicio - for i in range (quadrado 4 por 4)
"""
qtd_linhas = 4
qtd_colunas = 4

for linha in range(1, qtd_linhas + 1):
    for coluna in range(1, qtd_colunas + 1):
            print("*", end=" ")
    print() """


# exercicio - jogo da palavra secreta
"""
palavra_secreta = "teste"
letra_correta = []
i = 0

while i < 8:

    letra_digitada = input("digite uma letra: ")

    if len(letra_digitada) == 1 and letra_digitada.isalpha():
        if letra_digitada in palavra_secreta:
            letra_correta.append(letra_digitada)
            print(f"Tem {letra_digitada}!") 
        else:
            print(f"Tem {letra_digitada} não!")
            i+=1
            print(f"Você gastou {i} de 8 chances!")
            if i == 8:
                print("Você perdeu!")
            continue
    else:
        print("digite apenas uma LETRA!")
        continue
 
    palavra_formada = ""
    for letra in palavra_secreta:
        if letra in letra_correta or letra == "-":
            palavra_formada+=letra  
        else:
            palavra_formada+="*"


    print(palavra_formada)
 
    if "*" not in palavra_formada:
        print("Você ganhou!")
        break"""


# tipo list - listas mutáveis
"""
string = ["hello", "world"]

print (list(string))
"""


# Alterando uma lista - del, append, pop, clear, insert
"""
lista = [10,20,30,40]
print(lista)

lista[2] = 300 # substituir
print(lista)

del lista[2] # remover no indice escolhido
print(lista)

lista.append(50) # adicionar no final da lista
print(lista)

removido = lista.pop() # remover no final ou no indice escolhido
print (lista, "removido:", removido)

lista.insert(1, 5) # adicionar no indice escolhido
print(lista)

lista.clear() # apagar lista
print(lista, "a lista foi limpa!")
"""


# concatenando e estendendo listas
"""
lista_a = [1,2,3]
lista_b = [4,5]

lista_c = lista_a + lista_b 
print(lista_c)

lista_a.extend(lista_b) # estende a lista
print(lista_a)
"""


# list e copy 
"""
nome = "Elson"
salvar_nome = nome
nome = "Roberval"

print(nome)
print(salvar_nome)

lista_a = ["mim", "de", "papai"]
lista_b = lista_a.copy() # salvei o valor de A em B
lista_a[2] = "mamãe"
print(lista_a)
print(lista_b)"""


# for in com tipo list
"""
lista = ["mim", "de", "papai"]
for palavra in lista:
    print(palavra, type(palavra))"""


# exercicio - exiba os índices da lista
"""
lista_a = ["jorge", "roberval", "elson"]
i = 0

while i < len(lista_a):
    for nome in lista_a:
        print(i, nome)
        i += 1
"""


# empacotamento e desempacotamento
"""
nome1, *resto = ["mim","de","papai"]
print(nome1, resto)"""


# tipo tupla (imutavel - não muda valor)

"""nomes = ("jorge", "rogerio", "elson") # tupla
print(nomes[1])
print(nomes)

frutas = ["banana", "uva", "morango"]
frutas = tuple(frutas) # transformar em tupla
print(frutas, type(frutas))
frutas = list(frutas) # trasforma em lista
print(frutas, type(frutas))"""


# enumerate - enumerar valores de iteraveis
"""
frutas = ["banana", "uva", "morango"]
frutas.append("kiwi")
print(frutas)

for indice,fruta in enumerate(frutas):
    print(indice,fruta) # retorna duas variaveis separadas

for fruta in enumerate(frutas):
    print(fruta) # retorna uma tupla"""


# enumerate + startswitch
"""
frutas = ["maçã", "banana", "laranja", "abacaxi"]

for indice, fruta in enumerate(frutas):
    if fruta.startswith('a'):
        print(f"A fruta {fruta} está na posição {indice}")
"""


# exercicio - lista de compras com lista

"""lista = []

while True:

    opcao = int(input("inserir (1) || apagar por nome (2) || apagar por indice (3) || listar (4) || sair (5) :"))

    if opcao == 1:
        item = input("insira o item: ")
        lista.append(item)
    elif opcao == 2: 
        if lista == []:
            print("sua lista já está vazia!")
        else:
            item_removido = input("Que item você gostaria de remover?: ")
            if item_removido in lista:
                lista.remove(item_removido)
            else:
                print("esse item não está na lista!")

    elif opcao == 3:
        indice = int(input("indice a remover: "))
        if 0 <= indice < len(lista):
            lista.pop(indice)
        else:
            print("indice inexistente!")
        
    elif opcao == 4: 
        for indice, item_listado in enumerate(lista):
            print(indice,"-", item_listado)

    
    elif opcao == 5:
        print("adeus!")
        break"""


# listas dentro de listas (iteraveis dentro de iteraveis)
"""
equipes = [
["jorge", "roberval", "maria"],
["rogerio", "elson", "denilson"],
["wanderlei", "richarlison", "pedro"]

]

print(equipes)
print(equipes[2])
print(equipes[1][0])
print(equipes[0][1])

print("||||||||||||||||||||||||")

for i, equipe in enumerate(equipes):
    print(f"equipe completa {i+1}: {equipe}")
    for i, aluno in enumerate(equipe):
        print(f"aluno {i+1}: {aluno}") """


# desempacotamento em chamadas de função
    

            
             
             
             
