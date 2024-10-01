# Programa que calcula el promedio de notas de los alumnos

# Función para calcular el promedio de las notas
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Solicitar la cantidad de alumnos
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

# Crear una lista para almacenar la información de los alumnos
alumnos = []

# Recolectar la información para cada alumno
for i in range(cantidad_alumnos):
    print(f"\nAlumno {i + 1}")
    
    # Solicitar datos del alumno
    nombre = input("Ingrese el nombre del alumno: ")
    genero = input("Ingrese el género del alumno (M/F): ")
    
    # Solicitar las notas
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))
    
    # Calcular el promedio
    promedio = calcular_promedio([nota1, nota2, nota3])
    
    # Almacenar la información en un diccionario
    alumno_info = {
        'Nombre': nombre,
        'Género': genero,
        'Notas': [nota1, nota2, nota3],
        'Promedio': promedio
    }
    
    # Añadir la información del alumno a la lista
    alumnos.append(alumno_info)

# Mostrar la información de todos los alumnos
print("\nResumen de los alumnos:")
for alumno in alumnos:
    print(f"\nNombre: {alumno['Nombre']}")
    print(f"Género: {alumno['Género']}")
    print(f"Notas: {alumno['Notas']}")
    print(f"Promedio: {alumno['Promedio']:.2f}")