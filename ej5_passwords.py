'''
Escribir una función que compruebe la validez de un password introducida por pantalla.
La password debe cumplir todas estas condiciones para ser válido:
 - Al menos una letra minúscula (a-z) y la menos una mayúscula (A-Z).
 - Al menos un número (0-9).
 - Al menos un símbolo (#, $, /, @).
 - Al menos 8 caracteres de longitud.

NEXT STEP: Agregar un contador que dé al usuario 3 oportunidades para ingresar una clave correcta.
Después después del 3er intento fallido, se verá un mensaje que diga algo del tipo:
'Ha superado el número máximo de intentos.\nPuede volver a intentarlo en 1 hora'
'''

def nueva_password():
    passt = str(input("Ingrese la nueva password: "))
    # resultado:
    global devolucion
    # contamos los intentos que hizo el usuario de ingresar una password válida
    intentos = 0
    if len(passt) >= 8: # Si la password tiene mas de 8 dígitos es True y se ejecuta.
        # Se fija que tenga solamente números y letras.
        # isalnum devuelve True si la cadena esta formada solamente por caracteres alfanumericos (A-Z o 0-9)
        # el condicional va a devolver False si passt NO (not) está formada solamente por alfanuméricos
        if not passt.isalnum():
            # Para saber si la cadena x1 tiene una mayúscula y una minúscula:
            x1 = passt
            ## cambio todo a minuscula ##
            x2 = x1.lower()
            ## cambio todo a mayuscula ##
            x3 = x1.upper()
            # Comparo con las listas originales para ver si hay cambios:
            if x1 == x2:
                devolucion = ("La cadena debe contener al menos una mayúscula", 1)
            # lo mismo ahora para minúsculas
            elif x1 == x3:
                devolucion = ("La cadena debe contener al menos una minúscula", 1)
            else:  # Acá empieza la iteración para ver si hay números.
                valor = bool(False)
                q = len(passt)
                valor = bool(False)
                f = 0
                for i in passt:
                    if i.isdigit():
                        valor = True
                if valor != True:
                    devolucion = ("La nueva password debe contener al menos un número", 1)
                else:
                    devolucion = ("La clave está OK!\nThat\'s all, folks!", 0)
        else:
            devolucion = ("La nueva password debe contener algún simbolo", 1)
    else:
        devolucion = ("La nueva pasword debe conenter al menos 8 dígitos", 1)

    return devolucion


m, n = nueva_password()
print(m)