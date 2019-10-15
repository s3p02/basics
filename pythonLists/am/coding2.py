import random
import time
def return_array(inputArray):
    resultArray = []
    for i in inputArray:
        if i == "Pass":
            resultArray.append("Pass")
        elif i == "Failed":
            resultArray.insert(0,"Failed")
    return resultArray

#inputArray = ["Pass","Failed","Pass","Failed","Failed","Failed","Pass"]
choiceArray = ["Pass","Failed"]
inputArray = random.choices(choiceArray, k=10000)
startTime = time.time()
outputArray = return_array(inputArray)
print(time.time()-startTime)
#print(outputArray)
