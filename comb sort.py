def comb_sort(arr): 
    gap = len(arr)
    shrink = 1.3 
    no_swap = False
    while not no_swap:
        gap = int(gap/shrink) 
        if gap < 1 : gap , no_swap = 1 , True
        else : no_swap = False 
        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap] : arr[i] , arr[i + gap] , no_swap = arr[i + gap] , \
                                                                         arr[i] , \
                                                                         False                
            i = i + 1

    return arr