#Estruturas de dados. 

#1 - Listas: []

animais = ["Gato", "Cachorro", 1, 2, 3]
print(animais)
print(animais[0])
print(type(animais))
animais[0] = "Cavalo" #alterando valores do elemento
print(animais)
animais.remove("Cachorro") #removendo um elemento da lista
print(animais)
animais.pop(0) #removendo pelo indice
print(animais)
animais.append("Cachorro") #adiciona elemento ao final da lista
animais.extend(["Papagaio", "Coruja"]) #adicionando mais de um elemento a lista
print(animais)
animais.insert(0,"Peixe")
print(animais)

lista = [500, 30, 300, 80, 10]

lista.sort()
print(lista) #ordena lista do menor para o maior
lista.sort(reverse=True) #ordena lista do maior para o menor
print(lista)
print(max(lista))
print(min(lista))

lista = [["Cachorro", "Gato", "Peixe"],["Fusca", "Gol", "Captur"],[10,20,30]] #lista aninhada

print(lista[1][0])#o primeiro é sempre a lista e segundo o elemento
print(lista[0][2])

print(len(lista))
print(len(animais))
print(len(lista[0]))

#2 - Tuplas: São imutaveis

tp = ("Banana", "Maçã", 10, 50) #usa-se parenteses como sintaxe
print(type(tp))