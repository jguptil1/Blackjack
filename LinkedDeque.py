class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedDeque:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def pushFront(self, value):
        if self.head == None: #if we are dealing with an empty deque
            self.head = Node(value, next=None)
            self.tail = self.head
        else:
            self.head = Node(value, next = self.head)


    def popFront(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            value = self.head.value
            self.head = self.head.next
            return value

    def peekFront(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            return self.head


    def isEmpty(self) -> bool:
        if self.head == None:
            return True
        else:
            return False
        

