class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def add_first(self, e):
        newest = Node(e)
        newest.next = self.head
        self.size += 1
        
    def remove_first(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.size -= 1
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    