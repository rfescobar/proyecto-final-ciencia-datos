# Se importa la librería requests para realizar solicitudes HTTP y datetime para manejar fechas y horas
import requests
import datetime as dt

# URL base de la API de OpenWeatherMap para obtener datos actuales
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Función para convertir la temperatura de Kelvin a Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Función para obtener los datos meteorológicos actuales
def get_current_weather(city, api_key):
    # Construye la URL de la solicitud a la API
    url = BASE_URL + f"q={city}&appid={api_key}"
    # Realiza una solicitud HTTP GET y obtiene la respuesta en formato JSON
    response = requests.get(url).json()

    # Verifica si la respuesta contiene datos válidos
    if 'main' in response and 'temp' in response['main']:
        # Extrae los datos relevantes de la respuesta JSON
        temp_kelvin = response['main']['temp']
        temp_celsius = kelvin_to_celsius(temp_kelvin)
        feels_like_kelvin = response['main']['feels_like']
        feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)
        wind_speed = response['wind']['speed']
        humidity = response['main']['humidity']
        description = response['weather'][0]['description']
        # Calcula la hora de amanecer y anochecer en formato UTC
        sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
        sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
        # Retorna los datos meteorológicos actuales
        return temp_celsius, feels_like_celsius, humidity, wind_speed, description, sunrise_time, sunset_time
    else:
        # Si la respuesta no contiene datos válidos, retorna None
        return None

# URL base de la API de OpenWeatherMap para obtener datos históricos
BASE_URL2 = "https://history.openweathermap.org/data/2.5/history/city?"

# Función para obtener datos meteorológicos históricos
def get_historical_weather(lat, lon, start_unix, end_unix, api_key):
    # Construye la URL de la solicitud a la API de datos históricos
    url = f"{BASE_URL2}lat={lat}&lon={lon}&type=hour&start={start_unix}&end={end_unix}&appid={api_key}"
    # Realiza una solicitud HTTP GET y obtiene la respuesta en formato JSON
    response = requests.get(url).json()

    # Verifica si la respuesta contiene datos históricos
    if 'list' in response:
        # Extrae los datos históricos de la respuesta JSON
        historical_data = response['list']

        # Si -por ejemplo- se desea obtener la temperatura promedio de los datos históricos
        temperatures = [entry['main']['temp'] for entry in historical_data]
        average_temperature = sum(temperatures) / len(temperatures)

        # Retorna la temperatura promedio de los datos históricos
        return average_temperature
    else:
        # Si la respuesta no contiene datos históricos, retorna None
        return None
