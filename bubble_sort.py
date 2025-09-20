#using for loop

l=[4,5,8,2,6]
for i in range(len(l)):
    for j in range(len(l)-(i+1)):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)  

#using while loop

l=[5,4,7,1]
i=0
while i<len(l):
    j=0
    while j<(len(l)-(i+1)):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
        j+=1
    i+=1
    
print(l)

#using recursion

def recursive_bubble_sort(arr,n):
    if n == 1:
        return arr
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    return recursive_bubble_sort(arr,n-1)

l=[5,7,3,4,8,2]
print(recursive_bubble_sort(l,len(l)))
