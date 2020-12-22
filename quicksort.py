def quicksort(arr, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        p = partition(arr, start, end)
        quicksort(arr, start, p)
        quicksort(arr, p + 1, end)
 
 
def partition(arr, start, end):
    pivot = arr[start]
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and arr[i] <= pivot):
            i = i + 1
        while (i <= j and arr[j] >= pivot):
            j = j - 1
 
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[start], arr[j] = arr[j], arr[start]
            return j
 
 
arr = eval(input('Enter the list of numbers: '))
quicksort(arr, 0, len(arr))
print('Sorted list: ', end='')
print(arr)