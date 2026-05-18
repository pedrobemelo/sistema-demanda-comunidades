import requests


def get_weather(city="Cruzeiro"):
    url = "https://api.open-meteo.com/v1/forecast?latitude=-22.57&longitude=-44.97&current_weather=true"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return "Clima indisponível"

        data = response.json()

        temperature = data["current_weather"]["temperature"]
        windspeed = data["current_weather"]["windspeed"]

        return f"{temperature}°C | Vento: {windspeed} km/h"

    except Exception:
        return "Clima indisponível"