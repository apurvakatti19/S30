def partition(array, low, high):
	i = low - 1
	pivot = array[high]

	for j in range(low, high):
		if array[j] <= pivot:
			i = i+1
			array[i], array[j] = array[j], array[i]

	array[i+1], array[high] = array[high], array[i+1]
	return i+1

def quickSort(array, low, high):
	if len(array) == 1:
		return array

	if low < high:
		mid = partition(array, low, high)
		quickSort(array, low, mid-1)
		quickSort(array, mid+1, high)

if __name__ == "__main__":
    array = [17, 7, 81, 9, 14, 3]
    n = len(array)
    quickSort(array, 0, n-1)
    for i in range(n):
        print(array[i])