# Name : YAJJALA JOSHUA KIRAN
# 700 Number : 700765513
# Problem 2.10 (Physics: find runway length)

'''
Description:
Step 1: Reads the speed and acceleration from the user
Step 2: calculates minimumrunwaylength using the formula
        length = speed * speed / 2 * acceleration
Step 3: Display the results
'''

# step 1
speed = eval(input("Enter the speed:"))
acceleration = eval(input("Enter the acceleration:"))

# step 2
minimumrunawaylength = (speed ** 2) / (2 * acceleration)

# step 3
print("The minimum runway length for this airplane is", minimumrunawaylength, "meters.")
