# Ingresar números en una lista hasta que se intruduzca un cero.
# Muestrar los números en las posiciones par de la lista.
# Mostrar los números en orden inverso a como fueron ingresados.
# Dividir la lista en dos, sin importar si una lista queda con cantidad impar de elementos y mostarlas.
# Mostrar todos los elementos de la primera mitad, exceptuando el primero y el último.
# Mostrar el máximo y el mínimo de la segunda mitad.

lesta = []
print("Ingrese una lista de números. Termine con 0 (cero).")
x = ()
while x != 0:
    x = int(input(">> "))
    lesta.append(x)
lesta.pop()
d =len(lesta) # Calculo el largo de la lista
print(f'La lista ingresada es: {(lesta)} y tiene {d} elementos.')


#Obtengo los indices para las posiciones pares y creo la lista:
list = []
for x in range(0, d):
    if x % 2 == 0:
        list.append(x)
listp = []
for n in (list):
    listp.append(lesta[n])
listp.pop(0)
print(f'La sublista con los elementos en las posiciones pares es:{(listp)}')


primera_mitad = []  # La primer mitad va a contener los elementos desde 0 a 'd//2'.
for i in range (d//2):
    primera_mitad.append(lesta[i])
print (f'La primera mitad de la lista es:{primera_mitad}')

segunda_mitad = []  # La segunda mitad va a contener elementos desde 'd//2' hasta 'd'.
for n in range (d//2, d):
    segunda_mitad.append(lesta[n])
print(f'La segunda mitad de la lista es: {segunda_mitad}')

m = lesta
lesta.reverse()
print(f'La lista en orden inverso a como fueron ingresados es:{m}')

# Muestre por pantalla todos los elementos de la primera mitad, exceptuando el primero y el último.
primera_mitad.pop(0)
primera_mitad.pop(-1)
print(f'La primera mitad sin el primer y último elemento es:{primera_mitad}')

# Muestre por pantalla el máximo y el mínimo de la segunda mitad.
segunda_mitad.sort()
print(f'El mínimo valor de la segunda mitad es {segunda_mitad[0]} y el máximo {segunda_mitad[-1]}.')
print("That\' all, folks!")