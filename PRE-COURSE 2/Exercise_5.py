def partition(array, low, high):
	i = low - 1
	pivot = array[high]

	for j in range(low, high):
		if array[j] <= pivot:
			i = i+1
			array[i], array[j] = array[j], array[i]

	array[i+1], array[high] = array[high], array[i+1]
	return i+1

def quickSortIterative(arr, low, high):  
    size = high - low + 1
    stack = [0] * (size) 
    top = -1
    top += 1
    stack[top] = low
    top += 1
    stack[top] = high
  
    while top >= 0: 
        high = stack[top] 
        top -= 1
        low = stack[top] 
        top -= 1
   
        p = partition( arr, low, high) 
        if p-1 > low: 
            top += 1
            stack[top] = low
            top += 1
            stack[top] = p - 1
   
        if p + 1 < high: 
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = high
  
if __name__ == "__main__":
    array = [17, 7, 81, 9, 14, 3]
    n = len(array)
    quickSortIterative(array, 0, n-1)
    for i in range(n):
        print(array[i])  