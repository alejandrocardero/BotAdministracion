# db_manager.py
import os
import psycopg2
from dotenv import load_dotenv

# --- CONFIGURACIÓN Y CONEXIÓN ---

# Cargar las variables de entorno del archivo .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# --- FUNCIONES DE GESTIÓN DE LA BASE DE DATOS ---

def setup_database():
    """
    Intenta establecer una conexión con la base de datos para verificar
    que las credenciales y el servidor sean válidos.
    """
    if not DATABASE_URL:
        print("ERROR: La variable de entorno DATABASE_URL no está configurada.")
        return False
        
    conn = None
    try:
        # Añadimos un tiempo de espera de 15 segundos para dar margen a la conexión VPN
        conn = psycopg2.connect(DATABASE_URL, connect_timeout=15) 
        
        # Si la conexión es exitosa, cierra la conexión de prueba
        conn.close()
        return True
        
    except psycopg2.OperationalError as e:
        print(f"ERROR: Fallo al conectar a la Base de Datos. Detalle: {e}")
        return False
    except Exception as e:
        print(f"ERROR: Fallo inesperado durante la conexión. Detalle: {e}")
        return False

def execute_query(query, params=None, fetch=False):
    """
    Establece la conexión y ejecuta una consulta SQL.
    
    :param query: La consulta SQL a ejecutar.
    :param params: Tupla de parámetros para la consulta (para prevenir inyección SQL).
    :param fetch: Si es True, obtiene los resultados (SELECT). Si es False (INSERT/UPDATE/DELETE).
    :return: Los resultados de la consulta si fetch=True, o True/False si fetch=False.
    """
    conn = None
    try:
        # Reabrir la conexión para la operación
        conn = psycopg2.connect(DATABASE_URL, connect_timeout=15)
        cur = conn.cursor()
        
        cur.execute(query, params)
        
        if fetch:
            results = cur.fetchall()
            return results
        else:
            conn.commit() # Confirmar cambios (INSERT, UPDATE, DELETE)
            return True
            
    except psycopg2.OperationalError as e:
        # Esto incluye errores de autenticación, timeout y fallos de conexión
        print(f"ERROR de conexión durante la ejecución de la consulta: {e}")
        return None if fetch else False
    except Exception as e:
        # Otros errores (ej. sintaxis SQL incorrecta, tabla inexistente)
        print(f"ERROR al ejecutar la consulta: {e}")
        return None if fetch else False
        
    finally:
        if conn:
            conn.close()

def fetch_data(query, params=None):
    """ Función auxiliar para obtener datos (SELECT) """
    return execute_query(query, params, fetch=True)

# También necesitas tener esta función para insertar o actualizar datos (aunque no la usaremos aún)
def insert_update_data(query, params=None):
    """ Función auxiliar para modificar datos (INSERT, UPDATE, DELETE) """
    return execute_query(query, params, fetch=False)

# --- ESTRUCTURA DE TABLAS INICIALES ---

def create_initial_tables():
    """
    Crea las tablas necesarias si no existen.
    
    NOTA: Las hemos creado manualmente en Neon, pero es bueno tener la lógica aquí.
    """
    queries = [
        """
        CREATE TABLE IF NOT EXISTS tiendas_suscriptores (
            telegram_id BIGINT PRIMARY KEY,
            tienda_nombre VARCHAR(255) NOT NULL,
            fecha_vencimiento DATE,
            es_admin BOOLEAN DEFAULT FALSE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS datos_inventario (
            id SERIAL PRIMARY KEY,
            telegram_id BIGINT REFERENCES tiendas_suscriptores(telegram_id),
            producto_nombre VARCHAR(255) NOT NULL,
            cantidad INT NOT NULL,
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    ]
    
    for query in queries:
        execute_query(query)
        
# Puedes descomentar y llamar a create_initial_tables() si necesitas que Python cree las tablas