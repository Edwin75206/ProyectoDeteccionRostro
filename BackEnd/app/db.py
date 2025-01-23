import mysql.connector
from config import DATABASE_CONFIG

def get_db_connection():
    """Conecta a la base de datos y devuelve la conexión"""
    try:
        connection = mysql.connector.connect(**DATABASE_CONFIG)
        print("Conexión exitosa a la base de datos")
        return connection
    except mysql.connector.Error as err:
        print(f"Error al conectar con la base de datos: {err}")
        return None

def test_connection():
    connection = get_db_connection()
    if connection:
        print("¡Conexión exitosa a la base de datos!")
        connection.close()
    else:
        print("Error al conectar a la base de datos.")

if __name__ == "__main__":
    test_connection()