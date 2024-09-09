def binary_search(list1,n):
    low=0
    high=len(list1)-1
    mid=0
    while low<=high:
        mid=(high+low)//2
        if list1[mid]<n:
            low=mid+1
        elif list1[mid]>n:
            high=mid-1
        else:
            return mid
    return -1
list1=[12,24,32,39,45,50,54,64,89]
n=64
result=binary_search(list1,n)

if result !=-1:
    print("Element is present at index",str(result))
else:
    print("Element not found in list")
### Time Complexity O(1)-> Best case , O(log n )-> avergae and worst case
#### Using Recursion 
'''
def binary_search(list1,n)SS:
if low<=high:
 mid=(low+high)//2
 if list1[mid]==n:
  return mid
 elif list1[mid]>n:
  return binary_search(list1,low,mid-1,n)
 else:
  return binary_search(list1,mid+1,high,n)
else:
 return -1
list1=[12,24,32,39,45,50,54]
n=32
res= binary_search(list1,0,len(list1)-1,n)

if res != -1:
 print("Element is present at index",str(res))
else:
 print("Element not present in list1")


'''
