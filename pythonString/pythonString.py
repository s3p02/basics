import logging
import sys
class myString:
    def __init__(self,inputString):
        self.inputString = inputString
        logging.debug("reverseString CLASS: inputString initialized")
    
    def getReverse(self):
        logging.debug("reverseString CLASS: get function call")
        lenStr = len(self.inputString)
        strCpy = list(self.inputString)
        logging.debug("reverseString CLASS: get function call:"+str(lenStr))
        j=0
        logging.debug("reverseString CLASS: get function call:initial\tj="+str(j))
        for i in range(lenStr-1,0,-1):
            temp = strCpy[i]
            logging.debug("reverseString CLASS: get function call:\ttemp="+str(temp))
            strCpy[i] = strCpy[j]
            logging.debug("reverseString CLASS: get function call:\tinputString["+str(i)+"]="+str(strCpy[i]))
            strCpy[j] = temp
            logging.debug("reverseString CLASS: get function call:\tinputString["+str(j)+"]="+str(strCpy[j]))
            j +=1
            logging.debug("reverseString CLASS: get function call:\tj="+str(j))
        return ''.join(strCpy)

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    st1 = myString("Sree")
    logging.debug("RESULT:"+st1.getReverse())