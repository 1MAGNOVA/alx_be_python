#!/usr/bin/env python3

#Prompt User for Weather Input
weather = input("What's the weather like today? (sunny/rainy/cold):")

print(f"What's the weather like today? (sunny/rainy/cold): {weather_condition}")
#Based on the user’s input, your program will recommend different types of clothing

#If the weather is “sunny”
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
