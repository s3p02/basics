import random
import time
def return_array(inputArray):
    return inputArray.sort()

#inputArray = ["Pass","Failed","Pass","Failed","Failed","Failed","Pass"]
choiceArray = ["Pass","Failed"]
inputArray = random.choices(choiceArray, k=10000)
startTime = time.time()
outputArray = return_array(inputArray)
print(time.time()-startTime)
#print(outputArray)
