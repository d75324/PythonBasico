# Crear una función que genere una lista de N números random acotada entre 0 y 77,
# con N definido por el usuario.
def listaRandom():
    from random import randint
    mer = int(input("Indique la cantidad de elementos de la lista: "))
    lista = []
    while mer != 0:
        fr = randint(1, 77)
        lista.append(fr)
        mer = mer - 1
    #print(lista)
    return lista
y = listaRandom()
print(y)