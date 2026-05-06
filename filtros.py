from db_config import get_connection

def juego_ano(year):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT titulo, precio, fechaSalida FROM juegos WHERE fechaSalida = %s"
    cursor.execute(query, (year,))

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results


def juego_clasificacion(year):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT titulo, precio, fechaSalida FROM juegos WHERE fechaSalida = %s"
    cursor.execute(query, (year,))

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results
