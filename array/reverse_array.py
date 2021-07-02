#Write a program to reverse an array 

def reverse(arr,n):
    i = n-1
    li =[]
    while i>=0:
        li.append(arr[i])
        i -=1 
    return li

A = [1, 2, 3, 4, 5, 6]
print(A)

print("Reversed list is",reverse(A,6))