def cocktail_shaker_sort(arr):

    def swap(i , j) : 
        arr[i], arr[j] = arr[j], arr[i]

    upper = len(arr) - 1
    lower = 0 
    no_swap = False
    while (not no_swap and upper - lower > 1):
        no_swap = True
        for j in range(lower, upper):
            if arr[j + 1] < arr[j]:
                swap(j + 1, j)
                no_swap = False
        upper = upper - 1 
        for j in range(upper, lower, -1):
            if arr[j - 1] > arr[j]:
                swap(j - 1, j)
                no_swap = False
        lower = lower + 1

    return arr