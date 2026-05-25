import requests

def weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a1cfb9017d962d5d5c87d88f39985d73&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        # Showing more weather data
        print("\n------ Weather Report ------")
        print("City:", data["name"])

        print("Temperature:", data["main"]["temp"])

        print("Humidity:", data["main"]["humidity"], "%")
        print("Pressure:", data["main"]["pressure"], "hPa")

        print("Wind Speed:", data["wind"]["speed"], "m/s")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

city = input("Enter name of city: ")
weather_data(city)