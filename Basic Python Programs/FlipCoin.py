import random
import sys 
def test_positive_int(x):       # Ensure it is a positive Integer
    if int(x) > 0: 
        return int(x)  
    else:
        sys.exit("Enter Positive Integer")

numberOfFlips = test_positive_int(input("The number of times to Flip Coin: "))
countHeads = countTails = 0
for flip in range(numberOfFlips):
    if (random.random() > 0.5): 
        countHeads +=  1
    else:
        countTails +=  1
print("Percentage of Heads: {}% \n Percentage of Tails: {}%".format((countHeads/numberOfFlips)*100, (countTails/numberOfFlips)*100))