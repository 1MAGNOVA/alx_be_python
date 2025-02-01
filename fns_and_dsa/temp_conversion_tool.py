#!/usr/bin/env python3

#Define Global Conversion Factors

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


#define convert_to_celsius(fahrenheit) 
def convert_to_celsius(fahrenheit):
    celsius(fahrenheit)= (F-32) * CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius(fahrenheit)

def convert_to_fahrenheit(celsius):
    fahrenheit(celsius) = (C * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit(celsius)


#function to handle user input

Def Main():
    try:
        user_temp = float(input("Enter the temperature to convert: "))
        user_temp_unit = (input("Is this temperature in Celsius or Fahrenheit? (C/F)"))
        if user_temp_unit.upper() == "F":
            fahrenheit = float (user_temp)  
            C = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {C:.2f}°C.")

        elif user_temp_unit.upper == "C":
            celsius = float (user_temp)
            F = convert_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {F:.2f}°F.")
        else:
            # Raise an error if the temperature unit is invalid
            raise ValueError("Invalid temperature unit. Please use 'C' or 'F'.")
    
    except ValueError as e:
    # Handle invalid input
      print(f"Invalid temperature. Please enter a numeric value. Error: {e}")

# Run the program
if __name__ == "__main__":
    main()

