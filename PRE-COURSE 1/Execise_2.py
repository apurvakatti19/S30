class Node: 
    def __init__(self,val): 
        self.val = val 
        self.link = None
      
class Stack: 
    def __init__(self): 
        self.head = None
        self.size = 0
       
    def isempty(self): 
        if self.head == None: 
            return True
        else: 
            return False
 
    def push(self,val): 
        if self.head == None: 
            self.head=Node(val) 
            self.size +=1    
        else: 
            newnode = Node(val) 
            newnode.link = self.head 
            self.head = newnode 
            self.size +=1  

    def pop(self): 
        if self.isempty(): 
            return None    
        else: 
            self.size -= 1
            poppednode = self.head 
            self.head = self.head.link
            poppednode.link = None
            return poppednode.val 
            
    def peek(self): 
        if self.isempty(): 
            return None  
        else: 
            return self.head.val 
     
    def display(self): 
        curr = self.head 
        if self.isempty(): 
            print("Stack Underflow") 
        else: 
            while curr != None: 
                print(curr.val,"->",end = " ") 
                curr = curr.link
            return
          
if __name__ == "__main__":
    myStack = Stack() 
    myStack.push(11)  
    myStack.push(22) 
    myStack.push(33) 
    myStack.push(44)  
    myStack.display()   
    print("Top element is ",myStack.peek())  
    myStack.pop() 
    myStack.pop()  
    myStack.display()  
    print("Top element is ", myStack.peek())   
    print("Size = ",myStack.size)