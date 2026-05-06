## Esto es ejemplo nomas

from db_config import get_connection

conn = get_connection()
cursor = conn.cursor()

def usuario(user_id):

    query = """
            SELECT * FROM usuarios
            WHERE id = %s
            """

    cursor.execute(query, (user_id,))
    user = cursor.fetchone()

    if user:
        print(f"ID: {user[0]}")
        print(f"Nombre: {user[1]}")
        print(f"Correo: {user[2]}")
        print(f"Password: {user[3]}")
        print(f"Fecha de creación: {user[4]}")
        print(f"País: {user[5]}")
    else:
        print("Usuario no encontrado")


def juego(game_id):

    query = """
            SELECT * FROM juegos
            WHERE id = %s
            """

    cursor.execute(query, (user_id,))
    user = cursor.fetchone()

    if user:
        print(f"ID: {user[0]}")
        print(f"Nombre: {user[1]}")
        print(f"Correo: {user[2]}")
        print(f"Password: {user[3]}")
        print(f"Fecha de creación: {user[4]}")
        print(f"País: {user[5]}")
    else:
        print("Usuario no encontrado")







cursor.close()
conn.close()