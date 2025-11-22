FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    value = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(value)

def convert_to_fahrenheit(celsius):
    value = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(value)

temp = int(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
if unit == 'C':
    convert_to_fahrenheit(temp)
elif unit == 'F':
    convert_to_celsius(temp)
else:
    print("Invalid temperature. Please enter a numeric value.")