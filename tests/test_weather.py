from unittest.mock import patch
from src.weather import get_weather


@patch("src.weather.requests.get")
def test_get_weather(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "current_weather": {
            "temperature": 25,
            "windspeed": 10
        }
    }

    result = get_weather()

    assert "25" in result
    assert "Vento" in result