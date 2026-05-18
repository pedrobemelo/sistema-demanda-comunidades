import requests


def get_weather(city="Cruzeiro"):
    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        return "Não foi possível obter clima."

    data = response.json()

    temp = data["current_condition"][0]["temp_C"]
    desc = data["current_condition"][0]["weatherDesc"][0]["value"]

    return f"{temp}°C - {desc}"