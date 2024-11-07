# Programa Votaciones
# Crear un programa para una elección presidencial
# Tiene 2 candidatos (candidato AZUL, candidato ROJO)
# Se ingresan votantes hasta ingresar el nombre X
# Para cada votante se debe ingresar:
# NOMBRE
# APELLIDO
# GÉNERO (validar género)
# EDAD (validar edad mayor 18 años)
# CIUDAD SEDE DE VOTACIÓN
#LUGAR (COLEGIO O ESTADIO) DE VOTACIÓN
# Indicar quién ganó las elecciones
# y fue elegido presidente
# Calcular los votos obtenidos por AZUL
# Calcular los votos obtenidos por ROJO


def es_genero_valido(genero):
    return genero.lower() in ['masculino', 'femenino']

def es_edad_valida(edad):
    return edad >= 18

def pedir_datos_votante():
    while True:
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")

        while True:
            genero = input("Ingrese su género (masculino/femenino): ").lower()
            if es_genero_valido(genero):
                break
            print("Género no válido. Por favor, ingrese 'masculino' o 'femenino'.")

        while True:
            try:
                edad = int(input("Ingrese su edad: "))
                if es_edad_valida(edad):
                    break
                else:
                    print("Debe tener al menos 18 años para votar.")
            except ValueError:
                print("Por favor, ingrese una edad válida.")

        ciudad = input("Ingrese la ciudad de votación: ")
        lugar = input("Ingrese el lugar de votación (colegio/estadio): ")

        return nombre, apellido, genero, edad, ciudad, lugar

def main():
    votos_azul = 0
    votos_rojo = 0

    while True:
        print("\n--- Votación Presidencial ---")
        nombre_votante = input("Ingrese su nombre para votar (o 'X' para salir): ").strip()
        if nombre_votante.lower() == 'x':
            break


        nombre, apellido, genero, edad, ciudad, lugar = pedir_datos_votante()


        while True:
            candidato = input("¿Por quién desea votar? (AZUL/ROJO): ").upper()
            if candidato == 'AZUL':
                votos_azul += 1
                print("¡Gracias por votar por el Candidato AZUL!")
                break
            elif candidato == 'ROJO':
                votos_rojo += 1
                print("¡Gracias por votar por el Candidato ROJO!")
                break
            else:
                print("Opción no válida. Por favor, elija 'AZUL' o 'ROJO'.")


    print("\n--- Resultado de la Elección ---")
    print(f"Votos Candidato AZUL: {votos_azul}")
    print(f"Votos Candidato ROJO: {votos_rojo}")

    if votos_azul > votos_rojo:
        print("\nEl Candidato AZUL es el elegido presidente.")
    elif votos_azul < votos_rojo:
        print("\nEl Candidato ROJO es el elegido presidente.")
    else:
        print("\nLa elección ha terminado en empate.")

if __name__ == "__main__":
    main()
