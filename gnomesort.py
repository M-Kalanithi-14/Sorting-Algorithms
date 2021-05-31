def gnome_sort(arr):
    for pos in range(1, len(arr)):
        while (pos != 0 and arr[pos] < arr[pos - 1]):
            arr[pos], arr[pos - 1] = arr[pos - 1], arr[pos]
            pos = pos - 1

    return arr
 
arr = [i for i in range(1, 101)]
res = gnome_sort(arr)
print('Sorted list: ', res)