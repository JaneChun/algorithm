# 스택을 2개 만들고, 하나는 요소를 저장하고 다른 하나는 그 시점의 최소값을 저장한다

class MinStack:
    stack: List[int]
    min_stack: List[int]

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.min_stack) == 0:
            self.min_stack.append(value)
        else:
            self.min_stack.append(min(value, self.min_stack[-1]))
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()