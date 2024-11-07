#Crear un programa de python para Insuco Streaming
#Ingresar N peliculas
#Cada pelicula tiene:
#Nombre, Protagonista, Antagonista, Director, Genero, Año de estreno, Vistas
#Crear una funcion para validar genero
#(Accion, Terror, Comedia, Romance, Infantil)
#Crear otra funcion para validar año (2000 - 2024)
#Mostrar pelicula mas vista
#Mostrar pelicula menos vista
#Calcular promedio de visitas
#Sumar cantidad de peliculas de accion y almacenarlas en un nuevo arreglo
#Se debe implementar arreglo

class Pelicula:
    def __init__(self, nom, prota, antag, dire, genero, año, vistas):
        self.nombre = nom
        self.protagonista = prota
        self.antagonista = antag
        self.director = dire
        self.genero = genero
        self.año_estreno = año
        self.vistas = vistas

def val_gen(gen):
    gen_val = ["Accion", "Terror", "Comedia", "Romance", "Infantil"]
    return gen in gen_val

def val_año(año):
    return 2000 <= año <= 2024

def ing_pel(n):
    pel = []
    for _ in range(n):
        nom = input("Ingrese nombre de la película: ")
        prota = input("Ingrese el protagonista de la película: ")
        antag = input("Ingrese el antagonista de la película: ")
        dire = input("Ingrese el nombre del director: ")

        while True:
            gen = input("Ingrese género de la película (Acción, Terror, Comedia, Romance o Infantil): ")
            if val_gen(gen):
                break
            print("Género inválido, intente otra vez.")

        while True:
            try:
                año_estreno = int(input("Ingrese el año de estreno (2000-2024): "))
                if val_año(año_estreno):
                    break
                print("Año inválido, intente otra vez.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        while True:
            try:
                vistas = int(input("Ingrese la cantidad de vistas: "))
                if vistas >= 0:
                    break
                print("Las vistas no pueden ser negativas, intente otra vez.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        pelicula = Pelicula(nom, prota, antag, dire, gen, año_estreno, vistas)
        pel.append(pelicula)

        print("\n--- Ficha Técnica ---")
        print(f"Nombre: {pelicula.nombre}")
        print(f"Protagonista: {pelicula.protagonista}")
        print(f"Antagonista: {pelicula.antagonista}")
        print(f"Director: {pelicula.director}")
        print(f"Género: {pelicula.genero}")
        print(f"Año de estreno: {pelicula.año_estreno}")
        print(f"Vistas: {pelicula.vistas}")
        print("----------------------")
        
        input("Presione Enter para continuar...") 

    return pel

def pel_mas_vista(pel):
    return max(pel, key=lambda p: p.vistas)

def pel_menos_vista(pel):
    return min(pel, key=lambda p: p.vistas)

def prom_vistas(pel):
    total_vistas = sum(p.vistas for p in pel)
    return total_vistas / len(pel) if pel else 0

def pel_accion(pel):
    return [p for p in pel if p.genero == 'Accion']

def main():
    n = int(input("Ingrese la cantidad de películas: "))
    peliculas = ing_pel(n)

    mas_vista = pel_mas_vista(peliculas)
    menos_vista = pel_menos_vista(peliculas)
    promedio = prom_vistas(peliculas)
    peliculas_accion_lista = pel_accion(peliculas)

    print(f"\nPelícula más vista: {mas_vista.nombre} con {mas_vista.vistas} vistas.")
    print(f"Película menos vista: {menos_vista.nombre} con {menos_vista.vistas} vistas.")
    print(f"Promedio de vistas: {promedio:.2f}")
    print(f"Cantidad de películas de acción: {len(peliculas_accion_lista)}")

if __name__ == "__main__":
    main()