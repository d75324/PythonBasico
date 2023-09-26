print ('')
print ('==============')
print ('Bank of Python')
print ('==============')
print ('')

pinok = 1234

cont = 3 # es el contador de intentos fallidos. Para 4 intentos fallidos,
l = bool(False)

pin = int(input('Ingrese su PIN   '))

if pin == pinok:
    print()
    print('PIN Correcto - Bienvenido!\nThat\'s all, folks!')
else:
    while cont != 0 and l == False:
        pin = int (input ('PIN Incorrecto, inténtelo nuevamente:   '))
        if pin == pinok:
            l = True
            print()
            print('PIN Correcto - Bienvenido!\nThat\'s all, folks!')
        else:
            cont = cont - 1
    else:
        if cont == 0:
            print('')
            print ('Ha superado el límite de intentos.\nConsulte a su ejecutivo de cuenta.\nThat\'s all, folks!')
