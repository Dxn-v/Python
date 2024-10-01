# Realizar un programa en Python que solucione la siguente
# Problematica:   VENTAS DE FRUTAS Y VERDURAS
#                 Ingrese por teclado la cantidad de ventas a realizar
#                 Cada venta debe registrar:
# NOMBRE DEL VENDEDOR
# APELLIDO DEL VENDEDOR
# NOMBRE DEL CLIENTE
# APELLIDO DEL CLIENTE
# CANTIDAD QUE VA A COMPRAR EL CLIENTE (EN KGS OSEA KILOGRAMOS)
# FRUTA QUE VA A COMPRAR EL USUARIO
# PRECIO DE LA FRUTA O VERDURA (EN PESOS CHILENOS, POR KILO)
# CON CUANTO PAGO EL CLIENTE
# FUNCION: CALCULAR TOTAL A PAGAR
# FUNCION: CALCULAR VUELTO
# FUNCION: CALCULAR NOMBRE COMPLETO


def calcular_total_a_pagar(cantidad, precio_kilo):
    """Calcula el total a pagar por la compra."""
    return cantidad * precio_kilo

def calcular_vuelto(total_a_pagar, monto_pagado):
    """Calcula el vuelto que debe dar el vendedor al cliente."""
    return monto_pagado - total_a_pagar

def obtener_nombre_completo(nombre, apellido):
    """Obtiene el nombre completo combinando nombre y apellido."""
    return f"{nombre} {apellido}"

def main():
    # Solicitar la cantidad de ventas
    cantidad_ventas = int(input("Ingrese la cantidad de ventas a realizar: "))
    
    # Inicializar una lista para almacenar los registros de ventas
    ventas = []
    
    for _ in range(cantidad_ventas):
        # Recopilar información de cada venta
        nombre_vendedor = input("Nombre del vendedor: ")
        apellido_vendedor = input("Apellido del vendedor: ")
        nombre_cliente = input("Nombre del cliente: ")
        apellido_cliente = input("Apellido del cliente: ")
        cantidad = float(input("Cantidad que va a comprar el cliente (en kgs): "))
        fruta = input("Fruta que va a comprar el cliente: ")
        precio_por_kilo = float(input("Precio de la fruta o verdura (en pesos chilenos por kilo): "))
        monto_pagado = float(input("Con cuánto pagó el cliente: "))
        
        # Calcular el total a pagar y el vuelto
        total_a_pagar = calcular_total_a_pagar(cantidad, precio_por_kilo)
        vuelto = calcular_vuelto(total_a_pagar, monto_pagado)
        
        # Guardar el registro de la venta
        venta = {
            "nombre_vendedor": nombre_vendedor,
            "apellido_vendedor": apellido_vendedor,
            "nombre_cliente": nombre_cliente,
            "apellido_cliente": apellido_cliente,
            "cantidad": cantidad,
            "fruta": fruta,
            "precio_por_kilo": precio_por_kilo,
            "monto_pagado": monto_pagado,
            "total_a_pagar": total_a_pagar,
            "vuelto": vuelto
        }
        ventas.append(venta)
        
        # Mostrar la información de la venta
        print("\nInformación de la venta:")
        print(f"Nombre completo del vendedor: {obtener_nombre_completo(nombre_vendedor, apellido_vendedor)}")
        print(f"Nombre completo del cliente: {obtener_nombre_completo(nombre_cliente, apellido_cliente)}")
        print(f"Fruta comprada: {fruta}")
        print(f"Cantidad comprada (kgs): {cantidad}")
        print(f"Precio por kilo: {precio_por_kilo} CLP")
        print(f"Total a pagar: {total_a_pagar} CLP")
        print(f"Monto pagado: {monto_pagado} CLP")
        print(f"Vuelto: {vuelto} CLP")
        print("\n" + "="*30 + "\n")
    
    # Opcional: mostrar resumen de todas las ventas
    print("\nResumen de todas las ventas:")
    for venta in ventas:
        print(f"Nombre del vendedor: {obtener_nombre_completo(venta['nombre_vendedor'], venta['apellido_vendedor'])}")
        print(f"Nombre del cliente: {obtener_nombre_completo(venta['nombre_cliente'], venta['apellido_cliente'])}")
        print(f"Fruta: {venta['fruta']}")
        print(f"Cantidad (kgs): {venta['cantidad']}")
        print(f"Precio por kilo: {venta['precio_por_kilo']} CLP")
        print(f"Total a pagar: {venta['total_a_pagar']} CLP")
        print(f"Vuelto: {venta['vuelto']} CLP")
        print("-" * 30)

if __name__ == "__main__":
    main()