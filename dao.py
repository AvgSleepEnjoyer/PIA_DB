## Esto es ejemplo nomas

from db_config import get_connection

class PersonaDAO:
    def insertar(self, nombre, edad):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO personas (nombre, edad) VALUES (%s, %s)", (nombre, edad))
        conn.commit()
        cursor.close()
        conn.close()

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM personas")
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados

    def actualizar(self, id_persona, nombre, edad):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE personas SET nombre=%s, edad=%s WHERE id=%s", (nombre, edad, id_persona))
        conn.commit()
        cursor.close()
        conn.close()

    def eliminar(self, id_persona):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM personas WHERE id=%s", (id_persona,))
        conn.commit()
        cursor.close()
        conn.close()
