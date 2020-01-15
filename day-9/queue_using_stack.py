class MyQueue:

    def __init__(self):
        self.stack = []
        """
        Initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        self.stack.append(x)
            
            
        """
        Push element x to the back of queue.
        """
        

    def pop(self) -> int:
        temp_stack = []
        while len(self.stack) != 0:
            temp_stack.append(self.stack.pop())
        item = temp_stack.pop()
        while len(temp_stack)!=0:
            self.stack.append(temp_stack.pop())
        return item
        
        """
        Removes the element from in front of queue and returns that element.
        """
        

    def peek(self) -> int:
        temp_stack = []
        while len(self.stack) != 0:
            temp_stack.append(self.stack.pop())
        copy_stack = temp_stack.copy()
        while len(temp_stack)!=0:
            self.stack.append(temp_stack.pop())
            
        return copy_stack.pop()
        """
        Get the front element.
        """
        

    def empty(self) -> bool:
        
        return True if len(self.stack)==0 else False
        """
        Returns whether the queue is empty.
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()