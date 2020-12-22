def gaps(size):    
    length = size.bit_length()
    for k in range(length - 1, 0, -1) : yield 2**k - 1
 
def shell_sort(arr):
    def insertion_sort_with_gap(gap):
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while (j >= 0 and temp < arr[j]):
                arr[j + gap] = arr[j]
                j = j - gap
            arr[j + gap] = temp 
    for g in gaps(len(arr)) : insertion_sort_with_gap(g)
  
arr = eval(input('Enter the list of numbers: '))
shell_sort(arr)
print('Sorted list: ', end='')
print(arr)