#Program to find the minimum (or maximum) element of an array

def getMin(arr,n):
    minimum=arr[0]
    for i in range(1,n):
        if arr[i]<minimum:
            minimum = arr[i]
    return minimum

def getMax(arr,n):
    maximum=arr[0]
    for i in range(1,n):
        if arr[i]>maximum:
            maximum = arr[i]
    return maximum

arr = [12, 123, 45, 67, 1]
n = len(arr)
print ("Minimum element of array:", getMin(arr, n))
print ("Maximum element of array:", getMax(arr, n))