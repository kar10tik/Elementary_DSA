print("MergeSort Implementation")
# Python program for implementation of MergeSort
def MergeSort(arr):

	if len(arr) > 1:
        
		mid = len(arr)//2
		left = arr[:mid]
		right = arr[mid:]
		MergeSort(left)
		MergeSort(right)
		i = j = k = 0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1

		while i < len(left):
			arr[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1

n = int(input("How many elements in the array?"))
arr = [int(input()) for i in range(n)]
MergeSort(arr)
print("Sorted Array:")
for i in range(len(arr)):
	print(arr[i], end = " ")


'''def MergeSort(A, B, low, high):
    if (low <= high and len(A) > 1):
        mid = int((low+high)/2)
        MergeSort(A, B, low, mid)
        MergeSort(arr, low, piv)
        Merge(A, B, low, mid, high)

def Merge(A, B, left, mid, right):
    i = left
    j = mid + 1
    k = left
    while (i <= mid and j <= right):
        if A[i] < A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1
    while (i <= mid):
        B[k] = A[i]
        i += 1
        k += 1
    while (j <= right):
        B[k] = A[j]
        j += 1
        k += 1
        i = left
    while (i <= right):
        A[i] = B[i]
        i += 1
'''