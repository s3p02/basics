class linkedListNode:
    def __init__(self, llnValue):
        self.val = llnValue
        self.next = None
    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next