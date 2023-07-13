# Yvonne Aime 
#COP2500 
#July 5 2023

# Function Notes


    # You must define the function before you use it.
    # You can pass in values, seperated by a comma
    # You can only return 1 value (Not true in python, but true in this class)
    # Variables inside of the function have no relationship to the ones outside.
    # Same is true with the parameters (the values you pass in.
    # When you call return, it ends the function.

#Task 1 - Function Determine Discounts
def f(x):
    y = x + 5
    return y
z = f(5)
print(z)
print( f(13) )
value = 20
print(f(value))

# Calculate the the distance between two numbers.
def g(a, b):
    if (a > b):
        return a-b
    else:
        return b-a
    
# Calculate the the distance between two numbers.
def h(a, b):
    if (a > b):
        return a-b
    return b-a
print(g(15, 10))
print(g(10, 15))
def ticket_cost(ticket_price, adults, seniors, students, children):
    total = 0
    adult_price = adults * ticket_price
    if (ticket_price >= 12):
        senior_cost = ticket_price - 2
    else:
        senior_cost = ticket_price
    senior_price = seniors * senior_cost
    children_price = children *.5* ticket_price
    student_price = ticket_price * .9 * students
    total = adult_price + senior_price + children_price + student_price
    return total
print(ticket_cost(10, 2, 0, 0, 0)) # $20
print(ticket_cost(10, 0, 2, 0, 0)) # $20
print(ticket_cost(22, 0, 2, 0, 0)) # $40
print(ticket_cost(10, 0, 0, 2, 0)) # $18
print(ticket_cost(20, 0, 0, 0, 3)) # $30
print(ticket_cost(22, 2, 2, 2, 2)) # 145.6
value = True
if value == True:
    print("Value is true")
else:
    print("value is false")
def hamburger(number, cashier, sale):
    total = number
    if (cashier == True):
        total = total * 2
    elif (sale == True):
        total = total * 1.2
        total = int(total)
    return total
# Hamburger with no sales or people we like.
print( hamburger(2, False, False) ) 
# Testing when we like the people and there is sale
print( hamburger(10, True, True) ) 
 # Testing when we like the people but no sale.
print( hamburger(6, True, False) )
# Testing when we don't like people but there is a sale.
print( hamburger(10, False, True) ) 
# Testing when we don't like people but there is a sale.
print( hamburger(12, False, True) ) 
def meal_calc(meals):
    total = 0
    for count in range(meals):
        cost = float(input("How much does the meal #" + str(count+1) + " cost?\n"))
        total = total + cost
    return total
print(meal_calc(3) )

def total_cost(money):
    items = 0
    while (money > 0):
        cost = int(input("How much does the next item cost?\n"))
        money = money - cost
        items = items + 1
    if (money < 0):
        items = items - 1
    return items

print(total_cost(20))
