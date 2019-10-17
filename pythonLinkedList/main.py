from linkedList import *

if __name__ == "__main__":
    node1 = Node(2)
    node2 = Node(4)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    print("\nFirst Traversal\n")
    Node.traverse(node1)
    print("\nSecond Traversal\n")
    Node.traverse(node1)
    print("SUM: "+str(Node.traverseReturnSum(node1)))