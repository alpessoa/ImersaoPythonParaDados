#Dicionarios

#Para criar dicionarios, utilizamos {}

dc = {"Maçã":20, "Banana":10, "Laranja": 15, "Uva":5}
print(dc)

#retornando todas as chaves
print(dc.keys())
#retornando todos os valores
print(dc.values())

dc["Banana"] = 12 #alterando valores
print(dc)
print(dc.get("banana", "Inexistente")) #Verifica se a chave está no dicionario, caso nao exista ele retorna o que inserir no segundo parametro4
dc.setdefault("Limão", 22) #Se a chave nao existe e inclui com o valor passado
print(dc)
