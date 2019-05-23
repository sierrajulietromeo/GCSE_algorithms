
numOfDoors = int(input("Please enter a number of doors: "))
stepSize = 0 # Declares an integer for the stepSize. (This will change each time (first step 1, second step 2, 3rd step 3 all the way...
# Creates a doorList array of n elements and the loops sets the contents of each element to be "closed".
doorList = [""] * (numOfDoors)

def setupDoors(numOfDoors):

  for i in range(0, numOfDoors, 1):
    doorList[i] = "closed"

  return None  


def loopThruDoors(numOfDoors, stepSize):

  for i in range(0, numOfDoors, 1):
      stepSize = stepSize + 1
      
      # This loop iterates through the array for the current stepsize.
      for k in range(0, numOfDoors, stepSize):
          
          # If the door is open, set it to be closed.
          # If the door is not open, it must be closed. So set it to open.
          if doorList[k] == "open":
              doorList[k] = "closed"
          else:
              doorList[k] = "open"

  return None

## Prints out the final array
def printArray(numOfDoors):
  for i in range(0,numOfDoors, 1):
    print("Door ", i, " ",  doorList[i])

  return None  



# Calls for the subroutines
setupDoors(numOfDoors)
loopThruDoors(numOfDoors, stepSize)
printArray(numOfDoors) 
