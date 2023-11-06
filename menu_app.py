def agregar_compra(compras, valor):
    compras.append(valor)
    print(f"Compra de ${valor:.2f} agregada correctamente.")

def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        print("Compras registradas:")
        for i, compra in enumerate(compras, 1):
            print(f"Compra {i}: ${compra:.2f}")

def mostrar_total(compras):
    total = sum(compras)
    print(f"Total gastado: ${total:.2f}")

def main():
    compras = []
    total_gastado = 0.0

    while True:
        print("Menú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción (1/2/3/4): ")

        if opcion == "1":
            valor = float(input("Ingrese el valor de la compra: $"))
            agregar_compra(compras, valor)
            total_gastado += valor
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(compras)
        elif opcion == "4":
            print("Gracias por usar el programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida (1/2/3/4).")

if __name__ == "__main__":
    main()