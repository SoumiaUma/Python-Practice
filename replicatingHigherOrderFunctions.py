"""
Creating my own map function (myMap). It takes each value in my list (values) and triples 
the value in the list values and returns the new list with the values tripled
"""
values = [2,6,1,9,0,12]
#Lambda function that multiples the values in the values list by 5
multiplyOperation = lambda x:x*3
def myMap (multiplyOperation,values):
    #Creating an empty list to store the new values from my list (values) that are tripled using the op function
    outputList = []
    #Loop that appends the tripled value calculated using the op function into the outputList list
    for value in values:
        outputList.append(multiplyOperation(value))
    return outputList
#Printing the mymap function
print('Part 1: ',myMap(multiplyOperation,values))


"""
Creating my own reduce function.It takes the values from the list (values) 
and adds them together using a function additionOperation in a for loop.
"""
values = [1,2,3,4,5]
#Creating a variable startVal that is used to add the values in the values list
startVal=0
#Using the lambda function that adds the values in the values list together 
additionOperation = lambda x,y: x + y
#Function reduce that adds the values from the values list 
def reduce(additionOperation,values,startVal):
    #Setting a variable currentValue to startVal to which is then used to store the new current value
    currentValue=startVal
    """
    Loop that uses the op1 fucntion to calculate and store the new value into the variable currentValue 
    by adding the values in the list values
    """
    for value in values:
        currentValue=additionOperation(currentValue, value)
    return currentValue
#Printing the reduce function 
print('Part 2: ',reduce(additionOperation,values,startVal))

"""
Creating my own filter function. It takes the values from the list (values) 
and returns a new list with only the even numbers from the list.
"""
values=[1,2,4,7,8,3,14,28]
#Using the lambda function that sees if a value is even by checing if its module is 0 when divided by 2 
moduleOperation = lambda x: (x % 2) == 0
def filter(moduleOperation,values):
    #Creating an empty array to store the even numbers in the values list
    newList = []
    #Loop to see if the values in values list is even using the op2 function and appending it to the newList array if true
    for value in values:
        if moduleOperation(value)==True:
            newList.append(value)
    #Returning the new list with the even numbers 
    return newList
#Printing the filter function
print('Part 3: ',filter(moduleOperation,values))


