# Hacer un programa que pida tres números al usuario y muestre por pantalla
# el mínimo, el máximo y que indique si son pares o impares. No usar listas.

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

if a >= b and a >=c:
    mayor = a
    print (f'El mayor es {a}.')
elif b >= c and b >= a:
    mayor = b
    print (f'El mayor es {b}.')
else:
    mayor = c
    print (f'El mayor es {c}.')

if a <= b and a <= c:
    menor = a
    print (f'El menor es {a}.')
elif b <= a and b <= c:
    print (f'El menor es {b}.')
else:
    print (f'El menor es {c}.')

if a%2==0:
    print(f'El número {a} es par')
else: print(f'El número {a} es impar')

if b%2==0:
    print(f'El número {b} es par')
else: print(f'El número {b} es impar')

if c%2==0:
    print(f'El número {c} es par')
else: print(f'El número {c} es impar')

print("That\'s all, folks!")