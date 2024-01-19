# Name : YAJJALA JOSHUA KIRAN
# 700 Number : 700765513
# Problem 2.5 (Financial application: Calculate tips)

'''
Description:
Step 1: Reads the subtotal and gratuity rate from the user
Step 2: calculates gratuity rate and subtotal
        gratuity rate = gratuity rate / 10
        total = subtotal + gratuity_rate
Step 3: Display the results
'''

# step 1
subtotal = eval(input("Enter the subtotal: "))
gratuity = eval(input("Enter the gratuity: "))

# step 2
gratuity_rate = gratuity / 10
total = subtotal + gratuity_rate

# step 3
print("The gratuity is", gratuity_rate, "and total is", total)
