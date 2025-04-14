import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from simulation.data_sources.openweather import obtener_datos_climaticos
from decouple import config


def test_api_key_loaded():
    api_key = config('WEATHER_KEY', default=None)
    assert api_key is not None, "No se cargo la clave API desde .env"


@pytest.mark.parametrize("lat, lon", [(6.2442, -75.5812)])  # Medellin
def test_weather_api_success(lat, lon):
    result = obtener_datos_climaticos(lat, lon)
    assert "temperatura" in result
    assert "descripcion" in result
    assert "humedad" in result


def test_weather_api_failure():
    result = obtener_datos_climaticos(999, 999)  # Coordenadas invalidas
    assert "error" in result