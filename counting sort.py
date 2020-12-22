def counting_sort(arr, largest): # largest => maximum value of the list
    c = [0]*(largest + 1)

    for i in range(len(arr)):
        c[arr[i]] = c[arr[i]] + 1  

    c[0] = c[0] - 1 

    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1] 

    result = [None]*len(arr)

    for x in reversed(arr):
        result[c[x]] = x
        c[x] = c[x] - 1

    return result