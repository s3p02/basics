class myStream:
    """\nmyStream-CLASS - Holds a stream of numbers.\n
    Upon initialization a BOUND is provided.\n
    BOUND determines the total number of elements a stream can hold at any give time.\n
    myStream-CLASS has 3 methods: updateStream,getAverage & getStream.\n
    """
    holdStream = []
    
    def __init__(self,inputBound):
        print("\n\t\tINITIALIZATION\t\t\n")
        self.inputBound = inputBound
        print("BOUND:"+str(self.inputBound))
    
    def updateStream(self,inputElement):
        """myStream-CLASS method: updateStream.\n
        This method updates the stream with an input-element.\n
        The method enforces the BOUND, such that upon the method call, if length of stream exceeds BOUND, element 0 of STREAM is removed/dropped.\n
        """
        print("\n\t\tUPDATE-CALL\t\t\n")
        lenStream = len(self.holdStream)
        print("Len:"+str(lenStream))
        if lenStream < self.inputBound:
            self.holdStream.append(inputElement)
            print("UPDATE:\tSTREAM-->\t"+str(self.holdStream))
        else:
            removedElement = self.holdStream.pop(0)
            print("REMOVED [0] -->"+str(removedElement)+"\tSTREAM="+str(self.holdStream))
            self.holdStream.append(inputElement)
            print("UPDATE:\tSTREAM-->\t"+str(self.holdStream))
    
    def getAverage(self):
        """myStream-CLASS method: updateStream.\n
        This method returns the average[float] of the STREAM
        """
        print("\n\t\tAVERAGE-CALL\t\t\n")
        sumOfStream = 0
        lenStream = len(self.holdStream)
        for i in range(lenStream):
            sumOfStream += self.holdStream[i]
            print("SUM:"+str(i)+" --> "+str(sumOfStream))
        print("TOTAL:"+" -->"+str(sumOfStream))
        computeAvg = float(sumOfStream)/float(lenStream)
        print("AVERAGE:"+str(computeAvg))
        return computeAvg
    
    def getStream(self):
        """myStream-CLASS method: getStream.\n
        This method returns the entire STREAM[array]
        """
        print("\n\t\tSTREAM-CALL\t\t\n")
        return self.holdStream