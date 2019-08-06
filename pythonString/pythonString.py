class myString:
    def __init__(self,inputString):
        self.inputString = inputString
        print("reverseString CLASS: inputString initialized")
    
    def getReverse(self):
        print("reverseString CLASS: get function call")
        lenStr = len(self.inputString)
        strCpy = list(self.inputString)
        print("reverseString CLASS: get function call:"+str(lenStr))
        j=0
        print("reverseString CLASS: get function call:initial\tj="+str(j))
        for i in range(lenStr-1,0,-1):
            temp = strCpy[i]
            print("reverseString CLASS: get function call:\ttemp="+str(temp))
            strCpy[i] = strCpy[j]
            print("reverseString CLASS: get function call:\tinputString["+str(i)+"]="+str(strCpy[i]))
            strCpy[j] = temp
            print("reverseString CLASS: get function call:\tinputString["+str(j)+"]="+str(strCpy[j]))
            j +=1
            print("reverseString CLASS: get function call:\tj="+str(j))
        return ''.join(strCpy)

if __name__ == "__main__":
    st1 = myString("Sree")
    print("RESULT:"+st1.getReverse())