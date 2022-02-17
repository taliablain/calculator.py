import sys
from functools import reduce

loop = 1
while loop == 1:
#functions for the different operations
    def add(*args):
        newlist = []
        for i in inputlist:
            z = int(i)
            newlist.append(z)
        numberssum = sum(newlist)
        return numberssum

# This function subtracts two numbers
    def subtract(*args):
        newlist = []
        for i in inputlist:
            z = int(i)
            newlist.append(z)
        numberssum = newlist[0] - sum(newlist[1:])
        return numberssum

# This function multiplies two numbers
    def multiply(*args):
        newlist = []
        for i in inputlist:
            z = int(i)
            newlist.append(z)
        numbers_multiplied = reduce(lambda x, y: x*y, newlist)
        return numbers_multiplied


# This function divides two numbers
    def divide(*args):
            newlist = []
            try:
                for i in inputlist:
                    z = int(i)
                    newlist.append(z)
                numbers_divided = reduce(lambda x, y: x/y, newlist)
                return numbers_divided
            except ZeroDivisionError:
                print("division by zero not permitted!")
                sys.exit()



    operation = input("Enter operation: ")
    if operation == '+' or '-' or '*' or '/':
            print("Please enter numbers: ")
            inputlist = input().split()
        #print(inputlist)

    if operation == '+':
        varlist = add(inputlist)
        print(*inputlist, sep='+', end=' ')
        print('=',varlist)


    elif operation == '-':
        varlist = subtract(inputlist)
        print(*inputlist, sep='-', end=' ')
        print('=',varlist)


    elif operation == '*':
        varlist = multiply(inputlist)
        print(*inputlist, sep='*', end=' ')
        print('=',varlist)

    elif operation == '/':
        varlist = divide(inputlist)
        print(*inputlist, sep='/', end=' ')
        print('=',varlist)

    else:
        print("Invalid Input")

    next_calculation = input("Another calculation? (Y/N): ")
    if next_calculation == "N":
        sys.exit()
