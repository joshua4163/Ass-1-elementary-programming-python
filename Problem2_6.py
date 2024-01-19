# Name : YAJJALA JOSHUA KIRAN
# 700 Number : 700765513
# Problem 2.6 (Sum the digits in an integer)

'''
Description:
Step 1: Reads the integer from the user
Step 2: calculates dollars, quarters,dimes,nickels,pennies
        dollars = cents // 100
        quarters = remaining_cents // 2
        dimes = remaining_cents // 10
        nickels = remaining_cents // 5
Step 3: Display the results
'''

# step 1
cents = eval(input("Enter an amount as integer: "))

# step 2
dollars = cents // 100
remaining_cents = cents % 100

quarters = remaining_cents // 25
remaining_cents = quarters % 25

dimes = remaining_cents // 10
remaining_cents = dimes % 10

nickels = remaining_cents // 5
remaining_cents = nickels % 5

pennies = remaining_cents

# step 3
print(f"Your amount {cents} consists of")
print(f"{dollars} dollars")
print(f"{quarters} quarters")
print(f"{dimes} dimes")
print(f"{nickels} nickels")
print(f"{pennies} pennies")
