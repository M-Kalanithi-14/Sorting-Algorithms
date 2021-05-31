# Python program for Bitonic Sort. Note that this program
# works only when size of input is a power of 2.

# The parameter dir indicates the sorting direction, ASCENDING
# or DESCENDING; if (a[i] > a[j]) agrees with the direction,
# then a[i] and a[j] are interchanged.*/

# It recursively sorts a bitonic sequence in ascending order,
# if dir = 1, and in descending order otherwise (means dir=0).
# The sequence to be sorted starts at index position start,
# the parameter count is the number of elements to be sorted.


# This funcion first produces a bitonic sequence by recursively
# sorting its two halves in opposite sorting orders, and then
# calls Merge to make them in the same order
def BitonicSort(arr, start, count, reverse=False):
    if reverse:
        direction = 0
    else:
        direction = 1

    def Merge(arr, start, count, direction):
        def CompAndSwap(arr, i, j, direction):
            if (direction==1 and arr[i] > arr[j]) or (direction==0 and arr[i] < arr[j]):
                arr[i], arr[j] = arr[j], arr[i]

        if count > 1:
            k = int(count/2)

            for i in range(start , start+k):
                CompAndSwap(arr, i, i+k, direction)

            Merge(arr, start, k, direction)
            Merge(arr, start+k, k, direction)

    if count > 1:
        k = int(count/2)

        BitonicSort(arr, start, k, 1)
        BitonicSort(arr, start+k, k, 0)
        Merge(arr, start, count, direction)

    return arr

# Driver code to test above
arr = [3, 7, 4, 8, 6, 2, 1, 5]
n = len(arr)

res = BitonicSort(arr, 0, n, True)
print ("Sorted array is")
for i in range(n):
    print("%d" %res[i])