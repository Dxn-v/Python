# Arreglos
# Ingresar N personajs para un show en la Pampilla (N ingresado por teclado)
# Ingresar por personaje lo siguiente: 
# NOMBRE (Ej: Gary)
# APODO (Ej: Medel)
# SUELDO (rango entre $1.000.000 y $17.000.000)
# FECHA (las opciones son: 17 Septiembre, 18 Sept, 19 Sept, 20 Sept)
# Calcular promedio, y nombre completo (FUNCIONES)
# Mostrar el mas artista que mas se le paga

def validar_nota():
    nota = 0 # Inicialmente fuera del rango deseado 
    while ((nota < 1) or (nota > 7)):
        try:
            nota = float(input("Ingrese nota del alumno: "))
            if nota < 1:
                print("Nota muy pequeña, debe ser mayor o igual que 1.0... Intentelo de nuevo.")
            if nota > 7:
                print("Nota muy grande, dene ser menor o igual a 7.0... Intentelo de nuevo")
        except ValueError:
                print("Debe escribir la nota como numero decimal")
        print("")
    return nota 


def validar_sueldo():
    sueldo = 0 # Inicialmente fuera del rango deseado
    while ((sueldo < 1000000) or (sueldo > 17000000)):
        try:
            sueldo = int(input("Ingrese sueldo del artista: "))
            if sueldo < 1000000:
                print("Sueldo muy bajo, debe ser mayor o igual que 1000000 Intentelo de nuevo. ")
            if sueldo > 17000000:
              print("Sueldo muy alto, debe ser mejor o igual que 17000000 Intentelo de nuevo. ")
        except ValueError:
            print("Debe escribir el sueldo como entero")
        print("")

def validar_dia():
    dias_validos = ["17-09", "18-09", "19-09", "20-09"]
    
    while True:
        dia = input("Introduce fecha del show (17-09, 18-09, 19-09, 20-09)")

        if dia in dias_validos:
          print(f"Fecha {dia} validada correctamente")
          print("")
          return dia
        else:
            print("Opcion no valida. por favor, intenta de nuevo ") 

def validar_positivo(numero):
    if numero > 0:
        return True
    else:
        return False
    
# Arreglos o Arrays
nombre = []
apellido = []
apodo = []
dia = []
sueldo = []

# Iniciar

print("Bienvenido a la PAMPILLA INSUCO")
print("")

n = int(input("Ingrese cantidad de artistas: "))
print("")