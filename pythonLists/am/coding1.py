import random
import time
def return_array(inputArray):
    countDict = {"Pass":0,
            "Failed":0}
    resultArray = []
    for i in inputArray:
        countDict[i] +=1
        if i == "Failed":
            resultArray.append("Failed")
    #for j in range(countDict["Failed"]):
        #resultArray.append("Failed")
    for j in range(countDict["Pass"]):
        resultArray.append("Pass")
    return resultArray

##inputArray = ["Pass","Failed","Pass","Failed","Failed","Failed","Pass"]
choiceArray = ["Pass","Failed"]
inputArray = random.choices(choiceArray, k=10000)
startTime = time.time()
outputArray = return_array(inputArray)
print(time.time() - startTime)
#print(outputArray)
