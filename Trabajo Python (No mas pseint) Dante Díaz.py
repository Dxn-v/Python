# Condicional SI
# Ingrese 5 usuarios
# Debe ingresar su nombre y el color de su equipo o al
# 3 opciones: ROJO, AZUL Y AMARILLO
# contar cuantos rojos hay

print("Bienvenido al ANIVERSARIO INSUCO")
print("")
cont_rojo=0
cont_azul=0
cont_amarillo=0

# Ingreso de datos

# USUARIO 1
user1 = input(("Ingrese nombre del usuario 1: "))
menu1 = input("1 si es ROJO")
menu1 = input("2 si es AZUL")
menu1 = input("3 si es AMARILLO")
color1 = input("Ingresa color de su alianza (EN MAYUSCULAS): ")




if color1 == "ROJO":
    cont_rojo = cont_rojo + 1

if color1 == "AZUL":
    cont_azul = cont_azul + 1

if color1 == "AMARILLO":
    cont_amarillo = cont_amarillo + 1

# USUARIO 2
user2 = input(("Ingrese nombre del usuario 2: "))
color2 = input("Ingresa color de su alianza (EN MAYUSCULAS): ")
if color2 == "ROJO":
    cont_rojo = cont_rojo + 1

if color2 == "AZUL":
    cont_azul = cont_azul + 1

if color2 == "AMARILLO":
    cont_amarillo = cont_amarillo + 1

# USUARIO 3
user3 = input(("Ingrese nombre del usuario 3: "))
color3 = input("Ingresa color de su alianza (EN MAYUSCULAS): ")

if color3 == "ROJO":
    cont_rojo = cont_rojo + 1

if color3 == "AZUL":
    cont_azul = cont_azul + 1

if color3 == "AMARILLO":
    cont_amarillo = cont_amarillo + 1


print("La cantidad de rojos elegidos son: " , cont_rojo) 
print("")
print("La cantidad de azul elegidos son:" , cont_azul)
print("")
print("La cantidad de amarillo elegidos son:" , cont_amarillo)