def linear_search(list1,n,key):
 for i in range(0,n):
   if(list1[i]==key):
    return i
 return -1

list1=[1,3,5,6,4,7,9,2]
key=2
n=len(list1)
res=linear_search(list1,n,key)
if(res ==-1):
 print("Element Not Found")
else:
 print("Element found at index : ", res)

 
''' Time Complexity
Base Case : O(1) First element
Average Case: O(n) 
Worst Case: O(n)
'''
