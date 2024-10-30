import requests

city = input("What city's weather would you like to check:\n")

def get_weather_info(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=608eaca525f4386862d7558e336cae9b"
    response = requests.get(url)

    if response.status_code == 200:
        country_data = response.json()  # Add parentheses here
        print(country_data)
    else:
        print("Unable to retrieve data")

get_weather_info(city)
