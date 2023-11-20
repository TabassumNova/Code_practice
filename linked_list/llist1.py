
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtBegin(head, data):
    new_node = Node(data)
    new_node.next = head
    while (new_node):
        print(new_node.data)
        new_node = new_node.next

def printRecurssive(head):
    if head:
        print(head.data)
        printRecurssive(head.next)


def insertAtBeginRecurssive(head, data):
    new_node = Node(data)
    new_node.next = head
    printRecurssive(new_node)

if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # insertAtBegin(a, 'X')
    insertAtBeginRecurssive(a, 'X')