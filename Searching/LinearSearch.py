arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search=int(input("Enter the number to search: "))


for i in range(len(arr)):
    if arr[i]==search:
        print("Element found at index: ", i)
        break
else:
    print("Element not found in the array.")
