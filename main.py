
import requests
import os

# API endpoint and key setup
weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
print(f"API key: {os.environ.get('OWM_API_KEY')}")

if not api_key:
    raise EnvironmentError("API key not found. Please set the 'OWM_API_KEY' environment variable.")

# Weather parameters
weather_parameters = {
    "lat": 30.311150,
    "lon": 97.942749,
    "appid": api_key,
    "cnt": 4,
}

try:
    # API request
    response = requests.get(weather_endpoint, params=weather_parameters)
    response.raise_for_status()
    weather_data = response.json()

    # Rain detection
    will_rain = False
    for hour_data in weather_data["list"]:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            will_rain = True
            break  # Exit loop early if rain is detected

    # Output the result
    if will_rain:
        print("It will rain in the next forecast periods.")
    else:
        print("No rain expected in the next forecast periods.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching weather data: {e}")

if will_rain:
    print("Bring an Umbrella.")