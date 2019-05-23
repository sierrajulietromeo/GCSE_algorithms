arr = [5,7,2,6,8,4,1,3]


n = len(arr)
 
# Traverse through all array elements
for i in range(n):
 
  # Last i elements are already in place
  for j in range(0, n-i-1):
 
      # traverse the array from 0 to n-i-1
      # Swap if the element found is greater
      # than the next element
      if arr[j] > arr[j+1] :
          
          temp = arr[j]
          arr[j] = arr[j+1]
          arr[j+1] = temp
          
          
 
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]), 
