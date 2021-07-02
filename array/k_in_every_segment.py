#Check if a key is present in every segment of size k in an array

def check_segments(arr,n,k):
    j=k-1
    i=0
    x=len(arr)
    if(x%k==0):
        total = x/k
    else:
        total = x/k +1
    count = 0 
    while i<len(arr):        
        # for j in range(k):
        if j < len(arr) and  (n in arr[i:j+1]):            
            
            count +=1
        elif j>= len(arr)-1 and (n in arr[i:len(arr)]):
            count +=1
        else: 
            break
        i=j+1
        j+=k
    if count== total:
        return "Yes"
    else: 
        return "No"

arr = [5, 8, 7, 12, 14, 3, 9]
x, k = 8,2
        
print(check_segments(arr,x,k))