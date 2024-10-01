# Crear algoritmo en python que resuelva lo siguiente:
# Ingresar clientes hasta que el estacionamiento este completo
# Ingresar cantidad total de estacionamientos
# Ingresar el nombre del cliente
# ingresar la patente del auto
# Ingresar hora de inicio
# Ingresar hora de salida
# Ingresar valor por hora
# Calcular total a pagar FUNCION
class Cliente: 
    def __init__(self, nombre, patente, hora_inicio, hora_salida, valor_por_hora):
        self.nombre = nombre
        self.patente = patente
        self.hora_inicio = hora_inicio
        self.hora_salida = hora_salida
        self.valor_por_hora = valor_por_hora


    def calcular_total(self):
        duracion_horas = self.hora_salida - self.hora_inicio
        return duracion_horas * self.valor_por_hora
     
    def main():
    # Ingresar cantidad total de estacionamientos
    total_estacionamientos = int(input("Ingrese la cantidad total de estacionamientos: "))
    estacionados = []



while len(estacionados) < total_estacionamientos:
        # Ingresar información del cliente
        nombre = input("Ingrese nombre del cliente: ")
        patente = input("Ingrese patente del auto: ")
        hora_inicio = int(input("Ingrese la hora de inicio : "))
        hora_salida = int(input("Ingrese la hora de salida : "))
        valor_por_hora = float(input("Ingrese valor por hora: "))
        if


