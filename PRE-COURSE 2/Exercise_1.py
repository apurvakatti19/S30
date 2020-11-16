def binary_search(array, x): 
    low = 0
    high = len(array) - 1
    mid = 0
    while low <= high: 
        mid = (high + low) // 2

        if array[mid] < x: 
            low = mid + 1
  
        elif array[mid] > x: 
            high = mid - 1
   
        else: 
            return mid 
    return -1
  
if __name__ == "__main__":
    array = [ 22, 35, 60, 78, 99 ] 
    search = 35
    result = binary_search(array, search) 
  
if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element not present")