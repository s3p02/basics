class tb:
    def __init__(self,iTuple):
        self.iTuple = iTuple
    
    def printTuple(self):
        for i in self.iTuple:
            print(i)
    
    def checkForItem(self,item):
        if item in self.iTuple:
            print(str(item)+" exists in index: "+str(self.iTuple.index(item)))
        else:
            print(str(item)+" missing!\n")
    
    def checkForItemFrequency(self,item):
        print(str(item)+" occurs "+str(self.iTuple.count(item)))