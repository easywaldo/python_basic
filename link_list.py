class Node:
    data = None
    next = None
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
def add(data):
    node = head
    while(node.next):
        node = node.next
    node.next = Node(data)
    
def append(node, data):
    newNode = Node(data)
    node.next = newNode


node1 = Node(1)
head = node1
for index in range(2,10):
    add(index)

node = head
while node.next:
    print("Node Data : ", node.data)
    node = node.next
print(node.data)

append(node, 100)
append(node, 99)
append(node, 77)
print(node.next)