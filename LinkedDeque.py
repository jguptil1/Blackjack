class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedDeque:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def pushFront(self, value):
        self.head = Node(value, next=self.head)

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
            return


    def isEmpty(self) -> bool:
        if self.head == None:
            return True
        else:
            return False
        

