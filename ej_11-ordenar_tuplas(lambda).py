# Hacer un programa que ordene una lista de tuplas. Cada tupla tiene dos elementos.
# La lista debe quedar ordenada de mayor a menor por el segundo elemento de cada tupla.

a = (1, 4)
b = (2, 5)
c = (5, 3)
d = (7, 2)

list1 = [(1, 4), (2, 5), (5, 3), (7, 2)]
print(list1)
l = len(list1)
print(l)

print(sorted(list1, key=lambda tupla: tupla[1]))