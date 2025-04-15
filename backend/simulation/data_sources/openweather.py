from decouple import config
from security import safe_requests


def obtener_datos_climaticos(lat, lon):
    """Esta funcion realiza una solicitud a la API de OpenWeatherMap para obtener
    los datos climaticos actuales de una ubicacion especifica basada en su
    latitud y longitud.

    Parametros:

    lat (float): La latitud de la ubicacion para la cual se desea obtener los datos climaticos.
    lon (float): La longitud de la ubicacion para la cual se desea obtener los datos climaticos.

    Retorno:

    dict: Un diccionario que contiene dos claves:
    'temperatura': Un valor float que representa la temperatura actual en grados Celsius.
    'descripcion': Un string que describe las condiciones climaticas actuales en español.
    Si la solicitud a la API falla (status code diferente de 200), la funcion retorna None.

    -----------------------------------------------------------------------------------------------
    Consideraciones:
    Es necesario contar con una clave API valida de OpenWeatherMap para que la funcion funcione correctamente.
    La unidad de temperatura devuelta es en grados Celsius, y la descripcion del clima esta en espanol.
    La URL de la solicitud excluye datos minuciosos, horarios, diarios y alertas para enfocarse solo en las condiciones actuales.
    """
    api_key = config("WEATHER_KEY")

    base_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={api_key}&units=metric&lang=es"
    response = safe_requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        return {
            "temperatura": data["current"]["temp"],
            "descripcion": data["current"]["weather"][0]["description"],
            "humedad": data["current"]["humidity"],
        }
    else:
        return {"error": f"API error: {response.status_code}"}
