# Yvonne Aime, COP2500, July 5 2023
# Class Activity - Function

#Task 1 - Function Determine Discounts
def deter_discount(ticket_price, adults, seniors, children, students):
    total = 0
    if(adults > 0):
         total += ticket_price * adults
    elif(seniors > 0 ):
         if(ticket_price >= 12 ):
            total += (ticket_price - 2) * seniors
         else:
            total += (ticket_price) * seniors
    elif(children > 0):
        total += (ticket_price * .50) * children
    elif(students > 0):
        print(students, ticket_price)
        total += (ticket_price * .9) * students
    print(total)


deter_discount(20, 0, 0, 0, 3)

    