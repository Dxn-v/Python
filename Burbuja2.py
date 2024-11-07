

def calcpond(leng, mate, nem):
    return (mate * 0.5) + (leng * 0.3) + (nem * 0.2)

def burbuja(alum):
    n = len(alum)
    for i in range(n):
        for j in range(0, n-i-1):
            if alum[j][2] < alum[j+1][2]:
                alum[j], alum[j+1] = alum[j+1], alum[j]

def main():
    print("Hola, bienvenido al programa de acceso a la Universidad Catolica Del Norte")
    print("")

    alum = []

    for i in range(1, 3):
        nom = input(f"Ingrese el nombre del alumno {i} postulando a Ingeniería en Informática: ")
        ap = input(f"Ingrese el apellido del alumno {i} postulando a Ingeniería en Informática: ")
        
        # Ingreso y validación de puntajes
        while True:
            try:
                leng = float(input("Ingrese el puntaje obtenido en la PAES de Lenguaje (0-1000): "))
                mate = float(input("Ingrese el puntaje obtenido en la PAES de Matemáticas (0-1000): "))
                nem = float(input("Ingrese el NEM obtenido por el Alumno en enseñanza media (0-1000): "))
                if 0 <= leng <= 1000 and 0 <= mate <= 1000 and 0 <= nem <= 1000:
                    break
                else:
                    print("Ingrese un puntaje valido entre 0 y 1000.")
            except ValueError:
                print("Ingrese valores numéricos válidos.")
        
        prom = calcpond(leng, mate, nem)
        alum.append((nom, ap, prom))

    burbuja(alum)

   
    print("\nAlumnos seleccionados:")
    for i in range(min(22, len(alum))):
        nom, ap, prom = alum[i]
        print(f"{i + 1}. {nom} {ap} Con Promedio: {prom:.2f}")

if __name__ == "__main__":
    main()


