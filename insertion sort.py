def insertionsort(arr , reverse = False) :
    if reverse == False :
        for i in range(1 , len(arr)) :
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
            else : arr[j + 1] = key
        return arr
    else :
        for i in range(1 , len(arr)) :
            key = arr[i]
            j = i - 1
            while j >= 0 and key > arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
            else : arr[j + 1] = key
        return arr
        
