def pigeonhole_sort(arr):
    my_min = min(arr) 
    my_max = max(arr) 
    size = my_max - my_min + 1 
    holes = [0] * size
    for x in arr: 
        assert type(x) is int, "integers only please; got %s(%s)"%(type(x) , x)
        holes[x - my_min] += 1
    i = 0
    for count in range(size): 
        while holes[count] > 0: 
            holes[count] -= 1
            arr[i] = count + my_min 
            i += 1
            
arr = [2,33,443,554,55,6,6,7,8,8,65,445,6.45] 
print("Sorted order is : ", end =" ")   
pigeonhole_sort(arr)
for i in range(0, len(arr)): print(arr[i], end =" ") 
