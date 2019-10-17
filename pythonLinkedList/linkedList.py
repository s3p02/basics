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