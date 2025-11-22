FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    value = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(value)

def convert_to_fahrenheit(celsius):
    value = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(value)

temp = int(input("Enter the temperature value to convert: "))

convert_to_celsius(temp)
convert_to_fahrenheit(temp)
