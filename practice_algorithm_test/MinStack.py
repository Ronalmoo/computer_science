class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        return self.stack.append(x)
        

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
        
# test code
min_stack = MinStack()
print(min_stack.push(3))
print(min_stack.push(-1))
print(min_stack.push(0))
print(min_stack.push(5))
print(min_stack.push(7))
print(min_stack.pop())
print(min_stack.top())
print(min_stack.getMin())

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()