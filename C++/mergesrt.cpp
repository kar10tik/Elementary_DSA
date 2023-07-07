// C++ program for Merge Sort
#include <iostream>
using namespace std;

void Merge(int A[], int left, int mid, int right)
{
	int B[sizeof(A)];
    int i = left;
    int j = mid + 1;
    int k = left;
    while (i <= mid and j <= right)
        if (A[i] < A[j])
            B[k] = A[i];
            i += 1;
        else
            B[k] = A[j];
            j += 1;
        k += 1;
    while (i <= mid)
        B[k] = A[i];
        i += 1;
        k += 1;
    while (j <= right)
        B[k] = A[j];
        j += 1;
        k += 1;
        i = left;
    while (i <= right)
        A[i] = B[i];
        i += 1;
	}
}

void MergeSort(int A[], int low, int high)
{
	if (low <= high and len(A) > 1):
        mid = int((low+high)/2);
        MergeSort(A, B, low, mid);
        MergeSort(arr, low, piv);
        Merge(A, B, low, mid, high);

}

// UTILITY FUNCTIONS
// Function to print an array
void printArray(int A[], int size)
{
	for (auto i = 0; i < size; i++)
		cout << A[i] << " ";
}

// Driver code
int main()
{
	int arr[] = { 12, 11, 13, 5, 6, 7 };
	auto arr_size = sizeof(arr) / sizeof(arr[0]);

	cout << "Given array is \n";
	printArray(arr, arr_size);

	mergeSort(arr, 0, arr_size - 1);

	cout << "\nSorted array is \n";
	printArray(arr, arr_size);
	return 0;
}