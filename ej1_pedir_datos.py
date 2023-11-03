# Ingresar usuarios por nombre, edad y altura en centímetros.
# La funcion debe mostrar los datos en una linea con el formato:
# - El usuario NOMBRE tiene EDAD años y mide ALT metros y URA centímetros.
# y contemplar que el Usuario pueda medir mas de 2 metros o menos de 1,
# en cuyo caso el mensaje se deberá ajustar:

def pedir_datos(nom, eda, alt):
    # calculo la altura en metros
    altm = alt / 100

    # por si mide mas de un metro
    alt1 = alt // 100

    # Ajusto el texto de acuerdo a los requerimientos
    # estos son los centímetros
    alt2 = int((altm-alt1)*100)

    if alt1 > 1:
        mensaje_de_salida = (f'El usuario {nom} tiene {eda} años y mide {alt1} metros y {alt2} centímetros')
    elif alt1 < 1:
        mensaje_de_salida = (f'El usuario {nom} tiene {eda} años y mide {alt2} centímetros')
    else:
        mensaje_de_salida = (f'El usuario {nom} tiene {eda} años y mide {alt1} metro y {alt2} centímetros')
    return mensaje_de_salida

nom=input("Ingrese su nombre: ")
eda=int(input("Ingrese su edad: "))
alt=int(input("Ingrese su altura en centímetros: "))

print('')
print(f'{pedir_datos(nom, eda, alt)}')