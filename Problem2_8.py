# Name : YAJJALA JOSHUA KIRAN
# 700 Number : 700765513
# Problem 2.8 (Science: calculate energy)

'''
Description:
Step 1: Reads the water,initial temperature,final temperature from the user
Step 2: calculates energy using the formula
        energy = water * (finaltemp - initialtemp) * 4184
Step 3: Display the results
'''

# step 1
water = eval(input("Enter the water level: "))
initialtemperature = eval(input("Enter the Intial temperature: "))
finaltemperature = eval(input("Enter the final temperature: "))

# step 2
energy = water * (finaltemperature - initialtemperature) * 4184

# step 3
print("The energy needed is", energy)
