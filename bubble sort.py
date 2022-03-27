def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
 
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
arr = [21, 37, 4, 20, 19, 39, 1]
 
bubbleSort(arr)
 
print ("Sorted Array:")
for i in range(len(arr)):
    print ("% d" % arr[i],end=" ")