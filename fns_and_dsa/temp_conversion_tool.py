FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return  (fahrenheit - 32)*CELSIUS_TO_FAHRENHEIT_FACTOR
def convert_to_fahrenheit(celsius):
    return  (celsius*FAHRENHEIT_TO_CELSIUS_FACTOR) + 32

temperature = float(input("Enter the temperature to convert: "))
ex= input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
if ex == "f":
    print(temperature,"°F is " , convert_to_celsius(temperature),"°C")
elif ex == "c":
    print(temperature,"°C is " , convert_to_fahrenheit(temperature),"°F")
else:
    print("Invalid input")
    