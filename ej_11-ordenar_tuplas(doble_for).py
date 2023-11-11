'''
Hacer un programa que ordene una lista de tuplas. 
Cada tupla tiene dos elementos.
La lista debe quedar ordenada de mayor a menor en función del valor
del segundo elemento de cada tupla.

'''
# tuplas testigo
a = (1, 4)
b = (2, 5)
c = (5, 3)
d = (7, 2)

# las listo
list1 = [(1, 4), (2, 5), (5, 3), (7, 2)]
print (list1)
# las mido
y = len(list1)
print(len(list1))
pos = 1
for i in range(0, y):
    for j in range(0, y-i-1):
        if (list1[j][pos] > list1[j + 1][pos]):
            temp = list1[j]
            list1[j]= list1[j + 1]
            list1[j + 1]= temp
print(list1)