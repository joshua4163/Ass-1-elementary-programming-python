# Name : YAJJALA JOSHUA KIRAN
# 700 Number : 700765513
# Problem 2.7 (Find the number of years and days)

'''
Description:
Step 1: Reads the minutes from the user
Step 2: calculates days,years, remaining days
        days = minutes // (24 * 60)
        years = days // 365
        remaining_days = days % 365
Step 3: Display the results
'''

# step 1
minutes = eval(input("Enter the number of minutes: "))

# step 2
days = minutes // (24 * 60)
years = days // 365
remaining_days = days % 365

# step 3
print(f"{minutes} minutes is approximately {years} years and {remaining_days} days.")
