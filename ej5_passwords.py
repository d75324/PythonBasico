# Escribir un programa que compruebe la validez de un password introducida por pantalla.
# La password debe cumplir todas estas condiciones para ser válido:
# - Al menos una letra minúscula (a-z) y la menos una mayúscula (A-Z).
# - Al menos un número (0-9).
# - Al menos un símbolo (#, $, /, @).
# - Al menos 10 caracteres de longitud.

passt = str(input("Ingrese la nueva password: "))
#print(f'La password ingresada fue: {passt}')

if len(passt) >= 8: # Si la password tiene mas de 10 dígitos es True y se ejecuta.
    if not passt.isalnum(): # Se fija que tenga solamente números y letras
# Para saber si la cadena x1 tiene una mayúscula y una minúscula:
        x1 = passt
        x2 = x1.lower()
        x3 = x1.upper()
        if x1 == x2:
            print("La cadena debe contener al menos una mayúscula")
        elif x1 == x3:
            print("La cadena debe contener al menos una minúscula")
        else:  # Acá empieza la iteración para ver si hay números.
            valor = bool(False)
            q = len(passt)
            valor = bool(False)
            f = 0
            for i in passt:
                if i.isdigit():
                    valor = True
            if valor != True:
                print("La nueva password debe contener al menos un número")
            else:
                print ("La clave está OK\nThat\'s all, folks!")
    else:
        print("La nueva password debe contener algún simbolo")
else:
    print("La nueva pasword debe conenter al menos 8 dígitos")