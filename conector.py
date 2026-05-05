import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="appjuegos"
    )

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



def get_games_by_year(year):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT titulo, precio, fechaSalida FROM juegos WHERE fechaSalida = %s"
    cursor.execute(query, (year,))

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results


while True:
    respuesta = menu()
        
    if respuesta == 4:
        break