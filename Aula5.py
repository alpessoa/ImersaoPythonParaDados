#Estruturas condicionais:
idade = int(input("Informe sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade <= 65:
    print("Você é adulto.")
else:
    print("Você é idoso.")

nome = input("Digite seu nome: ")

if 10 > 20 or nome == "André":
    print(f"Olá, {nome}!")
else:
    print("Você nao é André.")

#loop

for i in ["Ferrari", "Fusca", "Audi"]:
    print(i)

for i in [1,2,3,4,5]:
    print("Valor", i)
    print(i+2)

for caracter in "Analisando dados com Python":
    print(caracter)

for letra in "Python":
    if letra == "h":
        break #loop interrompido
    print(letra)
    
for letra in "Python":
    if letra == "y":
        continue
    print("Letra",letra)