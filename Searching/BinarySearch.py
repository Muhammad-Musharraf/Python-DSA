arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search=int(input("Enter the number to search: "))

l=0
r=len(arr)-1
while l<=r:
    mid=(l+r)//2
    if arr[mid]==search:
        print("Element found at index: ", mid)
        break
    elif arr[mid]<search:
        l=mid+1
    else:
        r=mid-1
else:
    print("Element not found in the array.")