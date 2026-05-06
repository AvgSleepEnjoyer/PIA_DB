import dao
## Menu de prueba 


def menu():
    while True:
        print("\n--- Menu DE PRUEBA ---")
        print("1. Insertar")
        print("2. Listar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            dao.insertar(nombre, edad)
        
        
        
        elif opcion == "2":
            dao.listar()
        
        
        
        elif opcion == "3":
            id_p = int(input("ID a actualizar: "))
            nombre = input("Nuevo nombre: ")
            edad = int(input("Nueva edad: "))
            dao.actualizar(id_p, nombre, edad)
        
        
        
        elif opcion == "4":
            id_p = int(input("ID a eliminar: "))
            dao.eliminar(id_p)
        
        
        
        elif opcion == "5":
            print("Saliendo...")
            break
        
        
        
        else:
            print("Opción inválida")



def menu():
    opcion = 0
    print("""
        \t\tBASE DE DATOS: STEAM-SEQUEL\n
        \t1. Mostrar catalogo\n
        \t2. Registrar nuevo juego\n
        \t3. Mostrar usuarios\n
        \t4. Salir\n
    """)
    input(opcion)
    return opcion;



def mostrarCatalogo():
    print("""
        \t\tMostrar por:
        \t1.Clasificacion\n
        \t2.Titulo\n
        \t3.Precio\n
        \t4.Fecha de salida\n

    """)