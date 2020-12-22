def mergesort(arr) :
    '''This function sorts an array using
        'Merge Sort' sorting technique.'''
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