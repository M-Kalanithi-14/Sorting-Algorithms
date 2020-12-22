#BUBBLE SORT

def bubblesort(arr , reverse = False) :
    ''' This function returns the list after sorting using
    'Bubble Sort' Algorithm'''
    length = len(arr)
    if reverse == False :
        for i in range(length) :
            for j in range(length - i - 1) :
                if arr[j] > arr[j+1] :
                    arr[j] , arr[j+1] = arr[j+1] , arr[j]
    else :
        for i in range(length) :
            for j in range(length - i - 1) :
                if arr[j] < arr[j + 1] :
                    arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr

#MERGE SORT

def mergesort(arr) :
    '''This function sorts an array using
    'Merge Sort' Algorithm'''
    if len(arr) > 1 :
        mid = len(arr) // 2
        lefthalf = arr[: mid]
        righthalf = arr[mid :]
        mergesort(lefthalf)
        mergesort(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf) :
            if lefthalf[i] < righthalf[j] :
                arr[k] = lefthalf[i]
                i += 1
            else :
                arr[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf) :
            arr[k]  = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf) :
            arr[k] = righthalf[j]
            j += 1
            k += 1
        return arr