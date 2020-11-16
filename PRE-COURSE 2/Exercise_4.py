def mergeSort(array):
	if len(array) > 1:
		mid = len(array)//2
		L = array[:mid]
		R = array[mid:]

		mergeSort(L)
		mergeSort(R)

		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				array[k] = L[i]
				i += 1
			else:
				array[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			array[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			array[k] = R[j]
			j += 1
			k += 1

if __name__ == '__main__':
    array = [17, 7, 81, 9, 14, 3]
    n = len(array)
    mergeSort(array)
    for i in range(n):
        print(array[i])