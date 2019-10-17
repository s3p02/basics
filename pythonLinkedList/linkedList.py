class Node:
    def __init__(self, llnValue):
        self.val = llnValue
        self.next = None
    def traverse(self):
        node = self
        nodeCount = 0
        while node != None:
            nodeCount +=1
            print("Node Value : "+str(node.val))
            node = node.next
            print("Node-Count: "+str(nodeCount))
    def traverseReturnSum(self):
        node = self
        sum = 0
        while node != None:
            sum += node.val
            node = node.next
        return sum