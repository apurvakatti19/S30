class Stack:
    def __init__(self):
        self.stack = list()

    def push(self,element):
        self.stack.append(element)


    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1]


    def pop(self):
        return self.stack.pop()

    def display(self):
        result = ' '.join([str(element) for element in self.stack])
        print(result)
    
    def size(self):
        return len(self.stack)

if __name__ == "__main__":
    myStack = Stack()
    myStack.push(4)
    myStack.push(100)
    myStack.push("ComputerScience")
    myStack.push("20.0")
    print(myStack.pop())
    print(myStack.size())
    print(myStack.isEmpty())
    print(myStack.pop())
    print(myStack.pop())
    myStack.display()
    print(myStack.peek())
    myStack.push(23)
    myStack.push(77)
    print(myStack.peek())
    myStack.display()