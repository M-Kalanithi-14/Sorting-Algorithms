def bucket_sort(arr):
    largest = max(arr)
    length = len(arr)
    size = largest/length 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(arr[i]/size)
        if j != length : buckets[j].append(arr[i])
        else : buckets[length - 1].append(arr[i]) 
    for i in range(length):
        insertion_sort(buckets[i]) 
    result = []
    for i in range(length):
        result = result + buckets[i] 
    return result
     
arr = eval(input('Enter the list of (non-negative) numbers: '))
sorted_list = bucket_sort(arr)
print('Sorted list: ', end='')
print(sorted_list)
