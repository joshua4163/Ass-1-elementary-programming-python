# Name : YAJJALA JOSHUA KIRAN
# 700 Number : 700765513
# Problem 2.2 (Compute the volume of a cylinder)

'''
Description:
Step 1: Reads the length and radius of the cyclinder
Step 2: calculates the area and volume of the cyclinder
        area = radius * radius * 3.14159265359
        volume = area * length
Step 3: Display the results
'''

# step 1
radius = eval(input(" Enter the radius of the radius:"))
length = eval(input("Enter the length of the cyclinder:"))

# step 2
area = radius * radius * 3.14159265359
volume = area * length

# step 3
print("The area is:", area)
print("The volume of the cylinder is:", volume)
