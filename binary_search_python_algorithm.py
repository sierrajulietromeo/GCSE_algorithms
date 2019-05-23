arr = [10,16,23,32,37,44,56,63,72,84,91]

sought = int(input("Enter a number to find"))

min = 0
max = len(arr)-1
found = False
    
while( min<=max and found == False):
    mid = (min + max)//2
    if arr[mid] == sought :
        found = True
    else:
        if sought > arr[mid]:
            min = mid + 1
        else:
            max = mid - 1    
    
    
if found == True:
    print("Number found at position: ", mid)
    
else:
    print("Number not found")
