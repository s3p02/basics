import logging
import sys
class myAnagrams:
    def __init__(self,inputString1,inputString2):
        logging.debug("myAnagrams CLASS")
        self.inputString1 = inputString1.replace(" ","").lower()
        logging.debug("myAnagrams CLASS: inputString1 initialized --> "+self.inputString1)
        self.inputString2 = inputString2.replace(" ","").lower()
        logging.debug("myAnagrams CLASS: inputString2 initialized --> "+self.inputString2)
    
    def check(self):
        lenInputString1 = len(self.inputString1)
        logging.debug("myAnagrams CLASS: check METHOD: Length of Input String 1 --> "+str(lenInputString1))
        lenInputString2 = len(self.inputString2)
        logging.debug("\tmyAnagrams CLASS: check METHOD: Length of Input String 2 --> "+str(lenInputString2))

        if lenInputString1 != lenInputString2:
            logging.debug("myAnagrams CLASS: check METHOD: Checking if the provided strings are of same length or not --> False")
            return False

        alphabetsRef = "abcdefghijklmnopqrstuvwxyz"
        inputStringDict1 = dict.fromkeys(alphabetsRef,0)
        logging.debug("myAnagrams CLASS: check METHOD: Initializing inputStringDict1 for frequency count")
        inputStringDict2 = dict.fromkeys(alphabetsRef,0)
        logging.debug("myAnagrams CLASS: check METHOD: Initializing inputStringDict2 for frequency count")

        for i in range(lenInputString1):
            inputStringDict1[self.inputString1[i]] += 1
            logging.debug("myAnagrams CLASS: check METHOD: Counting Frequency of "+str(self.inputString1[i])+" inputStringDict1 --> "+str(inputStringDict1[self.inputString1[i]]))
            inputStringDict2[self.inputString2[i]] += 1
            logging.debug("myAnagrams CLASS: check METHOD: Counting Frequency of "+str(self.inputString2[i])+" inputStringDict2 --> "+str(inputStringDict2[self.inputString2[i]]))
        
        finalResult = inputStringDict1 == inputStringDict2
        logging.debug("myAnagrams CLASS: check METHOD: Final Result --> "+str(finalResult))
        return finalResult

class myString:
    def __init__(self,inputString):
        self.inputString = inputString
        logging.debug("myString CLASS: inputString initialized")
    
    def getReverse(self):
        logging.debug("myString CLASS: get function call")
        lenStr = len(self.inputString)
        strCpy = list(self.inputString)
        logging.debug("myString CLASS: get function call:"+str(lenStr))
        j=0
        logging.debug("myString CLASS: get function call:initial\tj="+str(j))
        for i in range(lenStr-1,0,-1):
            temp = strCpy[i]
            logging.debug("myString CLASS: get function call:\ttemp="+str(temp))
            strCpy[i] = strCpy[j]
            logging.debug("myString CLASS: get function call:\tinputString["+str(i)+"]="+str(strCpy[i]))
            strCpy[j] = temp
            logging.debug("myString CLASS: get function call:\tinputString["+str(j)+"]="+str(strCpy[j]))
            j +=1
            logging.debug("myString CLASS: get function call:\tj="+str(j))
        return ''.join(strCpy)