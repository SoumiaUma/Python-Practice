#Implementing the Heap Data Structure

#The Parent, Left and Right functions follow different code then from the slides because the slide code seemed
#not to work. 
def Parent(i):
    return (i-1)//2

def Left(i):
    return (i*2)+1

def Right(i):
    return (i*2)+2

def BUILDMAXHEAP(A):
    heapSize = (len(A)//2)-1
    for i in range (heapSize,-1,-1):
        MAXHEAPIFY(A,i,len(A)-1)

#Length of array is passed as an argument (was not in the slides), but I added it since it didn't work properly
#without the length being passed as an argument
def MAXHEAPIFY(A,i,n):
    l = Left(i)
    r = Right (i)
    if l <= n-1 and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= n-1 and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MAXHEAPIFY(A,largest,n-1)

def HEAPMAXIMUM(A):
    return A[0]

def HEAPEXTRACTMAX(A):
    heapSize = len(A)
    #https://rollbar.com/blog/throwing-exceptions-in-python/ used to find out how to raise error exception
    if len(A) < 0:
        raise Exception("heap underflow")
    max = A[0]
    A[0] = A[heapSize-1]
    heapSize -= 1
    MAXHEAPIFY(A,0,heapSize)
    #Not in pseudo code, but used to remove the element in the array at last position 
    A.remove(A[heapSize])
    return max

def MAXHEAPINSERT(A,x):
    heapSize = len(A)-1
    heapSize += 1 
    A[heapSize:] = [x]
    i = heapSize
    while A[i] > A[Parent(i)] and i > 0:
        A[i], A[Parent(i)] = A[Parent(i)], A[i]
        i = Parent(i)

def HEAPSORT(A):
    BUILDMAXHEAP(A)
    for i in range (len(A)-1,0,-1):
        A[0], A[i] = A[i], A[0]
        MAXHEAPIFY(A,0,i)
        printAsTree(A)
        

def printAsArray(A):
    #Returning no elements in array when 0 elements are in the array
    if (len(A)-1 < 0):
        print("No elements in array")
    else:
        print(A)


def printTree(arr, index, depth):
    #Returning nothing when index is at a position less then array size 
    # #or greater then the length of the array is reached
    if (index < 0 or index >= len(arr)):
        return

    #https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/
    #Above website was used to find way to increase depth (space at end) by adding the amount
    #of space that is equal to the index value at arr[0]
    depth += arr[0]

    #Recursively printing from right most to the left
    printTree(arr, Right(index), depth+1)

    #Adding horizontal space from right to the depth value
    for i in range (arr[0],depth):
        print(end = " ")
    
    #Printing the element at the index of array
    print(" " + str(arr[index]))
    
    #Recursively printing the left side of tree 
    printTree(arr, Left(index), depth+1)

#Calling the printTree function with the array starting at index 0 and depth 0
def printAsTree(A):
    printTree(A, 0, 0)

arr = [14,8,12,2,5,9,6,1]
printAsArray(arr)
printAsTree(arr)
MAXHEAPINSERT(arr,10)
printAsTree(arr)
HEAPEXTRACTMAX(arr)
printAsTree(arr)
HEAPEXTRACTMAX(arr)
printAsTree(arr)
HEAPEXTRACTMAX(arr)
printAsArray(arr)
printAsTree(arr)
