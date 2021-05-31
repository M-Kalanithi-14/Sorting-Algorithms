from random import shuffle

def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        smallest = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j

        arr[i], arr[smallest] = arr[smallest], arr[i]

    return arr
 
arr = [i for i in range(1, 101)]
shuffle(arr)
res = selection_sort(arr)
print('Sorted list: ', res)