#Haz un programa que pida por teclado un número entero N entre 10 y 20.
#Después, muestra por pantalla todos los números enteros entre 1 y N y finalmente
#muestra por pantalla todos los números enteros entre el 30 y el N, en orden inverso.
list = []
num=int(input("Ingrese un número N entre 10 y 20: "))
num = num + 1
for i in range (1, int(num)): #for i in range(int(num)):
    list.append(i)
print("")
print(f"Esta es la lista de enteros hasta {num-1}:")
print(list)
print("")
print(f"Esta es la lista de enteros desde {num-1} hasta 30:")
list2 = []
num = num - 1
for i in range (int(num), 31):
    list2.append(i)
print(list2)
list2.sort(reverse=True) #reverse
print("")
print("Y esta es la lista anterior, pero invertida:")
print(list2)