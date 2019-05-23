import random

random.seed()   #Prepare random number generator

cardList = [""] * (52)

cardList[0] = "2 of Hearts"
cardList[1] = "3 of Hearts"
cardList[2] = "4 of Hearts"
cardList[3] = "5 of Hearts"
cardList[4] = "6 of Hearts"
cardList[5] = "7 of Hearts"
cardList[6] = "8 of Hearts"
cardList[7] = "9 of Hearts"
cardList[8] = "10 of Hearts"
cardList[9] = "Jack of Hearts"
cardList[10] = "Queen of Hearts"
cardList[11] = "King of Hearts"
cardList[12] = "Ace of Hearts"

cardList[13] = "2 of Diamonds"
cardList[14] = "3 of Diamonds"
cardList[15] = "4 of Diamonds"
cardList[16] = "5 of Diamonds"
cardList[17] = "6 of Diamonds"
cardList[18] = "7 of Diamonds"
cardList[19] = "8 of Diamonds"
cardList[20] = "9 of Diamonds"
cardList[21] = "10 of Diamonds"
cardList[22] = "Jack of Diamonds"
cardList[23] = "Queen of Diamonds"
cardList[24] = "King of Diamonds"
cardList[25] = "Ace of Diamonds"

cardList[26] = "2 of Spades"
cardList[27] = "3 of Spades"
cardList[28] = "4 of Spades"
cardList[29] = "5 of Spades"
cardList[30] = "6 of Spades"
cardList[31] = "7 of Spades"
cardList[32] = "8 of Spades"
cardList[33] = "9 of Spades"
cardList[34] = "10 of Spades"
cardList[35] = "Jack of Spades"
cardList[36] = "Queen of Spades"
cardList[37] = "King of Spades"
cardList[38] = "Ace of Spades"

cardList[39] = "2 of Clubs"
cardList[40] = "3 of Clubs"
cardList[41] = "4 of Clubs"
cardList[42] = "5 of Clubs"
cardList[43] = "6 of Clubs"
cardList[44] = "7 of Clubs"
cardList[45] = "8 of Clubs"
cardList[46] = "9 of Clubs"
cardList[47] = "10 of Clubs"
cardList[48] = "Jack of Clubs"
cardList[49] = "Queen of Clubs"
cardList[50] = "King of Clubs"
cardList[51] = "Ace of Clubs"


# The following pointers point at the two random places that I will be swapping cards
# Temporary storage for a swapped card.
print("Please enter the number of shuffles you want to do")
numberOfShuffles = int(input())
i = 0
for i in range(0, numberOfShuffles + 1, 1):
    pointerOne = int(random.random() * 52)
    pointerTwo = int(random.random() * 52)
    temp = cardList[pointerOne]
    cardList[pointerOne] = cardList[pointerTwo]
    cardList[pointerTwo] = temp
i = 0
print("The shuffled cards are as follows:")
while i < len(cardList):
    print("Card: " + str(i+1) + "          " + cardList[i])
    i = i+1
