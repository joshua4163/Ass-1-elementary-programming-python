# Name : YAJJALA JOSHUA KIRAN
# 700 Number : 700765513
# Problem 2.9 (Science: wind-chill temperature)

'''
Description:
Step 1: Reads the temperature in Fahrenheit between -58 and 41 and wind speed miles per hour (must be greater than or equal to 2) from the user
Step 2: calculates wind chill with the formula
        wind chill = 35.74 + 0.6215 * (temperature) - 35.75 * wind speed ** 0.16 + 0.4275 * (temperature) * wind speed ** 0.16
Step 3: Display the results
'''

# step 1

temperature = eval(input("Enter temperature in Fahrenheit:"))
wind_speed = eval(input("Enter wind speed:"))

# step 2
if temperature >= -58 and temperature <= 41 and wind_speed >= 2:
    windchill = 35.74 + 0.6215 * (temperature) - 35.75 * wind_speed ** 0.16 + 0.4275 * (
        temperature) * wind_speed ** 0.16

# step 3
print("The wind chill index is", windchill)
