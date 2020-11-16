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
        
    def printElements(self):
        current = self.head
        while(current):
            print(current.val)
            current = current.link
    
    def middleNode(self):
        result = []
        while self.head:
            result.append(self.head.val)
            self.head = self.head.link
        return result[len(result)//2]
            
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(6)
    ll.insert(10)
    ll.insert(12)
    ll.insert(24)
    ll.delete(24)
    ll.insert(23)
    ll.insert(100)
    ll.printElements()
    print(ll.middleNode())