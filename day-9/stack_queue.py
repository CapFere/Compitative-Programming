from collections import deque 
class MyStack:

    def __init__(self):
        self.queue = deque()
        """
        Initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        temp_queue = deque()
        temp_queue.append(x)
        while len(self.queue) != 0:
            temp_queue.append(self.queue.popleft())
        while len(temp_queue) != 0:
            self.queue.append(temp_queue.popleft())
        """
        Push element x onto stack.
        """
        

    def pop(self) -> int:
        temp_queue = deque()
        while len(self.queue) != 0:
            temp_queue.append(self.queue.popleft())
        item = temp_queue.popleft()
        while len(temp_queue) != 0:
            self.queue.append(temp_queue.popleft())
        return item
        """
        Removes the element on top of the stack and returns that element.
        """
        

    def top(self) -> int:
        temp_queue = deque()
        while len(self.queue) != 0:
            temp_queue.append(self.queue.popleft())
        copy_queue = temp_queue.copy()
        while len(temp_queue) != 0:
            self.queue.append(temp_queue.popleft())
        return copy_queue.popleft()
        """
        Get the top element.
        """
        

    def empty(self) -> bool:
        return True if len(self.queue) ==0 else False
        """
        Returns whether the stack is empty.
        """
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()