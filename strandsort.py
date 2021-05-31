def strand_sort(arr):
	def merge_list(arr, b):
		out = []

		while len(arr) and len(b):
			if arr[0] < b[0]:
				out.append(arr.pop(0))
			else:
				out.append(b.pop(0))

		out += arr
		out += b

		return out
	 
	def strand(arr):
		i, s = 0, [arr.pop(0)]

		while i < len(arr):
			if arr[i] > s[-1]:
				s.append(arr.pop(i))
			else:
				i += 1

		return s

	out = strand(arr)

	while len(arr):
		out = merge_list(out, strand(arr))

	return out
 
res = strand_sort([1, 6, 3, 2, 1, 7, 5, 3])
print(res)