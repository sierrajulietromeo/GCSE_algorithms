cardList = [5,2,1,6,3,4,9,7,8]

for index in range(1,len(cardList)):

    currentvalue = cardList[index]
    position = index

    while position>0 and cardList[position-1]>currentvalue:
        cardList[position]=cardList[position-1]
        position = position-1

    cardList[position]=currentvalue


print(cardList)
