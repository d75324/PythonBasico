# Ingresar usuarios por nombre, edad y altura en centímetros y mostrar los datos
# en los siguientes 3 formatos:
# 1- El usuario NOMBRE, tiene EDAD años y mide ALTURA centímetros.
# 2- El usuario NOMBRE tiene EDAD años y mide ALTURA centímetros.
# 3- El usuario NOMBRE tiene EDAD años y mide ALT metros y URA centímetros.
print('')
nom=input("Ingrese su nombre: ")
eda=int(input("Ingrese su edad: "))
alt=int(input("Ingrese su altura en centímetros: "))
print('')
print(f'El usuario {nom} tiene {eda} años y mide {alt} centímetros')
altm=alt/100
print('')
print(f'El usuario {nom} tiene {eda} años y mide {altm} metros')
print('')
alt1=alt//100
alt2=int((altm-alt1)*100)
if alt1 > 1:
    print(f'El usuario {nom} tiene {eda} años y mide {alt1} metros y {alt2} centímetros')
elif alt1 < 1:
    print(f'El usuario {nom} tiene {eda} años y mide {alt2} centímetros')
else:
    print(f'El usuario {nom} tiene {eda} años y mide {alt1} metro y {alt2} centímetros')
print('')