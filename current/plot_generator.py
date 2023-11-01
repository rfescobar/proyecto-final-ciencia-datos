# Se importa la librería para crear gráficos
import matplotlib.pyplot as plt

# Función para generar un gráfico de temperatura y humedad a lo largo de un período
def plot_temperature_and_humidity(fechas, temperaturas, humedades):
    # Crea una figura para el gráfico con un tamaño de 10x6 pulgadas
    plt.figure(figsize=(10, 6))

    # Grafica la serie de datos de temperaturas con etiqueta 'Temperatura (°C)' y color rojo
    plt.plot(fechas, temperaturas, label='Temperatura (°C)', color='tab:red')

    # Grafica la serie de datos de humedad con etiqueta 'Humedad (%)' y color azul
    plt.plot(fechas, humedades, label='Humedad (%)', color='tab:blue')

    # Etiqueta el eje "x" como 'Fecha' y rota las etiquetas 45 grados para una mejor legibilidad
    plt.xlabel('Fecha')
    plt.xticks(rotation=45)

    # Etiqueta el eje "y" como 'Valores'
    plt.ylabel('Valores')

    # Establece el título del gráfico como 'Evolución de Temperatura y Humedad'
    plt.title('Evolución de Temperatura y Humedad')

    # Muestra una leyenda en la esquina superior izquierda del gráfico
    plt.legend(loc='upper left')

    # Ajusta el diseño del gráfico para evitar superposiciones de elementos
    plt.tight_layout()

    # Muestra el gráfico en la pantalla
    plt.show()


def plot_statistics(temperatura_actual, humedad_actual, promedio_temperatura, humedad_acumulada):
    print("\n=== Tablero de Monitoreo ===")
    print("Últimos datos:")
    print(f"Temperatura actual: {temperatura_actual:.2f}°C")
    print(f"Humedad actual: {humedad_actual:.2f}%")

    print("\nEstadísticas Diarias:")
    print(f"Temperatura promedio: {promedio_temperatura:.2f}°C")
    print(f"Humedad acumulada: {humedad_acumulada:.2f}%")