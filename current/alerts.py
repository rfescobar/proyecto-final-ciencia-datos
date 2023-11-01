import sqlite3

# Función para verificar las alertas
def check_alerts():
    conn = sqlite3.connect('datos_meteorologicos.db')
    cursor = conn.cursor()

    # Obtener los últimos datos registrados en la base de datos
    cursor.execute("SELECT temp_celsius, humidity FROM datos_meteorologicos ORDER BY fecha DESC LIMIT 1")
    latest_data = cursor.fetchone()
    temperatura_actual, humedad_actual = latest_data

    # Verificar alertas de temperatura
    if temperatura_actual > 35:
        print("Alerta: Temperatura muy alta")

    if temperatura_actual < 0:
        print("Alerta: Temperatura muy baja")

    # Verificar alertas de humedad
    if humedad_actual > 90:
        print("Alerta: Humedad alta")

    if humedad_actual < 20:
        print("Alerta: Humedad baja")

    conn.close()

if __name__ == "__main__":
    check_alerts()
