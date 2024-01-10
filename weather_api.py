import requests # a python library to handle api interactions
import time # python library to fetch current time 

# OpenWeatherMap API - Access weather data.
def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key}
    response = requests.get(base_url, params=params)
    data = response.json()
    return data["main"]["temp"]

# JokeAPI - Fetch jokes.
def get_joke():
    base_url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(base_url)
    joke_data = response.json()
    # get info from setup and display it.
    return joke_data

# check for presence of setup in the JokeAPI payload with a maximum of three loops over a 5s interval
def get_valid_joke_setup(max_attempts=3, timeout_seconds=5):
    attempts = 0


    while attempts < max_attempts:
        start_time = time.time()
        joke_data = get_joke()

        try:
            joke_setup = joke_data['setup']
            return joke_setup, joke_data["delivery"]
        except KeyError:
            pass

        elapsed_time = time.time() - start_time
        if elapsed_time < timeout_seconds:
            time.sleep(timeout_seconds - elapsed_time)
        
        attempts += 1

    return "Joke not available", None



def main():
    # The actual weather API key
    openweathermap_api_key = '4bd8979f1e011f3be1dda4122e4a411c' 


# Converting the temperature from Kelvin to celsius
    city = input("Enter the city for weather information: ").capitalize() #returns the city name in proper 
    temperature_k = get_weather(openweathermap_api_key, city)
    temperature_c = temperature_k - 273.15
    print(f"\nCurrent temperature in {city}: {temperature_c} °C\n")

    msg = "The current temperature at {location} is {temp}".format(
    location = city,
    temp = temperature_c
     )
    with open('weather.txt', 'a') as text_file:
      text_file.write(msg + '\n')

# prompt user to get their interest in hearing a joke after checking the weather
    if temperature_c > 25:
        print("Would you like to hear a joke to cool off?")
        resp = (input("Yes / No: ")).upper()
        if resp == "YES":
            print(get_valid_joke_setup())
        else:
            print("Thank you for checking the weather.")
    
    else:
        print("Would you like to hear a joke to warm up?")
        resp = (input("Yes / No: ")).upper()
        if resp == "YES":
            print(get_valid_joke_setup())
        else:
            print("Thank you for checking the weather.")



if __name__ == "__main__":
    main()
