import requests

city = input("Enter city: ")

url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
location = requests.get(url).json()["results"][0]

weather_url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={location['latitude']}&longitude={location['longitude']}"
    f"&current=temperature_2m"
)

weather = requests.get(weather_url).json()

print(f"\n{location['name']}, {location['country']}")
print(f"Temperature: {weather['current']['temperature_2m']}°C")