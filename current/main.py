# Importa la librería datetime para manejar fechas y horas, así como funciones personalizadas de otros módulos
import datetime as dt
from weather_data import get_current_weather, get_historical_weather
from database import create_table, insert_data, get_statistics
from plot_generator import plot_temperature_and_humidity, plot_statistics
from alerts import check_alerts

# Configuración de la API de OpenWeatherMap para obtener datos actuales
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read()  # Lee la clave de la API desde un archivo
CITY = "Olavarría"  # Nombre de la localidad deseada
LAT = 36.8927  # Latitud de la ubicación deseada
LON = 60.3225  # Longitud de la ubicación deseada

# Función principal del programa
def main():
    # Obtener datos meteorológicos actuales
    current_weather = get_current_weather(CITY, API_KEY)

    if current_weather:
        # Procesar y mostrar los datos meteorológicos actuales
        temp_celsius, feels_like_celsius, humidity, wind_speed, description, sunrise_time, sunset_time = current_weather
        print(f"Temperatura en {CITY}: {temp_celsius:.2f}ºC")
        print(f"Sensación térmica en {CITY}: {feels_like_celsius:.2f}ºC")
        print(f"Humedad en {CITY}: {humidity}%")
        print(f"Velocidad del viento en {CITY}: {wind_speed}m/s")
        print(f"Clima general en {CITY}: {description}")
        print(f"Amanece en {CITY} a las: {sunrise_time} hora local")
        print(f"Anochece en {CITY:} a las {sunset_time} hora local")
    else:
        print("No se pudieron obtener datos meteorológicos actuales.")

    # Obtener datos meteorológicos históricos
    start_date = "2023-10-27"
    end_date = "2023-10-29"
    start_datetime = dt.datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = dt.datetime.strptime(end_date, "%Y-%m-%d")
    start_unix = int(start_datetime.timestamp())
    end_unix = int(end_datetime.timestamp())

    historical_data = get_historical_weather(LAT, LON, start_unix, end_unix, API_KEY)

    if historical_data:
        # Procesar y mostrar la temperatura promedio de los datos históricos
        average_temperature = sum(historical_data) / len(historical_data)
        print(f"Temperatura promedio en {CITY} desde {start_date} hasta {end_date}: {average_temperature:.2f}ºC")
    else:
        print("No se encontraron datos históricos en la respuesta JSON.")

    # Crear la tabla en la base de datos
    create_table()

    # Insertar datos en la base de datos
    if current_weather:
        # Realizar una limpieza de datos para manejar valores faltantes o atípicos
        temp_celsius = max(min(temp_celsius, 40), -20)
        feels_like_celsius = max(min(feels_like_celsius, 40), -20)
        humidity = max(min(humidity, 100), 0)
        wind_speed = max(min(wind_speed, 100), 0)

        insert_data(CITY, dt.datetime.now(), temp_celsius, feels_like_celsius, humidity, wind_speed, description, sunrise_time, sunset_time)
    else:
        print("No se pudieron insertar datos en la base de datos debido a la falta de datos actuales.")

    # Verificar alertas automáticamente
    check_alerts()  # Llama a la función check_alerts con los datos actuales y se imprimirá el alerta en caso de corresponder

# Esta condición verifica si el archivo se está ejecutando directamente y no como un módulo
if __name__ == "__main__":
    main()  # Llama a la función principal si el archivo se ejecuta directamente

    # Después de que main() haya terminado, se podrá llamar a get_statistics
    promedio_temperatura, humedad_acumulada, velocidad_promedio_viento = get_statistics()

    # Luego, se podrá imprimir o utilizar las estadísticas como se prefiera
    print(f"Temperatura promedio: {promedio_temperatura:.2f}°C")
    print(f"Humedad acumulada: {humedad_acumulada}%")
    print(f"Velocidad promedio del viento: {velocidad_promedio_viento:.2f} m/s")

    fechas, temperaturas, humedades = get_statistics()

    # Después de que main() haya terminado y se hayan obtenido las estadísticas, se podrá generar el gráfico correspondiente
    plot_temperature_and_humidity(fechas, temperaturas, humedades)

    # Obtener datos meteorológicos actuales
    current_weather = get_current_weather(CITY, API_KEY)

    if current_weather:
        temp_celsius, feels_like_celsius, humidity, wind_speed, _, _, _ = current_weather

        # Se llama a la función para mostrar el tablero de monitoreo
        plot_statistics(temp_celsius, humidity, promedio_temperatura, humedad_acumulada)