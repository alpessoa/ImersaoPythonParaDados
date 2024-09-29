#Funções

def saudacao():#Criando a função sem argumento
    print("Olá, Seja bem vindo!") 

saudacao()#executando a função

def hello(nome):#função com arrgumento
    print(f"Olá {nome}!")

hello("André")

def somar(a, b):
    return a + " " + b

print(somar("André","Pessoa"))

def imc(peso, altura):
    return round(peso / altura **2 , 2)

print(imc(103,1.94))

def imc2():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em cm: "))

    return round(peso/(altura/100) ** 2, 2)

print(imc2())