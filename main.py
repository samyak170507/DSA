class Node:

    def __init__(self,value):

        self.value = value
        self.next = None


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3

head = n1
curr = head

while curr:
    print(curr.value)
    curr = curr.next
    