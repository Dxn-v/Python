#Crear un programa que ingrese 3 de notas para cada alumno
#Ingresar la cantidad de alumnos del curso
#Para cada alumno debe ingresar:
#nombre
#genero
#notas (nota 1, nota 2, nota 3)
#Calcular promedio para cada alumno
#Calcular cuantas mujeres hay en el curso
#Calcular el promedio de los hombres

def promedio (a,b,c):
    prom = (a + b + c)/3
    return prom 

print ("Welcome to thye python")
print ("")

cont_m = 0
cont_f = 0

ca = int(input("Ingrese cantidad de alumnos:"))

for i in range (0,ca,1):
    nombre = input("Ingrese nombre del alumno")
    genero = input("""Ingrese genero del alumno
    1 <- si es MASCULINO
    2 <- si es FEMENINO """)
    print("Ingrese notas:")
    nota1 = float(input("NOTA 1: "))
    nota2 = float(input("NOTA 2: "))
    nota3 = float(input("NOTA 3: "))

    if(genero==("Femenino")):
        cont_f = cont_f + 1
        print("Es mujer")
    else:
        cont_m = cont_m + 1
        print("es hombre")

        prom=promedio(nota1,nota2,nota3)
        print("El promedio del alumno es: " ,prom)

#Respuestas
print("La cantidad de mujeres es " ,cont_f)
print("El promedio del alumno es: " ,prom)




