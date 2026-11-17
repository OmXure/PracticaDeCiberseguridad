from nodoArbolC import Incidente, ArbolBinarioBusqueda


def main():
    arbol = ArbolBinarioBusqueda()

    # Ponemos los 7 incidentes iniciales del documento
    datos = [
        Incidente(150, "192.168.1.25", "Fuerza bruta", "En investigacion", "Alto"),
        Incidente(100, "192.168.1.30", "Malware", "Pendiente", "Critico"),
        Incidente(200, "10.0.0.15", "Escaneo de puertos", "Resuelto", "Medio"),
        Incidente(75, "192.168.1.45", "Phishing", "En investigacion", "Alto"),
        Incidente(125, "10.0.0.20", "Acceso no autorizado", "Pendiente", "Critico"),
        Incidente(175, "192.168.1.80", "Ransomware", "En investigacion", "Critico"),
        Incidente(250, "10.0.0.50", "Denegacion de servicio", "Resuelto", "Alto")
    ]



# Los inserte de esta manera ya que eran "predeterminados"
    for item in datos:
        arbol.insertar(item)

    while True:
        print("\n--- MENU DE INCIDENTES ---")
        print("1. Registrar incidente")
        print("2. Visualizar arbol")
        print("3. Mostrar recorridos")
        print("4. Buscar incidente por ID")
        print("5. Contar incidentes")
        print("6. Mostrar menor y mayor")
        print("7. Probar ID duplicado (150)")
        print("8. Buscar por nivel de riesgo")
        print("9. Salir")

        op = input("Elige una opcion: ")

        if op == "1":
            try:
                nid = int(input("Ingresa el ID: "))
                ip = input("Ingresa la IP: ")
                ataque = input("Ingresa el tipo de ataque: ")
                estado = input("Ingresa el estado: ")
                riesgo = input("Ingresa el nivel de riesgo: ")
                arbol.insertar(Incidente(nid, ip, ataque, estado, riesgo))
            except ValueError:
                print("Error: El ID debe ser un numero.")

        elif op == "2":
            print("\n--- ARBOL BINARIO ---")
            if arbol.isEmpty():
                print("El arbol esta vacio.")
            else:
                arbol.imprimirArbol()

        elif op == "3":
            if arbol.isEmpty():
                print("El arbol esta vacio.")
            else:
                print("\nRECORRIDOS:")
                print("Inorden:   ", end="")
                arbol.recorridoInorden()
                print("Preorden:  ", end="")
                arbol.recorridoPreorden()
                print("Postorden: ", end="")
                arbol.recorridoPostorden()

        elif op == "4":
            try:
                val = int(input("Ingresa el ID a buscar: "))
                res = arbol.buscar(val)
                if res:
                    print(f"\nResultado obtenido:\n{res}")
                else:
                    print(f"\nEl incidente con ID {val} no fue encontrado.")
            except ValueError:
                print("Error: Ingresa un numero valido.")

        elif op == "5":
            total = arbol.contarNodos()
            print(f"\nCantidad de incidentes encontrados: {total}")

        elif op == "6":
            print("\n--- EXTREMOS ---")
            menor = arbol.obtenerMenor()
            mayor = arbol.obtenerMayor()
            print(f"Menor: {menor}")
            print(f"Mayor: {mayor}")

        elif op == "7":
            print("\n--- PROBANDO DUPLICADO ---")
            duplicado = Incidente(150, "192.168.1.99", "Spoofing", "Pendiente", "Alto")
            arbol.insertar(duplicado)

        elif op == "8":
            nivel = input("Ingresa el nivel de riesgo (ej. Critico): ")
            lista = arbol.buscarPorNivelRiesgo(nivel)
            print(f"\nIncidentes encontrados: {len(lista)}")
            for x in lista:
                print(f" -> ID: {x.id} | {x.ataque} | Riesgo: {x.riesgo}")

        elif op == "9":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()