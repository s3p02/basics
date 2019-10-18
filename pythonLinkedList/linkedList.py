class Node:
    def __init__(self, llnValue):
        self.val = llnValue
        self.next = None

    def getData(self):
        return self.val

    def getNext(self):
        return self.next
    
    def setNext(self,nextVal):
        self.next = nextVal

class linkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert(self,data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode
    
    def traverse(self):
        if self.head is None:
            print("LL has no element!")
            return
        else:
            ln = self.head
            while ln is not None:
                print(ln.val)
                ln = ln.next