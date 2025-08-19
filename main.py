from api import get_weather

def main():
    city = input("Enter a city name: ")
    result = get_weather(city)

    if result:
        print(f"Weather in {city}: {result['weather']}")
        print(f"Temperature: {result['temperature']}°C")
    else:
        print("Error getting weather data. Please check the city name.")

if __name__ == "__main__":
    main()
