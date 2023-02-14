print("QuickSort Implementation")

def QuickSort(arr, low, up):
    if (low < up):
        piv = Partition(arr, low, up)
        QuickSort(arr, low, piv)
        QuickSort(arr, piv, up)
        return arr

def Partition(A, low, high):
    pivot = A[low]
    while (low < high):
        while (A[low] < pivot):
            low += 1
        while (A[high] > pivot):
            high -= 1
        if (low < high):
            A[low], A[high] = A[high], A[low]
            low += 1
            high -= 1
    while (low < high):
        pivot, A[high] = A[high], pivot
    return high

n = int(input("How many elements in the array?"))
arr = [int(input('Enter element ' + str(i+1) + ' ')) for i in range(n)]
p = input("Enter the lower and higher indices for Quicksort").split()
res = QuickSort(arr, int(p[0]), int(p[1]))
print(res)