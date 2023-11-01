# Importa la librería sqlite3 para trabajar con bases de datos SQLite
import sqlite3

# Función para crear una tabla en la base de datos
def create_table():
    # Conecta a la base de datos (o la crea si no existe) y obtiene un cursor que le permite operar con ésta
    conn = sqlite3.connect('datos_meteorologicos.db')
    cursor = conn.cursor()

    # Consulta SQL para verificar si la tabla ya existe
    table_check_query = "SELECT name FROM sqlite_master WHERE type='table' AND name='datos_meteorologicos'"
    cursor.execute(table_check_query)
    table_exists = cursor.fetchone()

    if not table_exists:
        # Si la tabla no existe, entonces la creamos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS datos_meteorologicos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  # Campo ID autoincremental
                ciudad TEXT,  # Ciudad
                fecha DATETIME,  # Fecha y hora
                temp_celsius REAL,  # Temperatura en grados Celsius
                feels_like_celsius REAL,  # Sensación térmica en grados Celsius
                humidity INTEGER,  # Humedad en porcentaje
                wind_speed REAL,  # Velocidad del viento en m/h
                description TEXT,  # Descripción del clima
                sunrise_time DATETIME,  # Hora de amanecer
                sunset_time DATETIME  # Hora de anochecer
            )
        ''')

    # Guarda los cambios en la base de datos y cierra la conexión
    conn.commit()
    conn.close()

# Función para insertar datos en la tabla de la base de datos
def insert_data(city, fecha, temp_celsius, feels_like_celsius, humidity, wind_speed, description, sunrise_time, sunset_time):
    # Conecta a la base de datos y obtiene un cursor
    conn = sqlite3.connect('datos_meteorologicos.db')
    cursor = conn.cursor()

    # Ejecuta una consulta SQL para insertar datos en la tabla
    cursor.execute("INSERT INTO datos_meteorologicos (ciudad, fecha, temp_celsius, feels_like_celsius, humidity, wind_speed, description, sunrise_time, sunset_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (city, fecha, temp_celsius, feels_like_celsius, humidity, wind_speed, description, sunrise_time, sunset_time))

    # Guarda los cambios en la base de datos y cierra la conexión
    conn.commit()
    conn.close()

def get_statistics():
    # Conectar a la base de datos
    conn = sqlite3.connect('datos_meteorologicos.db')
    cursor = conn.cursor()

    # Calcular la temperatura promedio
    cursor.execute("SELECT AVG(temp_celsius) FROM datos_meteorologicos")
    promedio_temperatura = cursor.fetchone()[0]

    # Calcular la humedad acumulada
    cursor.execute("SELECT SUM(humidity) FROM datos_meteorologicos")
    humedad_acumulada = cursor.fetchone()[0]

    # Calcular la velocidad promedio del viento
    cursor.execute("SELECT AVG(wind_speed) FROM datos_meteorologicos")
    velocidad_promedio_viento = cursor.fetchone()[0]

    # Cerrar la conexión a la base de datos
    conn.close()

    return promedio_temperatura, humedad_acumulada, velocidad_promedio_viento
