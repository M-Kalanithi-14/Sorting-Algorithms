def cycleSort(arr):
  writes = 0
   
  for cycleStart in range(0, len(arr) - 1):
    item = arr[cycleStart]     
    pos = cycleStart

    for i in range(cycleStart + 1, len(arr)):
      if arr[i] < item:
        pos += 1
     
    if pos == cycleStart:
      continue
     
    while item == arr[pos]:
      pos += 1

    arr[pos], item = item, arr[pos]
    writes += 1
     
    while pos != cycleStart:
      pos = cycleStart

      for i in range(cycleStart + 1, len(arr)):
        if arr[i] < item:
          pos += 1
       
      while item == arr[pos]:
        pos += 1

      arr[pos], item = item, arr[pos]
      writes += 1
   
  return arr
   
arr = [1, 8, 3, 9, 10, 10, 2, 4 ]
res = cycleSort(arr)
 
print("After sort : ", res)