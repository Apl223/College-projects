from conversions import *
from conversions_refactored import *

if __name__ == "__main__":
	#conversion.py
	print("\n")
	print("conversion.py: " + "\n")
	print(convertCelsiusToFahrenheit(300.00))
	print(convertCelsiusToKelvin(300.00))
	print(convertFahrenheittoCelsius(300.00))
	print(convertFahrenheittoKelvin(300.00))
	print(convertKelvintoFahrenheit(300.00))
	print(convertKelvintoCelsius(300.00))
	print("\n")
	#conversion_refactored.py
	print("conversion_refactored: " + "\n")
	print(convert('fahrenheit','kelvin', 300))
	print(convert('fahrenheit','celsius', 300))
	print(convert('fahrenheit','fahrenheit', 300))
	print(convert('celsius','kelvin', 300))
	print(convert('celsius', 'fahrenheit', 300))
	print(convert('kelvin', 'celsius', 300))
	print(convert('kelvin','fahrenheit', 300))

	print(convert('miles','yards', 300))
	print(convert('miles','meters', 300))

	print(convert('yards','meters', 300))
	print(convert('yards','miles', 300))

	print(convert('meters','miles', 300))
	print(convert('meters','yards', 300))
