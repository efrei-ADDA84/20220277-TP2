# importing requests and json
import os
import requests

def get_weather(API_KEY, LAT, LONG):
    # URL definition
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={API_KEY}"

    # HTTP request
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("--> ${}".format(e))

    # JSON response
    if response.status_code == 200:
    # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        city = data['name']
        temperature = main['temp']
        feels_like = main['feels_like']
        temp_min = main['temp_min']
        temp_max = main['temp_max']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']

        print("\n************************************************************\n")
        print("*****               ANISOFT WEATHER API                *****\n")
        print("************************************************************\n")
        print(f"--> City: {city}")
        print(f"--> Temperature: {temperature}")
        print(f"--> Feels lilke: {feels_like}")
        print(f"--> Temperature Min: {temp_min}")
        print(f"--> Temperature Max: {temp_max}")
        print(f"--> Humidity: {humidity}")
        print(f"--> Pressure: {pressure}")
        print(f"--> Weather Report: {report[0]['description']}")
    else:
        # showing the error message
        print("-> Error in the HTTP request")

if __name__ == "__main__":
    # URL parameters definition
    API_KEY = os.environ.get("API_KEY")
    LAT = os.environ.get("LAT")
    LONG = os.environ.get("LONG")
    if API_KEY is None or LAT is None or LONG is None:
        print("--> Missing parameters")
    else:
        get_weather(API_KEY, LAT, LONG)