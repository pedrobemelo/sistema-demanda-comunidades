from src.weather import get_weather


def test_get_weather():
    result = get_weather()

    assert isinstance(result, str)
    assert "°C" in result