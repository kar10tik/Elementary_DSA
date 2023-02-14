#Quickselect Implementation
def Partition(A, low, high):
    x = A[high]
    i = low
    for j in range(low, high):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1          
    A[i], A[high] = A[high], A[i]
    return i

def QuickSelect(A, low, high, k):
    if (k > 0 and k <= high - low + 1):
        index = Partition(arr, low, high)
        # if position is same as k
        if (index - low == k - 1):
            return A[index]
        #left subarray recursion
        if (index - low > k - 1):
            return QuickSelect(A, low, index - 1, k)
        #right subarray recursion
        return QuickSelect(A, index + 1, high, k - index + low - 1)
    print("Index exceeds list range!")

ch = 'y'
while (ch == 'y' or ch == 'Y'):
    print("Program to find kth smallest element in unsorted array")
    n = int(input("How many elements in the array? "))
    arr = [int(input('Enter element ' + str(i+1) + ' ')) for i in range(n)]
    p = input("Enter the lower and higher indices for Quickselect ").split()
    elem = int(input("Enter the value of k "))
    res = QuickSelect(arr, int(p[0]), int(p[1]), elem)
    print(res)
    ch = input("Do you wish to continue? ")