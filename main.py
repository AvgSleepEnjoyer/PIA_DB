import dao

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

def mostrarUsuario():
    