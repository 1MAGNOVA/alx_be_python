#!/usr/bin/env python3

#Prompt User for Weather Input
weather_condition = input ("What's the weather like today? (sunny/rainy/cold):")

print(f"What's the weather like today? (sunny/rainy/cold): {weather_condition}")
#Based on the user’s input, your program will recommend different types of clothing

#If the weather is “sunny”
if weather_condition == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_condition == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_condition == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else
    print("Sorry, I don't have recommendations for this weather.")
