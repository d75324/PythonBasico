'''
Escribir una programa que revierta una cadena de palabras
Por ejemplo, la entrada: "Maldición va a ser un día hermoso"
Salida: "hermoso dia un ser a va Maldición"
'''

frase = input("Escriba una frase: ")
list8 = frase.split(' ')
list8.reverse()
frase2 = " ".join(list8)
print('')
print(frase2)
print('')