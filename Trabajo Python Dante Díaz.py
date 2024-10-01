# Realizar un programa que de solucion a lo sigt: 
# Ingresar 5 alumons (nombre,apellido, y 3 notas)
# Calcular el promedio del alumno
# Calcular el promedio total del curso
# (Compuesto por estos 5 alumnos)
# Calcular la mejor nota por alumno
# Calcular el mejor promedio

def promedio_curso(n1,n2,n3,n4,n5):
    #variable
    prom = 0
    prom = (n1,n2,n3,n4,n5)/5
    return prom

def promedio_notas(n1,n2,n3,p1,p2,p3):
    # variables locales
    prom = 0
    prom = (p1*n1+p2*n2+p3*n3)/100
    return prom

# Ponderados, que en este caso son CONSTANTES
p1 = 20
p2 = 30
p3= 50

# Notas variables ingresadas por teclado
nota1 = float(input("Ingrese primera nota " ))
nota2 = float(input("Ingrese segunda nota " ))
nota3 = float(input("Ingrese tercera nota " ))

prom = promedio_notas(nota1,nota2,nota3,p1,p2,p3)
print(f"El promedio del alumno es " (prom))
