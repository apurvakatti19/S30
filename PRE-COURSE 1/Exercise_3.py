class Node:
    def __init__(self,val = None,link = None):
        self.val = val
        self.link = link
        
class LinkedList:
    def __init__(self,head = None):
        self.head = head
        
    def insert(self,value):
        newNode = Node(value,self.head)
        self.head = newNode
        
    def printElements(self):
        current = self.head
        while(current):
            print(current.val)
            current = current.link

    def delete(self,valueToBeDeleted):
        if self.head.val == valueToBeDeleted:
            next = self.head.link
            self.head.link = None
            self.head = next
        else:
            prev = None
            current = self.head
            while(current):
                if current.val == valueToBeDeleted:
                    prev.link = current.link
                    break
                else:
                    prev = current
                    current = current.link
        
    def reverse(self):
        prev = None
        current = self.head
        nextnode =  None
        while(current):
            nextNode = current.link
            current.link = prev
            prev = current
            current = nextNode
        self.head = prev
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(6)
    ll.insert(10)
    ll.insert(12)
    ll.insert(24)
    ll.printElements()
    ll.delete(24)
    ll.printElements()
    ll.delete(10)
    ll.printElements()
    ll.insert(23)
    ll.insert(56)
    ll.insert(51)
    ll.printElements()
    ll.reverse()
    ll.printElements()