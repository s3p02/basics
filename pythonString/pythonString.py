import logging
import sys
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