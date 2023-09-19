from random import randint
def generateListaRandom():
    n = int(input("Ingrese un número N mayor que 7: "))
    lista = []
    for i in range(n-2):
        lista.append(randint(1, 99)) #Genera una lista de N elementos random entre 1 y 99
    r = lista[2]
    s = lista[4]
    lista.insert(5, lista[2])
    lista.insert(7, lista[4]) # Inserto 2 elementos repetidas, la lista queda N + 2
    return lista
lista = generateListaRandom()
print(f'La lista generada es {lista} y tiene {len(lista)} elementos.')
#print(f'Tiene {len(lista)} elementos')
def dividir_lista():
    list_repe = []
    list_sin_repe = []
    for i in lista:
        if lista.count(i) > 1:
            list_sin_repe.append(i)
        else:
            list_repe.append(i)
    return [list_repe, list_sin_repe]
ge, fe = dividir_lista()
print(f'Los elementos que no se repiten son:{ge}')
def repest():
    repes = []
    for i in (fe):
        r = fe.count(i)
        if r > 1 and i not in repes:
            repes.append(i)
    repes.sort()
    print (f'Los elementos repetidos son:{repes}')
repest()
print ('That\'s all, folks!')