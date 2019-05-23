doorList = [""] * (100)

# Creates a doorList array of 100 elements and the loops sets the contents of each element to be "closed".

for i in range(0, 100, 1):
    doorList[i] = "closed"

# Declares an integer for the stepSize. (This will change each time (first step 1, second step 2, 3rd step 3 all the way...
stepSize = 0
for i in range(0, 100, 1):
    stepSize = stepSize + 1
    
    # This loop iterates through the array for the current stepsize.
    for k in range(0, 100, stepSize):
        
        # If the door is open, set it to be closed.
        # If the door is not open, it must be closed. So set it to open.
        if doorList[k] == "open":
            doorList[k] = "closed"
        else:
            doorList[k] = "open"


## Prints out the final array
for i in range(0,100, 1):
    print("Door ", i, " ",  doorList[i])

  
