#!/usr/bin/env python3

#Ask the user to input the current weather from a predefined set of conditions: sunny, rainy, or cold
weather_condition = input("What's the weather like today? (sunny/rainy/cold):")

#Based on the user’s input, your program will recommend different types of clothing

#for sunny weather
if weather_condition == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_condition == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_condition == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather")
