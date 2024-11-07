def burbuja(arreglo):
    n = len(arreglo)
    for i in range(n-1):
        swap = False
        for j in range(n-i-1):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                swap = True
        if swap == False:
            break
    return arreglo

def sueldo_v():
    while True:
        try:
            sueldo = int(input("Ingrese sueldo: "))
            if sueldo == 0:
                return None
            elif sueldo < 0:
                print("El sueldo no puede ser negativo.")
            else:
                return sueldo
        except ValueError:
            print("Ingrese un número.")

sueldo = []
nombre = []

while True:
    respuesta_sueldo = sueldo_v()
    if respuesta_sueldo is None:
        break
    sueldo.append(respuesta_sueldo)
    print("")
    nombre.append(input("Ingrese nombre: "))
    print("")


sueldo = burbuja(sueldo)
print("Sueldos ordenados de menor a mayor:")
for i in range(len(sueldo)):
    print(sueldo[i])
