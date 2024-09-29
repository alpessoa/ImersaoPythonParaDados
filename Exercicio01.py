#Criarr lista de 1 a 10 e imprima numeros pares

lista = [1,2,3,4,5,6,7,8,9,10]
pares= []
impares = []
for numeros in lista:
    if numeros%2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)

print(pares)
print(impares)

#list()cria uma lista automatica
for i in list(range(1, 11)): #(1 é o start, 11 é o stop, 1 ta oculto mas é o step)
    if i % 2 == 0:
        print(i)