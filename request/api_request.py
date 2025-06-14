import requests

# Replace with your own API key from https://www.weatherapi.com/
API_KEY = 'e2c725899629e2a772bb375a904120c3'
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

# Enter the city or location you want to check
city = input("Enter city name: ")

# Create the full URL with parameters
url = f"{BASE_URL}?key={API_KEY}&q={city}"

# Send GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Extract weather information
    location = data['location']['name']
    country = data['location']['country']
    temperature = data['current']['temp_c']
    condition = data['current']['condition']['text']
    
    print(f"Weather in {location}, {country}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {condition}")
else:
    print("Failed to retrieve weather data. Check your city name or API key.")
