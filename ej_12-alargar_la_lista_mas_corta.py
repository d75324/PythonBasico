# Ejercicio: dadas dos listas f1 y f2 con formadas por numeros enteros, completar la lista menor,
# hasta que las dos queden del mismo largo.
# Si son iguales, no pasa naranja.

f2 = [9,9,9,9,9,9,9,7,7,7,7,7,7,7]
f1 = [3,3,3,3]

def alargar_la_lista_mas_corta():

    if len(f1) > len(f2):
        relleno = [0]
        m = len(f1) - len(f2)
        while m != 0:
            f2.extend(relleno)
            m = m - 1
        lista_alargada = f2

    else:
        relleno = [0]
        m = len(f2) - len(f1)
        while m != 0:
            f1.extend(relleno)
            m = m - 1
        lista_alargada = f1

    return lista_alargada

resultado = alargar_la_lista_mas_corta()
print(resultado)