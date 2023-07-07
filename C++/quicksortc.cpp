#include <iostream>
using namespace std;

void swap(int* a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int Partition(int arr[], int low, int high) 
{
    int pivot = arr[low];
    int i = low;
    for (int j = low; j <= high; j++)
    {
        if (arr[j] <= pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void QuickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        int piv = Partition(arr, low, high);
        QuickSort(arr, low, piv);
        QuickSort(arr, piv, high);
    }
}

void display(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main()
{
    cout << "Quicksort Implementation" << endl;
    int n;
    cout << "How many elements in array? " << endl;
    cin >> n;
    int arr[n];
    cout << "Enter elements in the following lines" << endl;
    for (int j = 0; j < n; j++)
    {
        cin >> arr[j];
    }
    int n1 = sizeof(arr)/sizeof(arr[0]);
    QuickSort(arr, 0, n1 - 1);
    cout << "Sorted array: " << endl;
    display(arr, n1);
    return 0;
}