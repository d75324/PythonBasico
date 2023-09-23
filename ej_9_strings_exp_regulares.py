import re

# Escribir una función que reciba una cadena de texto por parámetro y que devuelva la suma de todos los
# números que haya en esa cadena. Por ejemplo: para la cadena de texto:
# "Tengo 5 gatos con 4 patas cada uno. Uno tiene 12 años." debería devolver el número 21.
cad = "Tengo 5 gatos con 4 patas cada uno. Uno tiene 12 años."
print (cad)

def func():
    re3 = re.findall(r'\d{2}|\d', cad)
    n = []
    for i in re3:
        i = int(i)
        n.append(i)
    f = sum(n)
    return f

func()
y = func()
print (f'La suma de todos los números que aparecen en la frase es {y}.\nThat\'s all, folks! ')
