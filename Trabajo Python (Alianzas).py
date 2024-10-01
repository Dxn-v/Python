# Condicional SI
# Ingrese 5 usuarios
# Debe ingresar su nombre y el color de su equipo o alianza
# 3 opciones: ROJO, AZUL Y AMARILLO
# Contar cuantos ROJOS hay
print("Bienvenido al ANIVERSARIO INSUCO")
print("")
# INICIALIZACION DE LA VARIABLE DE LOS AMARILLOS
cont_ama=0
# INICIALIZACION DE LA VARIABLE DE LOS AZULES
cont_azu=0
# INICIALÑIZACION DE LA VARIABLE DE LOS ROJOS
cont_rojo=0
# Ingreso de datos
# USUARIO 1
user1=input(input("Ingrese nombre del usuario 1 "))
color1=input("Ingrese su color de alianza:")
color1=input("1 si es ROJO ")
color1=input("2 si es AZUL ")
color1=input("3 si es AMARILLO ")
if color1=="AMARILLO":
    cont_ama=cont_ama +1

    if color1=="AZUL":
        cont_azu= cont_azu +1

    if color1=="ROJO":
        cont_rojo=cont_rojo+1
# USUARIO 2
user2=input(input("Ingrese nombre del usuario 2 "))
color2=input("Ingrese su color de alianza:")
color2=input("1 si es ROJO ")
color2=input("2 si es AZUL ")
color2=input("3 si es AMARILLO ")
if color2=="AMARILLO":
    cont_ama=cont_ama+1

    if color2=="AZUL":
        cont_azu =cont_azu+1

    if color2=="ROJO":
        cont_rojo=cont_rojo+1
# USUARIO 3
user3=input(input("Ingrese nombre del usuario 3 "))
color3=input("Ingrese su color de alianza:")
color3=input("1 si es ROJO ")
color3=input("2 si es AZUL ")
color3=input("3 si es AMARILLO ")
if color3=="AMARILLO":
    cont_ama=cont_ama+1

    if color2=="AZUL":
        cont_azu=cont_azu+1

    if color2=="ROJO":
        cont_rojo=cont_rojo+1
# USUARIO 4
user4=input(input("Ingrese nombre del usuario 4 "))
color4=input("Ingrese su color de alianza:")
color4=input("1 si es ROJO")
color4=input("2 si es AZUL")
color4=input("3 si es AMARILLO")
if color4=="AMARILLO":
    cont_ama=cont_ama+1

    if color2=="AZUL":
        cont_azu=cont_azu+1

    if color2=="ROJO":
        cont_rojo=cont_rojo+1
# USUARIO 5
user5=input(input("Ingrese nombre del usuario 5 "))
color5=input("Ingrese su color de alianza:")
color5=input("1 si es ROJO ")
color5=input("2 si es AZUL ")
color5=input("3 si es AMARILLO ")
if color4=="AMARILLO":
    cont_ama=cont_ama+1
    if color2=="AZUL":
        cont_azu=cont_azu+1

    if color2=="ROJO":
        cont_rojo=cont_rojo+1
    print("La cantidad de usuarios AMARILLOS es ",cont_ama)
    print("La cantida de usuarios AZULES es ",cont_azu)
    print("La cantidad de usuarios ROJOS es ",cont_rojo)