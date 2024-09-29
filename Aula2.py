#Manipulando Strings

texto = "Estou aprendendo Python."
print(texto[0]) #indexação sempre começa em zero
print(texto[0:-7])
print(texto.split())
print(texto.upper()) #texto maiusculo
print(texto.lower()) #texto minusculo
print(texto.capitalize()) #primeira letra em maiusculo
print(texto.title())#todas as primeiras letras em maiusculo

frase = texto.replace("Python", "dados") #substituição de texto
print(frase)

print("Python" in texto)
print("dados" in frase)