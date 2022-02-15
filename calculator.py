from functools import reduce

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
    for i in inputlist:
        z = int(i)
        newlist.append(z)
    numbers_divided = reduce(lambda x, y: x/y, newlist)
    return numbers_divided


operation = input("Enter operation: ")
if operation == '+' or '-' or '*' or '/':
        print("Please enter numbers: ")
        inputlist = input().split()
        #print(inputlist)

if operation\
        == '+':
    varlist = add(inputlist)
    splitlist = inputlist
    #print((*inputlist, sep = "+")varlist)
    print("inputs added: ", varlist)

elif operation == '-':
    varlist = subtract(inputlist)
    #print(inputlist[0], "-", inputlist[1], "-", inputlist[2], "-", inputlist[3], "=", varlist)
    print("inputs subtracted: ", varlist)

elif operation == '*':
    varlist = multiply(inputlist)
    #print(inputlist[0], "*", inputlist[1], "*", inputlist[2], "*", inputlist[3], "*", inputlist[4], "*", inputlist[5], "=", varlist)
    print("inputs multiplied: ", varlist)

elif operation == '/':
    if i in inputlist == 0:
        print("cannot divide by 0!")
    varlist = divide(inputlist)
    print("inputs divided equals: ", varlist)



else:
    print("Invalid Input")

    #next_calculation = input("Another calculation? (Y/N): ")
    #if next_calculation == "N":
        #break
