"""
Implementing the Queue data structure using Classes
"""
class Queue:
    def __init__(self):
        """
        __init__(self)
        This function creates an empty list 
        @arg self The queue 
        """
        self.list = []
    def front(self):
        """
        front(self)
        This function returns the first element of the queue
        @arg self The queue 
        @return The first element of the list
        """
        return self.list[0]
    def dequeue(self):
        """
        dequeue(self)
        This function removes the first element in the list and returns that value 
        @arg self The queue 
        @return The first element of the list
        """
        temp = self.front()
        self.list.remove(temp)
        return temp
    def enqueue(self,item):
        """
        enqueue(self,item)
        This function adds an element to the back of the queue  
        @arg self The queue 
        @arg item The value that is being added to the back of the queue
        @return The list with added element to the back of the queue
        """
        return self.list.append(item)
    def isEmpty(self):
        """
        isEmpty(self)
        This function checks the length of the list and returns true if the list is empty (with length of zero) or false if otherwise  
        @arg self The queue 
        @return The true if the list is empty (with length of zero) or false if otherwise 
        """
        if (len(self.list) == 0):
            return True
        else:
            return False
    def __str__(self):
        """
        __str__(self)
        This function returns a string representation of the queue 
        @arg self The queue 
        @return The string representation of the queue 
        """
        return str(self.list)

#Testing the Queue() class
queue = Queue()
print('Check empty:', queue.isEmpty())
print('empty:', queue)
queue.enqueue(15)
print('After adding 15 to queue:', queue)
print('Check empty:', queue.isEmpty())
queue.enqueue(0)
print('After adding 0 to queue:', queue)
print('Calling deque():', queue.dequeue())
print('After dequeue():', queue)
queue.enqueue(4)
print('after enqueue(4):', queue)
print('dequeue():', queue.dequeue())
print('after dequeue():', queue)
print('dequeue():', queue.dequeue())
print('isEmpty():', queue.isEmpty())


"""
Function to use queue data structure. This function determines if a string is a palindrome.
"""
def isPalindrome(str):
    """
    isPalindrome() function breaks the string in half 
    and checks from begginning to middle and middle to end.
    The function returns true if the element in the string is equal to 
    last element popped from the string and false otherwise
    """
    #Creating a variable to store the length of the string
    n = len(str)
    #Appending all the string characters in the first half of the string to the stack
    for i in range (int(n/2)):
        queue.enqueue(str[i])
    """
    If the length of the string is an even number than starting from the
    middle of the string to the end a character is popped and comapred to
    the next character in the string. If the compared strings are equal to 
    each other then the function returns true
    If the length of the string is an odd number than skipping one from the 
    middle position to the end a character is popped and comapred to the next 
    character in the string. If the compared strings are equal to each other 
    then the function returns true
    """
    if (n%2 == 0):   
        for i in range (int(n/2), n): 
            if str[i] == queue.dequeue():
                return True  
    else: 
        for i in range (int((n/2)+1),n): 
            if str[i] == queue.dequeue():       
                return True
    return False

#Testing the isPalindrome() function by printing the returned boolean of true or false determined from the function
str = "Racecar"
print('\nPart 2')
print(str, 'is a palindrome: ', isPalindrome(str))

