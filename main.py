import json

# Personal Expense Tracker
# Lets users add income or expense entries

# Asks for user's name
def get_name():
    user_name = input ("Enter your name: ")
    return user_name

name = get_name()
print ("Welcome " + name)

# Asks for user's income
def income_earnings():
    user_income = input ("Please enter your income: ")
    return user_income

income = income_earnings()
print ("Your income is " + income)

# Asks for user's monthly expenses
def monthly_expenses():
    user_expenses = input ("Please do enter your expenses: ")
    return user_expenses

expenses = monthly_expenses()
print ("Your monthly expenses is around: " + expenses)

balance = float(income) - float(expenses)
print ("Your remaining balance is: ",balance)

expenses = []
while True:
    exp = input("Enter an expense (or 'done' to finish): ")
    if exp.lower() == "done":
        break
    expenses.append(float(exp))

total_expenses = sum(expenses)
print("Total expenses:", total_expenses)


    

